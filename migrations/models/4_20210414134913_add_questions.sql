-- upgrade --
CREATE TABLE IF NOT EXISTS `questions` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '主键',
    `created_at` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_delete` BOOL NOT NULL  COMMENT '删除标识' DEFAULT 0,
    `owner_id` BIGINT NOT NULL  COMMENT '提问者',
    `title` VARCHAR(100) NOT NULL  COMMENT '问题',
    `content` LONGTEXT NOT NULL  COMMENT '问题内容',
    KEY `idx_questions_owner_i_932a50` (`owner_id`)
) CHARACTER SET utf8mb4;
-- downgrade --
DROP TABLE IF EXISTS `questions`;
