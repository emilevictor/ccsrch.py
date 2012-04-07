import xlsx
import xls
import pdf
import zip
import tar
import txt
import ods
import odt

plugins = \
    {
        'pdf': pdf.plugin,
        'xls': xls.plugin,
        'xlsx': xlsx.plugin,
        'zip': zip.plugin,
        'odt': odt.plugin,
        'ods': ods.plugin,
        #'doc': 'doc',
        #'docx': 'docx',
        'txt': txt.plugin,
        'tar': tar.plugin,
        'tar.gz': tar.plugin,
        'tgz' : tar.plugin,
        'tar.bz2' : tar.plugin

    }

