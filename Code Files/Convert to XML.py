# Iport dependency to load pdf files
import pdfquery

# Import dependency to load location of current directory
import os

# Get the current working directory and convert it into a iterable
path = os.getcwd()
dirs = os.listdir(path)

# Empty list to store the name of PDF file name
PDF_Files = []

# Find all the pdf files
for file in dirs:
    if '.pdf' in file.lower():
        PDF_Files.append(file)

# Empty List to store the name of xml files
XML_Name = []

# Create names for HTML Files to be created 
for filename in PDF_Files:
    XML_Name.append(filename[:-4]+".xml")
    
# List all the files in the directory
for num in range(len(PDF_Files)):
    print("%d. - %s" % (num,PDF_Files[num]))

# Choosing a file
File_Number = int(input("Please choose a file number from the above list: "))

# Loading the chosen pdf 
pdf = pdfquery.PDFQuery(PDF_Files[File_Number])
pdf.load()

# Convert file into internal tree to traverse
pdf.tree

# Convert the tree to xml to read elements
pdf.tree.write(XML_Name[File_Number], pretty_print=True, encoding="utf-8")
