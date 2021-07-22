# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 10:16:31 2021

@author: ca273
"""

# Import dependency to load csv data 
import pandas as pd
# Import dependency to load location of current directory
import os

# Get the current working directory and convert it into a iterable
path = os.getcwd()
dirs = os.listdir(path)

# Empty list to store the name of csv fiels
CSV_Files = []

# Find all the csv files
for file in dirs:
    if '.csv' in file.lower():
        CSV_Files.append(file)
    
# Empty List to store the name of html files
HTML_Name = []

# Create names for HTML Files to be created 
for filename in CSV_Files:
    HTML_Name.append(filename[:-4]+".html")
    
# List all the files in the directory
for num in range(len(CSV_Files)):
    print("%d. - %s" % (num, CSV_Files[num]))

# Choosing a file
File_Number = int(input("Please choose a file number from the above list: "))

# Open a blank html file
file = open(HTML_Name[File_Number],"w")

# Load a extracted csv file with interactive elements
df = pd.read_csv(CSV_Files[File_Number])
# Load the linked history as a dataframe
History = pd.read_csv("Linked History.csv")

# Write general HTML syntax
file.write("<!DOCTYPE html>\n")
file.write("<html>\n")
file.write("<head>\n")
file.write("<title>Sample Form</title>\n")
file.write("<style> body {width: 580px;}\n")
file.write("</style>")
file.write("</head>\n")
file.write("<body>\n")
file.write("<table width=" + str(580) + ">\n")
file.write("<tbody>\n")
file.write("<tr>\n")

# Choosing number of elements 
Threshold = int(input("Enter the number of fields in a row: "))
# Flag for elements in a row
Row_Elements = 0

# Traverse the dataframe row by row
for row in range(len(df)):
    
    # If the object is empty text blank 
    if df.loc[row, "ObjectType"] == "text fillup":
        # Increment the row elements 
        Row_Elements += 1 
        
        # Check if the threshold is met 
        if Row_Elements <= 3:
            
            # Extract the filed name
            Test_String = str(df.loc[row, 'Name'])
            Test_String = Test_String.upper()
            
            # Split the name of the string into words
            Chunks = Test_String.split(' ')
            Chunks2 = Test_String.lower().split(' ')
            
            # empty sections for labels and appending in the dictonary
            label = ''
            AddToHistory = []
            
            # Traverse the history to check for field name
            for row1 in range(len(History)):
                
                # Check for the filed name 
                if History.loc[row1, "Label Name"].lower() == Test_String.lower():
                    
                    # If the database name is not none
                    if History.loc[row1, "Database Name"] != 'NONE':
                       
                        # It's the new label
                        label = History.loc[row1, "Database Name"]
            
            # Making the name and ID for form 
            if len(Chunks) > 1:
                # Name and ID with quirks 
                name_block = '_'.join(Chunks)
                
                # if label is None or empty 
                if label == 'NONE' or label == '':
                    label = name_block
            else:
                # Name and ID with quirks 
                name_block = Chunks[0]
                
                # if label is None or empty
                if label == 'NONE' or label == '':
                    label = name_block
                    
            # Making the name and ID for form         
            if len(Chunks2) > 1:
                
                # Name and ID with quirks 
                name_block2 = '&#32;'.join(Chunks2)
                # Name and ID with quirks 
                name_block2 = name_block2 + "_1"
            else:
                # Name and ID with quirks 
                name_block2 = Chunks2[0]
                # Name and ID with quirks 
                name_block2 = name_block2 + "_1"
             
            # Storing the HTML script 
            text = '<td>'+'<p>' + str(df.loc[row, 'Name']) + ' <input id="' + name_block2 + '" name="' + name_block + '" value="[*' + label + '*]"' + ' type="text" />' + '</p>' +'</td>'+' \n'
        
        else:
            # Rest the row elements 
            Row_Elements = 0
            
            # Extract the filed name
            Test_String = str(df.loc[row, 'Name'])
            Test_String = Test_String.upper()
            
            # Split the name of the string into words
            Chunks = Test_String.split(' ')
            Chunks2 = Test_String.lower().split(' ')
            
            # empty sections for labels and appending in the dictonary
            label = ''
            AddToHistory = []
            
            # Traverse the history to check for field name
            for row1 in range(len(History)):
                
                # Check for the filed name 
                if History.loc[row1, "Label Name"].lower() == Test_String.lower():
                    
                    # If the database name is not none
                    if History.loc[row1, "Database Name"] != 'NONE':
                       
                        # It's the new label
                        label = History.loc[row1, "Database Name"]
            
            # Making the name and ID for form
            if len(Chunks) > 1:
                # Name and ID with quirks 
                name_block = '_'.join(Chunks)
                
                # if label is None or empty
                if label == 'NONE' or label == '':
                    label = name_block
            else:
                # Name and ID with quirks
                name_block = Chunks[0]
                
                # if label is None or empty
                if label == 'NONE' or label == '':
                    label = name_block
                    
            if len(Chunks2) > 1:
                # Name and ID with quirks 
                name_block2 = '&#32;'.join(Chunks2)
                # Name and ID with quirks 
                name_block2 = name_block2 + "_1"
            
            else:
                # Name and ID with quirks 
                name_block2 = Chunks2[0]
                # Name and ID with quirks 
                name_block2 = name_block2 + "_1"
                
            # Write general HTML syntax
            file.write("</tr>\n")
            file.write("<tr>\n")
                
            # Storing the HTML script 
            text = '<td>'+'<p>' + str(df.loc[row, 'Name']) + ' <input id="' + name_block2 + '" name="' + name_block + '" value="[*' + label + '*]"' + ' type="text" />' + '</p>' +'</td>'+' \n'
        
        # Write general HTML syntax
        file.write(text)
    
    if df.loc[row, "ObjectType"] == "checkbox":
        # Increment the row elements
        Row_Elements += 1
        
        # Check if the threshold is met 
        if Row_Elements <= 3:
            
            # Extract the filed name
            Test_String = str(df.loc[row, 'Name'])
            Test_String = Test_String.upper()
            
            # Split the name of the string into words
            Chunks = Test_String.split(' ')
            Chunks2 = Test_String.lower().split(' ')
            
            # Making the name and ID for form 
            if len(Chunks) > 1:
                # Name and ID with quirks
                name_block = '_'.join(Chunks)
            else:
                # Name and ID with quirks
                name_block = Chunks[0]
            
            
            if len(Chunks2) > 1:
                # Name and ID with quirks
                name_block2 = '&#32;'.join(Chunks2)
                name_block2 = name_block2 + "_1"
            else:
                # Name and ID with quirks
                name_block2 = Chunks2[0]
                name_block2 = name_block2 + "_1"
            
            # Storing the HTML script 
            text = '<td>'+'<p>' + str(df.loc[row, 'Name']) + ' <input id="' + name_block2 + '" name="' + name_block + '" value="yes"' + ' type="checkbox" />' + '</p>' +'</td>'+' \n'
        
        else:
            # Rest the row elements 
            Row_Elements = 0
            
            # Extract the filed name
            Test_String = str(df.loc[row, 'Name'])
            Test_String = Test_String.upper()
            
            # Split the name of the string into words
            Chunks = Test_String.split(' ')
            Chunks2 = Test_String.lower().split(' ')
            
            # Making the name and ID for form
            if len(Chunks) > 1:
                # Name and ID with quirks
                name_block = '_'.join(Chunks)
            else:
                # Name and ID with quirks
                name_block = Chunks[0]
            
            if len(Chunks2) > 1:
                # Name and ID with quirks
                name_block2 = '&#32;'.join(Chunks2)
                name_block2 = name_block2 + "_1"
            else:
                # Name and ID with quirks
                name_block2 = Chunks2[0]   
                name_block2 = name_block2 + "_1"
            
            # Write general HTML syntax
            file.write("</tr>\n")
            file.write("<tr>\n")
            
            # Storing the HTML script 
            text = '<td>'+'<p>' + str(df.loc[row, 'Name']) + ' <input id="' + name_block2 + '" name="' + name_block + '" value="yes"' + ' type="checkbox" />' + '</p>' +'</td>'+' \n'
        
        # Write general HTML syntax
        file.write(text)

# Write general HTML syntax
file.write("</tr>\n")
file.write("</tbody>\n")
file.write("</table>\n")
file.write("</body>\n")
file.write("</html>\n")

# CLose the file
file.close()