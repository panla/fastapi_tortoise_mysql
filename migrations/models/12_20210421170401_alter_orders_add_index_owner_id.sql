-- upgrade --
ALTER TABLE orders ADD INDEX `owner_id` (`owner_id` );
-- downgrade --
ALTER TABLE orders DROP INDEX `owner_id`;