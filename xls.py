import xlrd # Import the packages
import scan
import panscan
import logger
import StringIO

def plugin(filename, data = None):
    if data is not None:
        
        book = xlrd.open_workbook(filename, file_contents=data)

    else:
        book = xlrd.open_workbook(filename) # Open an .xls file
        
    #iterate over sheets
    for i in range (len(book.sheet_names())):
        sheet = book.sheet_by_index(i)
        for rownum in range(sheet.nrows) :
            for column in range(len(sheet.row_values(rownum))):
                # scan text for pans and return as a list
                pans = panscan.panscan(" " +
                unicode(sheet.row_values(rownum)[column]) + " ")

                # log each pan found
                for p in pans:
			        logger.Logger().log_pan(filename, p[1], 
                        "in sheet %s, in cell %s:%d" % 
                        (book.sheet_names()[i], intToChar(column),  rownum))    
			         
def intToChar(integer):
    """A really lazy way to convert the ints to chars. will return the column name according to the int provided"""
    temp = integer/26 +1
    character = integer%26
    character+=65    
    return chr(character)*temp
    
#plugin("/home/d/Dropbox/Uni/3000/ccsrch/testFiles/1 Excel.xls")
