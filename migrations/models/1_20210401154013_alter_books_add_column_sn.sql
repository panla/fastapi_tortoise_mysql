-- upgrade --
ALTER TABLE `books` ADD `sn` VARCHAR(100) NOT NULL UNIQUE COMMENT '序列号';
-- downgrade --
ALTER TABLE `books` DROP COLUMN `sn`;
