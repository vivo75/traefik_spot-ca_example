#! /usr/bin/bash

docker run -d -p 8080:8080 -p 80:80 \
 -v $PWD/traefik.yml:/etc/traefik/traefik.yml \
 -v /var/run/docker.sock:/var/run/docker.sock \
 traefik:v2.10

docker run -d --name test traefik/whoami

curl --header 'Host:test.docker.localhost' 'http://localhost:80/'


