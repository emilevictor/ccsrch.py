from pyPdf import PdfFileWriter, PdfFileReader
from panscan import panscan
from logger import Logger
import StringIO

def plugin(fileName, data = None):
    
    if data == None:
        try:
            fd = file(fileName, "rb")
            pdf = PdfFileReader(fd)
        except Exception as e:
            Logger().log_error(e)
            return
    else:
        # handle data as a block
        # TODO test this actually works
        try:
            flo = StringIO.StringIO(data)
            pdf = PdfFileReader(flo)
        except Exception as e:
            Logger().log_error(e)
            return

    # create and zero contents string
    contents = ""

    # find how many pages input1 has:
    try:
        numPages = pdf.getNumPages()
    except Exception as e:
        Logger().log_error(e)
        return

    # iterate over all pages and extract text
    for i in range(numPages):

        # get next page from pdf and extract text as a single string        
        try:
            s = pdf.getPage(i).extractText() + "\n"
            s.encode("ascii", "ignore")
        except Exception as e:
            Logger().log_error(e)
            return
        
        # scan text for pans and return as a list
        pans = panscan(s)

        # log each pan found
        for p in pans:
            Logger().log_pan(fileName, p[1], "on page %s" % (i + 1))

    if data == None:
        fd.close()

