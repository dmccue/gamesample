CREATE DATABASE IF NOT EXISTS gamesample;
DROP TABLE IF EXISTS gamesample.player;

CREATE TABLE gamesample.player ( identifier INT NOT NULL, player_name VARCHAR(20) NOT NULL, gold_amount INT(10), PRIMARY KEY (player_name, identifier), UNIQUE (player_name) );

INSERT INTO gamesample.player(identifier, player_name, gold_amount)
VALUES(927312837,'Alpha',999999999),
      (127312123,'Bravo',8119),
	  (327312456,'Charlie',912),
	  (673829382,'Delta',190);
