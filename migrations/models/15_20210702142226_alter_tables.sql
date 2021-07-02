-- upgrade --
ALTER TABLE `books` DROP INDEX `sn`;
ALTER TABLE `books` ADD UNIQUE INDEX `uid_books_sn_7a31d1` (`sn`);
ALTER TABLE `users` DROP INDEX `cellphone`;
ALTER TABLE `users` ADD UNIQUE INDEX `uid_users_cellpho_d65b44` (`cellphone`);
-- downgrade --
