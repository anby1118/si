"""
@file:   enums
@author: linuxzhen520@163.com
@date:   2020/07/18
@desc:
"""

import enum

class AssetType(enum.Enum):
    SERVER = 1
    NETWORK = 2


class StatusType(enum.Enum):
    INIT = 0
    ONLINE = 1
    OFFLINE = 2
    UNREACHABLE = 3
    MAINTAIN = 4

class DiskIfaceType(enum.Enum):
    pass

class MethodType(enum.Enum):
    GET = 1
    POST = 2
    DELETE = 3
    PUT = 4
    PATH = 5