#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import os
from contextlib import contextmanager

# define images to build
images = {
    'php:7.0-alpine': {
        'path': 'php/7.0-alpine',
        'aliases': ['php:alpine', 'php:latest']
    },
}

# process aliases
aliases = {}
for tag, image in images.iteritems():
    if 'aliases' in image:
        base_image = image.copy()
        del (base_image['aliases'])
        for alias in image['aliases']:
            aliases[alias] = base_image
            aliases[alias]['tag'] = tag


def run(cmd):
    click.secho(cmd, fg='blue')
    os.system(cmd)


def error(err):
    click.echo('[' + click.style('ERROR', fg='red') + '] ' + err)


@click.group()
def cli():
    pass


@cli.command(name='build')
@click.argument('tag', required=False)
def build_php(tag):
    """Build docker images images"""

    tags = []
    if tag is None:  # build all
        for tag in images:
            tags.append(tag)
    else:
        tags.append(tag)

    for tag in tags:
        docker_build(tag)


def docker_push(tag):
    run('docker push slabs/{}'.format(tag))


def docker_build(tag):
    if tag in aliases:
        tag = aliases[tag]['tag']  # use referenced image's tag
    if tag not in images:
        return error("invalid tag: " + tag)

    click.secho('----- ' + tag + ' -----', fg='green')

    path = images[tag]['path']
    with cd(path):
        run('docker build -t slabs/{} .'.format(tag))
        docker_push(tag)
        if 'aliases' in images[tag]:
            for alias in images[tag]['aliases']:
                run('docker tag slabs/{} slabs/{}'.format(aliases[alias]['tag'], alias))
                docker_push(alias)


@cli.command(name='list:php')
def list_php():
    """List buildable PHP images"""

    for tag in images['php']:
        click.echo('- ' + tag)


@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    click.secho('cd ' + newdir, fg='blue')
    try:
        yield
    finally:
        os.chdir(prevdir)


if __name__ == "__main__":
    cli()
