FROM php:7.0-alpine


MAINTAINER Victor Farazdagi <simple.square@gmail.com>

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer 

RUN mkdir -p /project
WORKDIR /project
VOLUME /project


ENTRYPOINT ["/bin/sh", "-c"]
