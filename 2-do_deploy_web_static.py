#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers.
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['3.85.168.165', '100.24.72.68']


def do_deploy(archive_path):
    """ Distributes an archive to the web servers. """
    if not exists(archive_path):
        print("Archive path does not exist")
        return False

    try:
        file_name = archive_path.split("/")[-1]
        name_no_ext = file_name.split(".")[0]
        remote_tmp_path = "/tmp/{}".format(file_name)
        remote_release_folder = "/data/web_static/releases/{}/".format(name_no_ext)

        # Upload the archive
        print("Uploading the archive...")
        put(archive_path, remote_tmp_path)
        print("Archive uploaded.")

        # Operations on the server
        print("Creating release directory...")
        run("mkdir -p {}".format(remote_release_folder))
        print("Release directory created.")

        print("Uncompressing the archive...")
        run("tar -xzf {} -C {}".format(remote_tmp_path, remote_release_folder))
        print("Archive uncompressed.")

        print("Moving content out of web_static directory...")
        run("mv {}web_static/* {}".format(remote_release_folder, remote_release_folder))
        print("Content moved.")

        print("Cleaning up...")
        run("rm -rf {}web_static".format(remote_release_folder))
        run("rm {}".format(remote_tmp_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(remote_release_folder))
        print("New version deployed.")

        return True
    except Exception as e:
        print(e)
        return False
