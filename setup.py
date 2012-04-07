from distutils.core import setup
import py2exe

setup(console=['ccsrch.py'],
      scripts=['txt.py', 'pdf.py', 'ods.py', 'odt.py', 'xls.py',
               'xlsx.py', 'zip.py', 'tar.py'])
