## Overview

- Nginx node with SSL installed, on Alpine Linux.
- Based on alpine docker image (`alpine:3.4`)
- Uses instructions from the official nginx image (`nginx:alpine`)
- Process (`nginx`) are manager by supervisord

[![](https://images.microbadger.com/badges/image/osenio/nginx:1.13.3-alpine.svg)](https://microbadger.com/images/osenio/nginx:1.13.3-alpine "Get your own image badge on microbadger.com")


## Getting the image from Docker Hub

```
docker pull osenio/nginx:1.13.3-alpine
```

## Running container for Symfony project

Go to project directory and run:

```
docker network create --driver bridge my_network_with_fpm
docker run -it --rm -v $(pwd):/var/www/ --network=my_network_with_fpm --network-alias=php_fpm -p 80:80 osenio/nginx:1.13.3-alpine
```

To add custom config create your `site.conf` and run:
```
docker run -it --rm -v $(pwd):/var/www/ -v $(pwd)/site.conf:/etc/nginx/conf.d/default.conf -p 80:80 osenio/nginx:1.13.3-alpine
```

Where `site.conf` configured like described [here](http://nginx.org/en/docs/beginners_guide.html#conf_structure).

## Overriding Nginx configuration

To override `nginx.conf`, pass `-v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro`:

```
docker run -it --rm -v $(pwd):/var/www/ -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro -p 80:80 osenio/nginx:1.13.3-alpine
```

## Re-use as base image

Use for any PHP based tools (as base image in your `Dockerfile`):

```
FROM osenio/nginx:1.13.3-alpine

// custom directives
```
