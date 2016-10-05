#!/bin/sh
ROOT=$PWD

# PHP 5.6
cd "$ROOT/5.6-alpine"
docker build -t farazdagi/php:5.6-alpine .

cd "$ROOT/5.6-alpine/nginx"
docker build -t farazdagi/php:5.6-nginx-alpine .

# PHP 7.0
cd "$ROOT/7.0-alpine"
docker build -t farazdagi/php:7.0-alpine .

cd "$ROOT/7.0-alpine/nginx"
docker build -t farazdagi/php:7.0-nginx-alpine .

docker tag farazdagi/php:7.0-alpine farazdagi/php:latest
docker tag farazdagi/php:7.0-nginx-alpine farazdagi/php:nginx

docker push farazdagi/php
