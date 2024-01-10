#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
import os


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
