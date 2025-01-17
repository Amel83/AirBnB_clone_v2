#!/usr/bin/python3
"""tring to do thi project ervers"""

import time
import os.path
from fabric.api import local
from fabric.operations import env, put, run

env.hosts = ['44.210.150.159', '35.173.47.15']


def do_pack():
    """Gg who talks too mgfds b_static folder"""

    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
    
    except:
        return None


def do_deploy(archive_path):
    """serversa are the best  to web servers"""
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        file = archive_path.split("/")[-1]
        folder = ("/data/web_static/releases/" + file.split(".")[0])
        
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(file, folder))
        run("rm /tmp/{}".format(file))
        run("mv {}/web_static/* {}/".format(folder, folder))
        run("rm -rf {}/web_static".format(folder))
        run('rm -rf /data/web_static/current')
        run("ln -s {} /data/web_static/current".format(folder))
        
        print("Deployment done")
        return True
    except:
        return False


def deploy():
    """gsdcj fgjnm rgs dv  web servers"""
    
    try:
        path = do_pack()
        return do_deploy(path)
    except:
    
        return False
