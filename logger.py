import datetime
import sys

class Logger:
    """
    The logging class. This class provides three different types of logs: PAN,
    ignore and error. See the comment for each type of log for arguments.

    This class is like a singleton so call methods on it like this:

        Logger().log_pan(...)

    """

    error_log = None
    ignore_log = None
    pan_log = None

    def __init__(self, pan_log_filename = None, error_log_filename =
                 None, ignore_log_filename = None):
        """
        The optional arguments should be given only the first time this
        constructor is called. If the name of an error log or ignore log are not
        given, they will not be enabled. The pan log filename need only be given
        if it is to deviate from the default
        """

        if not Logger.pan_log:
            if not pan_log_filename:
                Logger.pan_log = sys.stdout
            else:
                try:
                    Logger.pan_log = open(pan_log_filename, 'a')
                except IOError as e:
                    print "Cannot open PAN log for appending:", e
                    sys.exit(1)

        if error_log_filename:
            try:
                Logger.error_log = open(error_log_filename, 'a')
            except IOError as e:
                print "Cannot open error log for appending:", e
                sys.exit(1)
        if ignore_log_filename:
            try:
                Logger.ignore_log = open(ignore_log_filename, 'a')
            except IOError as e:
                print "Cannot open ignore log for appending:", e
                sys.exit(1)

    def log_error(self, e, info = ""):
        """
        Used for logging exceptions. The argument e is ideally an exception but
        doesn't have to be. Info is a string and is optional, anything given
        here will be appended to the log line.

        Logger().log_error(Exception, String)

        """

        if Logger.error_log:
            time = datetime.datetime.now().isoformat()
            Logger.error_log.write("%s Caught exception %s: %s %s\r\n" % (time,
                    type(e), e, info))

    def log_ignore(self, path, info = ""):
        """
        For logging ignored files. Info argument as for log_error

        Logger().log_ignore(String, String)

        """

        if Logger.ignore_log:
            time = datetime.datetime.now().isoformat()
            Logger.ignore_log.write("%s Ignored file %s %s\r\n" % (time, path,
                                                                   info))

    def log_pan(self, path, pan, loc, info = ""):
        """
        For logging PANs. Path should be the full location of the file,
        including paths within an archive. pan should be the snippet of text
        that contains the PAN. loc should be some string or number describing
        the location within the file. Info as for the other functions.

        Logger().log_pan(string, string, string, string)

        """

        time = datetime.datetime.now().isoformat()
        Logger.pan_log.write("%s Found PAN: %s %s in %s %s\r\n" %
                             (time, pan, loc, path, info))

