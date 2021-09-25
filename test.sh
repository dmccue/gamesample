#!/bin/bash

curl -i -H 'Content-Type: application/json' -d '{"name":"Gamma"}' http://localhost:8083/player/create
echo

curl -i -H 'Content-Type: application/json' -d '{"id": "3"}' http://localhost:8083/player/get
echo

curl -i -H 'Content-Type: application/json' -d '{"name":"Alpha"}' http://localhost:8083/player/get
echo
curl -i -H 'Content-Type: application/json' -d '{"name":"Gamma"}' http://localhost:8083/player/get
echo
curl -i -H 'Content-Type: application/json' -d '{"name":"Oscar"}' http://localhost:8083/player/get
echo