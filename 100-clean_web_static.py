#!/usr/bin/python3
""" Function that clens archive files """
from fabric.api import *


env.hosts = ['54.236.24.199', '34.207.212.193']
env.user = "ubuntu"


def do_clean(number=0):
    """ deletes unnecessary archive files"""

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
