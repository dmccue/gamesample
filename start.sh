#!/bin/bash

export REDIS_AUTH=ComplexPassword123
export MYSQL_ROOT_PASSWORD=ComplexPassword123
export MYSQL_DATABASE=gamesample
export MYSQL_USER=gamesample
export MYSQL_PASSWORD=gamesample

webappnum=3
[ "$1" ] && webappnum=$1
docker-compose up --build --scale webapp=$webappnum
