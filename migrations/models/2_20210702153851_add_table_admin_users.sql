-- upgrade --
CREATE TABLE IF NOT EXISTS `admin_users` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '主键',
    `created_at` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_delete` BOOL NOT NULL  COMMENT '删除标识' DEFAULT 0,
    `login_time` DATETIME(6)   COMMENT '登录时间',
    `token_expired` DATETIME(6)   COMMENT '登录过期时间',
    `user_id` BIGINT NOT NULL UNIQUE
) CHARACTER SET utf8mb4 COMMENT='管理员表';
-- downgrade --
DROP TABLE IF EXISTS `admin_users`;
