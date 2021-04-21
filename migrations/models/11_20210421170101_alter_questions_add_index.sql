-- upgrade --
ALTER TABLE questions ADD INDEX `owner_id` (`owner_id` );
-- downgrade --
ALTER TABLE questions DROP INDEX `owner_id`;