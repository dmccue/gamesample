#!/bin/bash

#pip install -r requirements.txt
docker-compose up --build --scale webapp=3
