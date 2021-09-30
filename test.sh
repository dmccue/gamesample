#!/bin/bash

echo CHECKING: player create - name: Gamma
curl -i -H 'Content-Type: application/json' -d '{"name":"Gamma"}' http://localhost:8083/player/create
echo

echo CHECKING: player get - id: 3
echo
curl -i http://localhost:8083/player/get?id=3
echo

echo CHECKING: player get - name: Alpha
echo
curl -i http://localhost:8083/player/get?name=Alpha
echo
echo CHECKING: player get - name: Gamma
echo
curl -i http://localhost:8083/player/get?name=Gamma
echo
echo CHECKING: player get - name: Oscar
echo
curl -i http://localhost:8083/player/get?name=Oscar
echo
