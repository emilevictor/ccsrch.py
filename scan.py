from pluginmap import plugins
from panscan import panscan
from logger import Logger
import mimetypes

class Scanner:
    """
    Scanner of files. Works out the appropriate plugin to call based on the
    associations in pluginmap.py and call that plugin with filename and
    data given to scan.

    This class is like a singleton so use it like this:
        Scanner().scan(filename, data)
    """
    plugin_fns = {}

    def __init__(self):
        if not Scanner.plugin_fns:
            Scanner.plugin_fns = plugins

    def scan(self, filename, data=None):
        plugin = Scanner.plugin_fns.get(filename.split('.')[-1])
        if plugin:
            return plugin(filename, data)

        mime = mimetypes.guess_type(filename)
        if mime[0] and mime[0].startswith('text'):
            return Scanner.plugin_fns['txt'](filename, data)
        else:
            Logger().log_ignore(filename, "Unrecognised binary file")
