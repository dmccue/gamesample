#!/bin/bash

curl -i -H 'Content-Type: application/json' -d '{"id": "874301557", "name":"Gamma"}' http://localhost:8083/player/create
echo

curl -i -H 'Content-Type: application/json' -d '{"id": "874301557", "name":"Gamma"}' http://localhost:8083/player/get
echo