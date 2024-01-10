#!/usr/bin/python3
from fabric.api import put, run, env
from os.path import exists

env.hosts = ['3.85.168.165', '100.24.72.68']
env.user = "ubuntu"

def do_deploy(archive_path):
    """Distributes an archive to web servers."""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        folder_name = f"/data/web_static/releases/{base_name}/"

        # Upload the archive to the /tmp/ directory
        put(archive_path, f"/tmp/{file_name}")

        # Uncompress the archive to the folder on the web server
        run(f"mkdir -p {folder_name}")
        run(f"tar -xzf /tmp/{file_name} -C {folder_name}")

        # Delete the archive from the web server
        run(f"rm /tmp/{file_name}")

        # Move contents out of the 'web_static' subfolder
        run(f"mv {folder_name}web_static/* {folder_name}")

        # Delete the web_static subfolder
        run(f"rm -rf {folder_name}web_static")

        # Delete the symbolic link and create a new one
        run("rm -rf /data/web_static/current")
        run(f"ln -s {folder_name} /data/web_static/current")

        print("New version deployed!")
        return True
    except Exception as e:
        return False
