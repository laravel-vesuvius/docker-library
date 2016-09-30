FROM php:7.1-alpine

MAINTAINER Victor Farazdagi <simple.square@gmail.com>

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer 

RUN mkdir -p /var/www
WORKDIR /var/www
VOLUME /var/www


ENTRYPOINT ["/bin/sh", "-c"]
