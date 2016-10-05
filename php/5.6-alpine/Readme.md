## Overview

- PHP5.6 with Composer, on Alpine Linux.
- Slim (as anything based on Alpine), and easy to use
- Based on official PHP docker image (`php:5.6-alpine`)

[![](https://images.microbadger.com/badges/image/farazdagi/php:5.6-alpine.svg)](https://microbadger.com/images/farazdagi/php:5.6-alpine "Get your own image badge on microbadger.com")


## Getting the image from Docker Hub

```
docker pull farazdagi/php:5.6-alpine
```

## Using Composer (to install dependencies, for ex)

Go to any directory that contains `composer.json`, and run composer command:

```
docker run -it --rm -v $(pwd):/var/www farazdagi/php:5.6-alpine "composer intall --prefer-dist"
```

## Using PHP

To run arbitrary PHP command:

```
docker run -it --rm -v $(pwd):/var/www farazdagi/php:5.6-alpine "php --version"
```

Quite similarly, you can run executables installed into `vendor` folder:
```
docker run -it --rm -v $(pwd):/var/www farazdagi/php:5.6-alpine "./vendor/bin/phpunit --version"
```

## Re-use as base image

Use for any PHP based tools (as base image in your `Dockerfile`):

```
FROM farazdagi/php:5.6-alpine

// custom directives
```


