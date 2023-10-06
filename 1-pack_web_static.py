#!/usr/bin/python3
"""olla asta la vistar."""

from fabric.api import local
import time


def do_pack():
    """fhyv dvxsg hjkbf fdeg fvhj"""

    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
    
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
    except:
        return None
