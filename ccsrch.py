from os.path import walk, join, isfile, abspath
import subprocess
import sys
from scan import Scanner
from logger import Logger
from optparse import OptionParser

def visitor(arg, dirname, names):
    for name in names:
        fullpath = abspath(join(dirname, name))
        if fullpath == arg:
            continue
        elif(isfile(join(dirname, name))):
            Scanner().scan(join(dirname, name))


if __name__ == "__main__":
    parser = OptionParser(usage="usage: %prog [options] path")
    parser.add_option("-p", "--pan-log", dest="pan_log_filename", 
                      help="write PANs to this file, default is stdout",
                      default=None)
    parser.add_option("-e", "--error-log", dest="error_log_filename",
                       help="write error log to this file, off by default",
                       default=None)
    parser.add_option("-i", "--ignore-log", dest="ignore_log_filename",
                      help="write ignore log to this file, off by default",
                      default=None)
    (options, args) = parser.parse_args()

    Logger(options.pan_log_filename, options.error_log_filename,
            options.ignore_log_filename)

    if args and args[0]:
        path = args[0]
    else:
        path = "."

    if options.pan_log_filename:
        walk(path, visitor, abspath(options.pan_log_filename))
    else:
        walk(path, visitor, "")
