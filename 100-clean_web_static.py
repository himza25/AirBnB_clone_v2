#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
import os
from fabric.api import *

env.hosts = ["3.85.168.165", "100.24.72.68"]


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    # Clean local archives
    local_archives = sorted(os.listdir("versions"))
    local_archives = [a for a in local_archives if "web_static_" in a]
    archives_to_delete = local_archives[:-number]

    with lcd("versions"):
        for archive in archives_to_delete:
            local("rm ./{}".format(archive))

    # Clean archives on remote servers
    with cd("/data/web_static/releases"):
        remote_archives = run("ls -tr").split()
        remote_archives = [a for a in remote_archives if "web_static_" in a]
        remote_archives_to_delete = remote_archives[:-number]

        for archive in remote_archives_to_delete:
            run("rm -rf ./{}".format(archive))
