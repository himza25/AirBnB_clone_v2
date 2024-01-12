#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives.
"""

from fabric.api import local, sudo, env

env.hosts = ['3.85.168.165', '100.24.72.68']
env.user = "ubuntu"

def do_clean(number=0):
    """
    Deletes out-of-date archives.
    """
    number = int(number)

    if number == 0:
        number = 1

    # Delete local archives
    local("ls -tr versions/web_static_*.tgz | head -n -{} | xargs rm -f".format(number))

    # Delete remote archives
    sudo("ls -tr /data/web_static/releases/web_static_* | head -n -{} | xargs rm -rf".format(number))

if __name__ == "__main__":
    do_clean()
