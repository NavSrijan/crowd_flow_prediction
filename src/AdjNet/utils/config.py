from __future__ import print_function
import os
import platform

class Config_setup(type):  # must inherit from type
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Config_setup, cls).__call__(*args, **kwargs)
        else:
            cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]

class Config(metaclass=Config_setup):
    def __init__(self, DATAPATH=None):
        if DATAPATH is None:
            DATAPATH = os.environ.get('DATAPATH')
            if DATAPATH is None:
                if platform.system() in ("Windows", "Linux"):
                    DATAPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../..', 'data')
                else:
                    print("Unsupported/Unknown OS:", platform.system(), "please set DATAPATH")
        self.DATAPATH = DATAPATH

