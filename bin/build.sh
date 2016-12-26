#!/bin/sh
ROOT=$PWD

# PHP 5.6 (Ubuntu)
cd "$ROOT/5.6-ubuntu"
docker build -t farazdagi/php:5.6-ubuntu .
cd "$ROOT/5.6-ubuntu/nginx"
docker build -t farazdagi/php:5.6-ubuntu-alpine .

# PHP 5.6 (Alpine)
cd "$ROOT/5.6-alpine"
docker build -t farazdagi/php:5.6-alpine .
cd "$ROOT/5.6-alpine/nginx"
docker build -t farazdagi/php:5.6-nginx-alpine .

# PHP 7.0
cd "$ROOT/7.0-alpine"
docker build -t farazdagi/php:7.0-alpine .
cd "$ROOT/7.0-alpine/nginx"
docker build -t farazdagi/php:7.0-nginx-alpine .

# extra tags
docker tag farazdagi/php:7.0-alpine farazdagi/php:latest
docker tag farazdagi/php:7.0-nginx-alpine farazdagi/php:nginx


# push images and update badges
docker push farazdagi/php
http post https://hooks.microbadger.com/images/farazdagi/php/V1fr9W4DsgOKNW6tHYg-YugBQMs=
