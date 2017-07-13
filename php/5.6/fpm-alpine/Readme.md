## Overview

- PHP FPM 5.6 with Composer, and pgsql, gd, mcrypt, redis PHP extensions on Alpine Linux.
- Slim (as anything based on Alpine), and easy to use
- Based on official PHP docker image (`php:5.6-fpm-alpine`)

[![](https://images.microbadger.com/badges/image/osenio/php:5.6-fpm-alpine.svg)](https://microbadger.com/images/osenio/php:5.6-fpm-alpine "Get your own image badge on microbadger.com")


## Getting the image from Docker Hub

```
docker pull osenio/php:5.6-fpm-alpine
```

## Using Composer (to install dependencies, for ex)

Go to any directory that contains `composer.json`, and run composer command:

```
docker run -it --rm -v $(pwd):/var/www osenio/php:5.6-fpm-alpine "composer intall --prefer-dist"
```

## Using PHP

To run arbitrary PHP command:

```
docker run -it --rm -v $(pwd):/var/www osenio/php:5.6-fpm-alpine "php --version"
```

Quite similarly, you can run executables installed into `vendor` folder:
```
docker run -it --rm -v $(pwd):/var/www osenio/php:5.6-fpm-alpine "./vendor/bin/phpunit --version"
```

## Re-use as base image

Use for any PHP based tools (as base image in your `Dockerfile`):

```
FROM osenio/php:5.6-fpm-alpine

// custom directives
```
