#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers.
"""

from fabric.api import local, put, sudo, env
from os.path import exists, isdir
from datetime import datetime
import os

env.hosts = ['3.85.168.165', '100.24.72.68']
env.user = "ubuntu"


def do_pack():
    """
    Generates a .tgz archive from the contents of the 'web_static' folder.
    """
    try:
        if not isdir("versions"):
            local("mkdir versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        print("An error occurred: {}".format(e))
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    """
    if not exists(archive_path):
        return False

    try:
        file_name = os.path.basename(archive_path)
        name_no_ext = file_name.split(".")[0]
        remote_tmp_path = "/tmp/{}".format(file_name)
        remote_release_folder = "/data/web_static/releases/{}/".format(
            name_no_ext)

        put(archive_path, remote_tmp_path)
        sudo("mkdir -p {}".format(remote_release_folder))
        sudo("tar -xzf {} -C {}".format(remote_tmp_path,
                                        remote_release_folder))
        sudo("rm {}".format(remote_tmp_path))
        sudo("mv {}web_static/* {}".format(remote_release_folder,
                                           remote_release_folder))
        sudo("rm -rf {}web_static".format(remote_release_folder))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {} /data/web_static/current".format(remote_release_folder))

        return True
    except Exception as e:
        print("An error occurred: {}".format(e))
        return False


def deploy():
    """
    Creates and distributes an archive to the web servers.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


if __name__ == "__main__":
    deploy()
