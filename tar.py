import tarfile
from logger import Logger
import scan
import StringIO

def plugin(filename, data=None):
        if data is not None:
                try:
                        #filelikeObj = StringIO.StringIO(data)
                        filelikeObj = StringIO.StringIO(data)
                        tar = tarfile.open(fileobj=filelikeObj)
                except tarfile.TarError as e:
                        Logger().log_error(e)
                        return
        else:
                try:
                        tar = tarfile.open(filename)
                except tarfile.TarError as e:
                        Logger().log_error(e)
                        return
        """ For each file in the tarball, run it through the scanner """
        for file in tar.getmembers():
                innerFile = tar.extractfile(file)
                if not innerFile:
                        continue
                try:
                        innerFileContent = innerFile.read()
                except tarfile.TarError as e:
                        Logger().log_error(e)
                        continue
                if not innerFileContent:
                        continue
                scan.Scanner().scan(filename + "/" + file.name, innerFileContent)

        tar.close()
