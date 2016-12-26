## Overview

- PHP7.0 with Composer, on Alpine Linux.
- Slim (as anything based on Alpine), and easy to use
- Based on official PHP docker image (`php:7.0-alpine`)

[![](https://images.microbadger.com/badges/image/slabs/php:7.0-alpine.svg)](https://microbadger.com/images/slabs/php:7.0-alpine "Get your own image badge on microbadger.com")


## Getting the image from Docker Hub

```
docker pull slabs/php
```

## Using Composer (to install dependencies, for ex)

Go to any directory that contains `composer.json`, and run composer command:

```
docker run -it --rm -v $(pwd):/project slabs/php "composer intall --prefer-dist"
```

## Using PHP

To run arbitrary PHP command:

```
docker run -it --rm -v $(pwd):/project slabs/php "php --version"
```

Quite similarly, you can run executables installed into `vendor` folder:
```
docker run -it --rm -v $(pwd):/project slabs/php "./vendor/bin/phpunit --version"
```

## Re-use as base image

Use for any PHP based tools (as base image in your `Dockerfile`):

```
FROM slabs/php:7.0-alpine

// custom directives
```


