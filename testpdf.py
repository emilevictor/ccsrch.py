import os
from pdf import scanPdf

for filename in os.listdir("testFiles/PDF"):
	scanPdf("testFiles/PDF/" + filename)

