-- upgrade --
CREATE TABLE IF NOT EXISTS `books` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '主键',
    `created_at` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_delete` BOOL NOT NULL  COMMENT '删除标识' DEFAULT 0,
    `name` VARCHAR(100) NOT NULL  COMMENT '书名',
    `price` INT NOT NULL  COMMENT '价格,分',
    `sn` VARCHAR(100) NOT NULL  COMMENT '序列号',
    UNIQUE KEY `uid_books_sn_7a31d1` (`sn`),
    KEY `idx_books_name_3562e3` (`name`)
) CHARACTER SET utf8mb4 COMMENT='书籍表';
-- downgrade --
DROP TABLE IF EXISTS `books`;
