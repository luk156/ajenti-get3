__author__ = 'matteo'

from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='GeT3',
    icon=None,
    dependencies=[
        PluginDependency('main'),
    ],
)


def init():
    import main