FROM php:5.6-fpm-alpine

MAINTAINER Vadim Serdunich <symphonyviolist51@gmail.com>

ADD php.ini /usr/local/etc/php/conf.d/

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer 

# Install PHP extensions
RUN set -ex && \
## Install pgsql
apk --no-cache add postgresql-dev && \
docker-php-ext-install pdo pdo_pgsql pgsql && \
## Install gd
apk add --no-cache freetype libpng libjpeg-turbo freetype-dev libpng-dev libjpeg-turbo-dev && \
docker-php-ext-configure gd \
    --with-gd \
    --with-freetype-dir=/usr/include/ \
    --with-png-dir=/usr/include/ \
    --with-jpeg-dir=/usr/include/ && \
docker-php-ext-install gd && \
## Install mcrypt
apk add --no-cache libmcrypt-dev && \
docker-php-ext-configure mcrypt  --with-mcrypt && \
docker-php-ext-install mcrypt && \
## Install redis extension
apk add --no-cache autoconf g++ make && \
pecl install redis-2.2.4 && \
docker-php-ext-enable redis

RUN apk add --update --no-cache grep

RUN mkdir -p /var/www

ENV USER=php-fpm
ENV USER_ID=${USER_ID:-1000}
RUN addgroup -g $USER_ID $USER && \
adduser -D -u $USER_ID -G $USER $USER

USER $USER

WORKDIR /var/www
