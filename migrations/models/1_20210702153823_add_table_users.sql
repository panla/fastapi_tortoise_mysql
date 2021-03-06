-- upgrade --
CREATE TABLE IF NOT EXISTS `users` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '主键',
    `created_at` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_delete` BOOL NOT NULL  COMMENT '删除标识' DEFAULT 0,
    `cellphone` VARCHAR(16) NOT NULL  COMMENT '手机号',
    `name` VARCHAR(30) NOT NULL  COMMENT '用户名',
    UNIQUE KEY `uid_users_cellpho_d65b44` (`cellphone`)
) CHARACTER SET utf8mb4 COMMENT='用户表';
-- downgrade --
DROP TABLE IF EXISTS `users`;
