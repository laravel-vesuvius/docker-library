## Overview

- PHP7 with Composer, on Alpine Linux.
- Slim (as anything based on Alpine), and easy to use
- Based on official PHP docker image (`php:alpine`)

[![](https://badge.imagelayers.io/farazdagi/php:latest.svg)](https://imagelayers.io/?images=farazdagi/php:latest 'Get your own badge on imagelayers.io')


## Getting the image from Docker Hub

```
docker pull farazdagi/php
```

## Using Composer (to install dependencies, for ex)

Go to any directory that contains `composer.json`, and run composer command:

```
docker run -it --rm -v $(pwd):/var/www farazdagi/php "composer intall --prefer-dist"
```

## Using PHP

To run arbitrary PHP command:

```
docker run -it --rm -v $(pwd):/var/www farazdagi/php "php --version"
```

Quite similarly, you can run executables installed into `vendor` folder:
```
docker run -it --rm -v $(pwd):/var/www farazdagi/php "./vendor/bin/phpunit --version"
```

## Re-use as base image

Use for any PHP based tools (as base image in your `Dockerfile`):

``
FROM farazdagi/php:latest

// custom directives
``

