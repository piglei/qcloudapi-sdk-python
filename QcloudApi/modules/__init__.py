# -*- coding: utf-8 -*-
from .base import Base

_GLOBAL_MODULES = {}


def register_module(name, host, path):
    """Register a new module to current modules

    :param name: module name, such as "dcdb"
    :param host: request host
    :param path: request path
    """
    mclass = type("DynamicModule_%s" % name, (Base, ), {
        "requestHost": host,
        "requestUri": path
    })
    _GLOBAL_MODULES[name] = mclass


def find_module_by_name(name):
    """Find a dynamic module by given module name

    :param name: module name
    :returns: a DynamicModule class or None if no module named `name` is found
    """
    return _GLOBAL_MODULES.get(name, None)


# Register current default modules
# DCDB documentation: https://cloud.tencent.com/document/product/557/16123
register_module("dcdb", "dcdb.tencentcloudapi.com", "/")
