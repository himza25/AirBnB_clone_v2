#!/usr/bin/python3
from fabric.api import put, run, env
from os.path import exists

env.hosts = ['3.85.168.165', '100.24.72.68']


def do_deploy(archive_path):
    """Distributes an archive to web servers."""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        folder_name = f"/data/web_static/releases/{base_name}/"

        put(archive_path, f"/tmp/{file_name}")
        run("mkdir -p " + folder_name)
        run(f"tar -xzf /tmp/{file_name} -C {folder_name}")
        run(f"rm /tmp/{file_name}")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {folder_name} /data/web_static/current")

        print("New version deployed!")
        return True
    except Exception as e:
        return False
