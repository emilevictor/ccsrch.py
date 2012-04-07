from panscan import panscan
from logger import Logger

def plugin(filename, data):
    if not data:
        try:
            f = open(filename)
        except IOError as e:
            Logger().log_error(e)
            return
        try:
            data = f.read()
        except IOError as e:
            Logger().log_error(e)
        finally:
            f.close()

    results = panscan(data)
    for r in results:
        Logger().log_pan(filename, r[1], "at offset %d" % (r[0]))
