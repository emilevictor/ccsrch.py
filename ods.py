import openOffice
def plugin(filename, data=None):
    openOffice.parse(filename, "ods", data)

#plugin('/home/d/Dropbox/Uni/3000/ccsrch/testFiles/4 Excel.ods')
