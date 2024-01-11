#!/usr/bin/python3
"""Compress web static package."""
from fabric.api import *
from os import path

env.hosts = ['3.85.168.165', '100.24.72.68']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Deploy web files to server."""
    try:
        if not path.exists(archive_path):
            return False

        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        dest_path = f"/data/web_static/releases/{base_name}/"

        # Upload archive and create target directory
        put(archive_path, f"/tmp/{file_name}")
        run(f"sudo mkdir -p {dest_path}")

        # Uncompress archive and delete .tgz
        run(f"sudo tar -xzf /tmp/{file_name} -C {dest_path}")
        run(f"sudo rm /tmp/{file_name}")

        # Move contents and remove extraneous directory
        run(f"sudo mv {dest_path}web_static/* {dest_path}")
        run(f"sudo rm -rf {dest_path}web_static")

        # Handle symbolic link
        run("sudo rm -rf /data/web_static/current")
        run(f"sudo ln -s {dest_path} /data/web_static/current")
    except Exception as e:
        print(e)  # Optionally, log the exception
        return False

    return True
