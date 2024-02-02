#!/bin/bash

DIRECTORY=/opt/integration-ais-ado/;

cd $DIRECTORY;

docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY;

docker-compose pull;
docker-compose down;
docker-compose up -d;
