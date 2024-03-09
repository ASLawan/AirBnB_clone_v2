#!/usr/bin/python3
"""
    Module implementing distributon of archive
    files to servers using Fabric
"""
from fabric.api import env, put, run, local
from os.path import exists
from datetime import datetime


env.hosts = ['54.236.24.199', '34.207.212.193']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """ Function that distributes archived files to servers with Fabric"""
    if not exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        archive_filename = archive_path.split("/")[-1]
        filename = archive_filename.split(".")[0]
        release_dir = "/data/web_static/releases/{}".format(filename)
        run("mkdir -p {}".format(release_dir))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_dir))

        run("rm /tmp/{}".format(archive_filename))
        run("rm -f /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_dir))
        print("New version deployed")
        return True
    except Exception as e:
        print(e)
        return False

