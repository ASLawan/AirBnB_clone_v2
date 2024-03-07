#!/usr/bin/python3
"""
    Module implementing file compression to
    .tar files
"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """Function that creates a tar archive file"""
    if not os.path.exists("versions"):
        local('mkdir versions')
    time = datetime.now()
    time_format = "%Y%m%d%H%M%S"
    path = 'versions/web_static_{}.tgz'.format(time.strftime(time_format))
    local('tar -cvzf {} web_static'.format(path))

    if path:
        return path
    else:
        return None
