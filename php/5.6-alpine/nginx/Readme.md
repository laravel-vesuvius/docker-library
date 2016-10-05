## Overview

- Nginx node with PHP5.6 (FPM) installed, on Alpine Linux.
- Based on official PHP docker image (`php:5.6-fpm-alpine`)
- Uses instructions from the official nginx image (`nginx:alpine`)
- Processes (`php-fpm` and `nginx`) are manager by supervisord

[![](https://images.microbadger.com/badges/image/farazdagi/php:5.6-nginx-alpine.svg)](https://microbadger.com/images/farazdagi/php:5.6-nginx-alpine "Get your own image badge on microbadger.com")


## Getting the image from Docker Hub

```
docker pull farazdagi/php:5.6-nginx-alpine
```

## Running container

Go to project directory and run:

```
docker run -it --rm -v $(pwd):/project:ro -v $(pwd)/site.conf:/etc/nginx/conf.d/default.conf:ro -p 8080:80 farazdagi/php:5.6-nginx-alpine
```

Where `site.conf` (feel free to tune as needed):

```nginx
server {
    index index.php index.html;
    listen 80 default_server;
    server_name _;
    error_log  /var/log/nginx/error.log;
    access_log /var/log/nginx/access.log;
    root /project/web;

    location ~ \.php$ {
        try_files $uri =404;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_pass 127.0.0.1:9000;
        fastcgi_index index.php;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $fastcgi_path_info;
    }
}
```

Assumption is that project directory has `web` folder where `index.php` file is located (which is conventional way to
setup modern PHP application).

## Overriding Nginx configuration

To override `nginx.conf`, pass `-v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro`:

```
docker run -it --rm 
  -v $(pwd):/project:ro -v $(pwd)/site.conf:/etc/nginx/conf.d/default.conf:ro 
  -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro
  -p 8080:80 farazdagi/php:5.6-nginx-alpine

```

## Overriding PHP configuration

To override `php.ini`, pass `-v $(pwd)/php.ini:/usr/local/etc/php/php.ini:ro`:

```
docker run -it --rm 
  -v $(pwd):/project:ro -v $(pwd)/site.conf:/etc/nginx/conf.d/default.conf:ro 
  -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro
  -v $(pwd)/php.ini:/usr/local/etc/php/php.ini:ro
  -p 8080:80 farazdagi/php:5.6-nginx-alpine

```

If you need to configure `php-fpm.conf`, it is located `/usr/local/etc/php-fpm.conf`.


## Re-use as base image

Use for any PHP based tools (as base image in your `Dockerfile`):

```
FROM farazdagi/php:5.6-nginx-alpine

// custom directives
```


