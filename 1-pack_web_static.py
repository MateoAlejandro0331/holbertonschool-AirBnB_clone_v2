#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
    from the contents of the web_static"""
from fabric.api import local
from os.path import isdir
import time


def do_pack():
    """Funtion to generates the file"""

    if isdir('versions') is False:
        local("mkdir versions")
    file = "web_static_" + time.strftime("%Y%m%d%H%M%S", time.gmtime())\
        + ".tgz"
    result = local("tar -cvzf versions/{} web_static ".format(file))
    if result.failed:
        return None
    return "versions/web_static_" +\
        time.strftime("%Y%m%d%H%M%S", time.gmtime())\
        + ".tgz"
