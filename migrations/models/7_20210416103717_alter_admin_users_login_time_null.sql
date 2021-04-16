-- upgrade --
ALTER TABLE `admin_users` MODIFY COLUMN `login_time` DATETIME(6)   COMMENT '登录时间';
ALTER TABLE `admin_users` MODIFY COLUMN `token_expired` DATETIME(6)   COMMENT '登录过期时间';
-- downgrade --
ALTER TABLE `admin_users` MODIFY COLUMN `login_time` DATETIME(6) NOT NULL  COMMENT '登录时间';
ALTER TABLE `admin_users` MODIFY COLUMN `token_expired` DATETIME(6) NOT NULL  COMMENT '登录过期时间';
