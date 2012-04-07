import openOffice
def plugin(filename, data=None):
    openOffice.parse(filename, "odt",data)
