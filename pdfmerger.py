from PyPDF2 import PdfMerger
import os
#Create and instance of PdfFileMerger() class
merger = PdfMerger()
#Create a list with PDF file names
# path_name = str(input(enter your folder path))
path_to_files = r'pdf_files/'
#Get the file names in the directory
for root, dirs, file_names in os.walk(path_to_files):
    #Iterate over the list of file names
    for file_name in file_names:
        #Append PDF files
        merger.append(path_to_files + file_name)
#Write out the merged PDF
merger.write("result.pdf")
merger.close()