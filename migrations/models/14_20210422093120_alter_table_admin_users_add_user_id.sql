-- upgrade --
ALTER TABLE `admin_users` ADD `user_id` BIGINT NOT NULL COMMENT '用户id';
ALTER TABLE `admin_users` ADD UNIQUE INDEX `uid_admin_users_user_id_025014` (`user_id`);
-- downgrade --
ALTER TABLE `admin_users` DROP INDEX `uid_admin_users_user_id_025014`;
ALTER TABLE `admin_users` DROP COLUMN `user_id`;
