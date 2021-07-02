-- upgrade --
CREATE TABLE IF NOT EXISTS `phones` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '主键',
    `created_at` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_delete` BOOL NOT NULL  COMMENT '删除标识' DEFAULT 0,
    `brand` VARCHAR(100) NOT NULL  COMMENT '品牌',
    `price` INT NOT NULL  COMMENT '价格,分',
    KEY `idx_phones_brand_2ff5b1` (`brand`)
) CHARACTER SET utf8mb4 COMMENT='手机表';
-- downgrade --
DROP TABLE IF EXISTS `phones`;
