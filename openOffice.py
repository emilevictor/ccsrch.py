import logger
import zipfile
import StringIO
import panscan

def parse(filename, fileType, data = None):
    """
    This will open the file, and then will proceed to parse myFile: String
    containing the path of the file to parse fileType:  just the extension of
    the file. I would parse it myself, but the caller will already know this"""
    try:
        if data:
            
            filelikeObj = StringIO.StringIO(data)
            myfile = zipfile.ZipFile(filelikeObj, "r", zipfile.ZIP_DEFLATED)

        else:
            myfile = zipfile.ZipFile(filename,'r', zipfile.ZIP_DEFLATED)
    except zipfile.BadZipfile:
        logger.Logger().log_ignore(filename, "Bad zip file")
        return
    
    xmldata = myfile.read("content.xml")
    myfile.close()
    pans = panscan.panscan(xmldata)
    for p in pans:
        logger.Logger().log_pan(filename, p[1], "at offset %d" % p[0])

