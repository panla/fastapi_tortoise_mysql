-- upgrade --
ALTER TABLE `admin_users` DROP COLUMN `user_id`;
-- downgrade --
ALTER TABLE `admin_users` ADD `user_id` BIGINT NOT NULL UNIQUE COMMENT '用户id';
