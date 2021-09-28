#!/bin/bash

echo CHECKING: player create - name: Gamma
curl -i -H 'Content-Type: application/json' -d '{"name":"Gamma"}' http://localhost:8083/player/create
echo

echo CHECKING: player get - id: 3
echo
curl -i -H 'Content-Type: application/json' -d '{"id": "3"}' http://localhost:8083/player/get
echo

echo CHECKING: player get - name: Alpha
echo
curl -i -H 'Content-Type: application/json' -d '{"name":"Alpha"}' http://localhost:8083/player/get
echo
echo CHECKING: player get - name: Gamma
echo
curl -i -H 'Content-Type: application/json' -d '{"name":"Gamma"}' http://localhost:8083/player/get
echo
echo CHECKING: player get - name: Oscar
echo
curl -i -H 'Content-Type: application/json' -d '{"name":"Oscar"}' http://localhost:8083/player/get
echo
