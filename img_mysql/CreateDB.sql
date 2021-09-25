CREATE DATABASE IF NOT EXISTS gamesample;
DROP TABLE IF EXISTS gamesample.player;

CREATE TABLE gamesample.player (
	id INT(10) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
	player_name VARCHAR(20) NOT NULL,
	gold_amount INT(10) unsigned NOT NULL,
	INDEX(id),
	UNIQUE(id,player_name)
);

INSERT INTO gamesample.player(player_name, gold_amount)
VALUES('Alpha',999999999),
      ('Bravo',8119),
	  ('Charlie',912),
	  ('Delta',190);
