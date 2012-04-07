from logger import Logger
from scan import Scanner
import panscan
import sys
import zipfile

def plugin(filename, data=None):
    if data is not None:
        try:
            filelikeObj = StringIO.StringIO(data)
        except Exception as e:
            Logger().log_error(e)
            return

        try:
            file = zipfile.ZipFile(filelikeObj, "r")
        except zipfile.BadZipfile as e:
            Logger().log_error(e)
            return

        try:
            f = open(file)
        except Exception as e:
            Logger().log_error(e)
            return
    else:
        try:
            f = open(filename)
        except Exception as e:
            Logger().log_error(e)
            return


    out = ""

    for c in f.read():
        if ord(c) >= 32 and ord(c) < 127:
            out += c
        elif ord(c) == 10 or ord(c) == 13:
            out += "\n"
        else:
            out += " "
    f.close()

    results = panscan(out)
    for r in results:
        Logger().log_pan(filename, r[1], "")
    
