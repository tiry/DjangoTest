#!/bin/bash

docker build . -t tiry-pyserver
docker tag tiry-pyserver:latest

