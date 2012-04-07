import zipfile
#import all of the other modules for text reading.
from logger import Logger
import scan
import StringIO

def plugin(filename, data=None):
    """Takes as input the file path to a zip file
        returns an array of pairs giving "internal" file path
        and text to be scanned"""
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
    else:
        try:
                file = zipfile.ZipFile(filename, "r")
        except (zipfile.BadZipfile, zipfile.LargeZipFile) as e:
                Logger().log_error(e)
                return

    for name in file.namelist():
        #Read the contents of each file.
        innerFile = file.read(name)
        if not innerFile:
            continue
        #Now call the scanner with the "fake" path and data read from the inner
        #file.
        scan.Scanner().scan(filename + "/" + name, innerFile);

        #data = file.read(file)
        #Check whether file is a readable type
            #xls, txt, pdf, oO, xlsx, doc, docx
            #Use other modules to read the text out of each.
            #once text is read, put it into a pair with the "inside" filename

    #once all files are completed, return the pairs in an array.
