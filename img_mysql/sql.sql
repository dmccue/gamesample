CREATE DATABASE `gamesample`;
DROP TABLE IF EXISTS `player`;
CREATE TABLE `player` (
	`identifier` VARCHAR,
	`name` VARCHAR(20),
	`gold_amount` INT(10),
	PRIMARY KEY (`identifier`,`name`)
);
