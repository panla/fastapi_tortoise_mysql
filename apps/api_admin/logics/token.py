from config import Config
from extensions import NotFound, BadRequest
from redis_ext import SMSCodeRedis, TokenRedis
from apps.models import User, AdminUser
from apps.modules import TokenResolver


class LoginResolver:
    EXTEND_MODEL_MAP = {'AdminUser': AdminUser}

    @classmethod
    async def authentic(cls, cellphone: str, code: str, extend_model: str) -> dict:
        """the entrance to get auth token"""

        sms_redis_op = SMSCodeRedis(cellphone)
        if code == await sms_redis_op.get():
            user, extend_user = await cls.check_user(cellphone, extend_model)

            token, login_time, token_expired = TokenResolver.encode_auth_token(user.id, extend_user.id, 'AdminUser')

            extend_user.login_time = login_time
            extend_user.token_expired = token_expired
            await extend_user.save()

            # save redis
            token_redis_op = TokenRedis(cellphone, extend_model, extend_user.id)
            await token_redis_op.set(token, ex=Config.authentic.ADMIN_TOKEN_EXP_DELTA)

            rt = {'token': token, 'user_id': user.id, 'extend_user_id': extend_user.id, 'extend_model': 'AdminUser'}
            return rt
        raise BadRequest(message='SMS Code error')

    @classmethod
    async def check_user(cls, cellphone: str, extend_model: str):
        Model = cls.EXTEND_MODEL_MAP.get(extend_model)
        if not Model:
            raise BadRequest(message=f'Model {extend_model} error')

        user = await User.filter(cellphone=cellphone, is_delete=False).first()
        if not user:
            raise NotFound(f'User User.cellphone = {cellphone} is not exists or is deleted')

        extend_user = await Model.filter(user_id=user.id, is_delete=False).first()
        if not extend_user:
            raise NotFound(message=f'{extend_model} User.cellphone = {cellphone} is not exists or is deleted')

        return user, extend_user
