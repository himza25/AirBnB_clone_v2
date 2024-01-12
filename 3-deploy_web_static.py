#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers.
"""

from fabric.api import *
from datetime import datetime
import os

env.hosts = ['3.85.168.165', '100.24.72.68']


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(date_time)

    if not os.path.exists("versions"):
        os.mkdir("versions")

    try:
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception as e:
        return None

def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    if not os.path.exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        name_no_ext = file_name.split(".")[0]

        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(name_no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file_name, name_no_ext))
        run("rm /tmp/{}".format(file_name))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name_no_ext, name_no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name_no_ext))

        print("New version deployed!")
        return True
    except:
        return False

def deploy():
    """Creates and distributes an archive to web servers."""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
