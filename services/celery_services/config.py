from kombu import Queue, Exchange


class MQConfig:
    pass


class RedisConfig:
    pass


class CeleryConfig:
    # 1，任务队列 代理设置
    broker_url = f'amqp://{MQConfig.USER}:{MQConfig.PASSWD}@{MQConfig.HOST}:{MQConfig.PORT}'

    # 2，结果存储 默认，无
    result_backend  = f'redis://{RedisConfig.USER}:{RedisConfig.PASSWD}@{RedisConfig.HOST}:{RedisConfig.PORT}/0'

    # 3，存储结果，过期时间为 一小时
    result_expires = 60 * 60

    # 4，禁用 UTC
    enable_utc = False

    # 5，时区
    timezone = 'Asia/Shanghai'

    # 6，允许的接收的内容类型/序列化程序的白名单 默认，json
    accept_content = ['json']
    # 允许结果后端的内容类型/序列化程序的白名单 默认，与 accept_content 相同
    # result_accept_content

    # 7，以秒为单位的任务硬时间限制 默认，无
    # task_time_limit = 100

    DefaultExchangeType = 'direct'

    class QueueNameConst:
        default = 'celery-default-queue'
        test = 'celery-test-queue'
        pay = 'celery-pay-queue'

    class ExchangeConst:
        default = 'celery-default-exchange'
        test = 'celery-test-exchange'
        pay = 'celery-pay-exchange'

    class RoutingKeyConst:
        default = 'celery-default-routing'
        test = 'celery-test-routing'
        pay = 'celery-pay-routing'

    # 8，default
    # 消息没有路由或没有指定自定义队列使用的默认队列名称，默认值，celery
    task_default_queue = QueueNameConst.default
    # 当没有为设置中键指定自定义交换时使用的交换的名称
    task_default_exchange = ExchangeConst.default
    # 当没有为设置中键指定自定义交换类型时使用的交换类型，默认值，direct
    task_default_exchange_type = DefaultExchangeType
    # 当没有为设置中键指定自定义路由键时使用的路由键
    task_default_routing_key = RoutingKeyConst.default

    define_exchange = {
        'test': Exchange(name=ExchangeConst.test, type=DefaultExchangeType),
        'pay': Exchange(name=ExchangeConst.pay, type=DefaultExchangeType)
    }

    # 9，消息路由 使用 kombu.Queue
    task_queues = (
        Queue(name=QueueNameConst.pay, exchange=define_exchange.get('pay'), routing_key=RoutingKeyConst.pay),
    )

    # 10，路由列表把任务路由到队列的路由
    task_routes = {
        'pay': {'exchange': define_exchange.get('pay').name, 'routing_key': RoutingKeyConst.pay}
    }
