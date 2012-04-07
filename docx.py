#################################################
#                                               #
#         Requires lxml to be installed         #
#                                               #    
#      Credit to 'gtozzi' for some code at      #
#  https://github.com/mikemaccana/python-docx   #
#                                               #
#################################################

import zipfile
from logger import Logger
from scan import Scanner
import panscan
from lxml import etree

nsprefixes = {
    # Text Content
    'mv':'urn:schemas-microsoft-com:mac:vml',
    'mo':'http://schemas.microsoft.com/office/mac/office/2008/main',
    've':'http://schemas.openxmlformats.org/markup-compatibility/2006',
    'o':'urn:schemas-microsoft-com:office:office',
    'r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'm':'http://schemas.openxmlformats.org/officeDocument/2006/math',
    'v':'urn:schemas-microsoft-com:vml',
    'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'w10':'urn:schemas-microsoft-com:office:word',
    'wne':'http://schemas.microsoft.com/office/word/2006/wordml',
    # Drawing
    'wp':'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
    'a':'http://schemas.openxmlformats.org/drawingml/2006/main',
    'pic':'http://schemas.openxmlformats.org/drawingml/2006/picture',
    # Properties (core and extended)
    'cp':"http://schemas.openxmlformats.org/package/2006/metadata/core-properties",
    'dc':"http://purl.org/dc/elements/1.1/",
    'dcterms':"http://purl.org/dc/terms/",
    'dcmitype':"http://purl.org/dc/dcmitype/",
    'xsi':"http://www.w3.org/2001/XMLSchema-instance",
    'ep':'http://schemas.openxmlformats.org/officeDocument/2006/extended-properties',
    # Content Types (we're just making up our own namespaces here to save time)
    'ct':'http://schemas.openxmlformats.org/package/2006/content-types',
    # Package Relationships (we're just making up our own namespaces here to save time)
    'pr':'http://schemas.openxmlformats.org/package/2006/relationships'
}


def plugin(file, data=None):
    if data is not None:
        try:
                filelikeObj = StringIO.StringIO(data)
        except Exception as e:
        	Logger().log_error(e)
                return

        try:
                mydoc = zipfile.ZipFile(filelikeObj)
        except zipfile.BadZipfile as e:
                Logger().log_error(e)
                return
    else:
        try:
                mydoc = zipfile.ZipFile(file)
        except (zipfile.BadZipfile, zipfile.LargeZipFile) as e:
                Logger().log_error(e)
                return

    try:                
        xmlcontent = mydoc.read('word/document.xml')
    except IOError as e:
        Logger().log_error(e)
        return
    try:
        document = etree.fromstring(xmlcontent)
    except Exception as e:
        Logger().log_error(e)
        return

    # Create a list of paragraphs
    paratextlist=[]
    paralist = []
    for element in document.iter():
        if element.tag == '{'+nsprefixes['w']+'}p':
            paralist.append(element)
    for para in paralist:
        paratext=u''
        for element in para.iter():
            if element.tag == '{'+nsprefixes['w']+'}t':
                if element.text:
                    paratext = paratext+element.text
        if not len(paratext) == 0:

            paratextlist.append(paratext)

    # Scan and log
    paraNum = 1
    for i in paratextlist:
        pans = panscan.panscan(i)
        for p in pans:
            logger.Logger().log_pan(file, p, "Paragraph number " + i +".")
        paraNum += 1


    
