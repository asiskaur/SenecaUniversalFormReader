# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 11:37:37 2021

@author: ca273
"""

# Import dependency to load csv data  
import pandas as pd
# Import dependency to update the linked history
from csv import writer
# Import dependency to load location of current directory
import os
# Import library to manipulate text strings
import string

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
History = pd.read_csv("Linked History.csv")
Label_Filename = CSV_Files[File_Number]
Label_Filename = Label_Filename[:-4]+"_WithText_Labels.csv"
Labels = pd.read_csv(Label_Filename)
                                    
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
        # To Check if label was found or not 
        Label_check = 0
        
        # Check if the threshold is met 
        if Row_Elements < Threshold:
            
            # Extract the filed name
            Test_String = str(df.loc[row, 'Name'])
            
            # Split the name of the string into words
            Chunks = Test_String.upper().split(' ')
            Chunks2 = Test_String.lower().split(' ')
            
            # empty sections for labels and appending in the dictonary
            label = ''
            AddToHistory = []
            
            # Traverse the history to check for field name
            for row1 in range(len(History)):
                
                # Check for the filed name 
                if History.loc[row1, "Label Name"].lower() == Test_String.lower():
                    
                    # If the database name is not none
                    if History.loc[row1, "Database Name"].lower() != 'none':
                       
                        # It's the new label
                        label = History.loc[row1, "Database Name"]
                    
                    else:
                        label = "NONE"
            
            # if the label is still empty, which means it is not found in history
            if label == '':
                # store new label
                list_of_elem = []
                
                print("The field name is: %s" % Test_String.lower())
                
                list_of_elem.append(Test_String.lower())
                list_of_elem.append(input("Please Enter Database Name (format DB_NAME): "))
                print("\n")
                
                # Open file in append mode
                with open("Linked History.csv", 'a+', newline='') as write_obj:
                    # Create a writer object from csv module
                    csv_writer = writer(write_obj)
                    # Add contents of list as last row in the csv file
                    csv_writer.writerow(list_of_elem)
            
            # if label is None or empty 
            if label.lower() == 'none' or label.lower() == "n" or label == '':
                Label_check = -1
            
            # Making the name and ID for form 
            if len(Chunks) > 1:
                # Name and ID with quirks 
                name_block = '_'.join(Chunks)
                
                # if label is None or empty 
                if label.lower() == 'none' or label.lower() == "n" or label == '':
                    label = name_block
            else:
                # Name and ID with quirks 
                name_block = Chunks[0]
                
                # if label is None or empty
                if label.lower() == 'none' or label.lower() == "n" or label == '':
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
             
            # if label was not found 
            if Label_check == -1:
                # Search for elements in label dictionary and print the text as the title 
                for element in range(len(Labels)):
                    # Check for the Name of element in both files 
                    if Labels.loc[element, 'Boxname'] == df.loc[row, 'Name']:
                        
                        label_String = Labels.loc[element, 'Labelname']
                        alphabets = list(string.ascii_uppercase) + list(string.ascii_lowercase) 
                        label_String2 = ""

                        for i in range(len(label_String)):
                            if label_String[i] == " " or label_String[i] in alphabets:
                                label_String2 = label_String2 + label_String[i]
        
                        if label_String2 != "":
                            label_String = label_String2
                        else:
                            label_String = "Not Found"
                        # Storing the HTML script 
                        
                        # Storing the HTML script 
                        text = '<td>'+'<p>' + str(label_String) + ' <input id="' + name_block2 + '" name="' + name_block + '" value="[*' + label + '*]"' + ' size="' + '30' + '"' + ' type="text" />' + '</p>' +'</td>'+' \n'
                    
                    else:
                        # Storing the HTML script 
                        text = '<td>'+'<p>' + str(df.loc[row, 'Name']) + ' <input id="' + name_block2 + '" name="' + name_block + '" value="[*' + label + '*]"' + ' size="' + '30' + '"' + ' type="text" />' + '</p>' +'</td>'+' \n'
            
            else:
                # Storing the HTML script 
                text = '<td>'+'<p>' + str(df.loc[row, 'Name']) + ' <input id="' + name_block2 + '" name="' + name_block + '" value="[*' + label + '*]"' + ' size="' + '"100"' + '"' + ' type="text" />' + '</p>' +'</td>'+' \n'
        
        else:
            # Reset the row elements flag
            Row_Elements = 0
            # To Check if label was found or not 
            Label_check = 0
            
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
                    if History.loc[row1, "Database Name"].lower != 'none':
                       
                        # It's the new label
                        label = History.loc[row1, "Database Name"]
                        
                    else:
                        label = "NONE"
            
            # if the label is still empty, which means it is not found in history
            if label == '':
                list_of_elem = []
                
                print("The field name is: %s" % Test_String.lower())
                
                list_of_elem.append(Test_String.lower())
                list_of_elem.append(input("Please Enter Database Name (format DB_NAME): "))
                print("\n")
                
                # Open file in append mode
                with open("Linked History.csv", 'a+', newline='') as write_obj:
                    # Create a writer object from csv module
                    csv_writer = writer(write_obj)
                    # Add contents of list as last row in the csv file
                    csv_writer.writerow(list_of_elem)
            
            # if label is None or empty 
            if label.lower() == 'none' or label.lower() == "n" or label == '':
                Label_check = -1
            
            if len(Chunks) > 1:
                # Name and ID with quirks
                name_block = '_'.join(Chunks)
                
                if label.lower() == 'none' or label.lower() == "n" or label == '':
                    label = name_block
            else:
                # Name and ID with quirks
                name_block = Chunks[0]
                
                if label.lower() == 'none' or label.lower() == "n" or label == '':
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
            
            # if label was not found 
            if Label_check == -1:
                # Search for elements in label dictionary and print the text as the title 
                for element in range(len(Labels)):
                    # Check for the Name of element in both files 
                    if str(Labels.loc[element, 'Boxname']) == str(df.loc[row, 'Name']):
                        
                        label_String = Labels.loc[element, 'Labelname']
                        alphabets = list(string.ascii_uppercase) + list(string.ascii_lowercase) 
                        label_String2 = ""

                        for i in range(len(label_String)):
                            if label_String[i] == " " or label_String[i] in alphabets:
                                label_String2 = label_String2 + label_String[i]
        
                        if label_String2 != "":
                            label_String = label_String2
                        else:
                            label_String = "Not Found"
                        # Storing the HTML script 
                        
                        # Storing the HTML script 
                        text = '<td>'+'<p>' + str(label_String) + ' <input id="' + name_block2 + '" name="' + name_block + '" value="[*' + label + '*]"' + ' size="' + '30' + '"' + ' type="text" />' + '</p>' +'</td>'+' \n'
                    else:
                        # Storing the HTML script 
                        text = '<td>'+'<p>' + str(df.loc[row, 'Name']) + ' <input id="' + name_block2 + '" name="' + name_block + '" value="[*' + label + '*]"' + ' size="' + '"100"' + '"' + ' type="text" />' + '</p>' +'</td>'+' \n'
            else:
                # Storing the HTML script 
                text = '<td>'+'<p>' + str(df.loc[row, 'Name']) + ' <input id="' + name_block2 + '" name="' + name_block + '" value="[*' + label + '*]"' + ' size="' + '30' + '"' + ' type="text" />' + '</p>' +'</td>'+' \n'
        
        # Write general HTML syntax
        file.write(text)
    
    if df.loc[row, "ObjectType"] == "checkbox":
        # Increment the row elements 
        Row_Elements += 1
        
        # Check if the element flag is lower then threshold or not
        if Row_Elements < Threshold:
            
            # Extract the filed name
            Test_String = str(df.loc[row, 'Name'])
            
            # Split the name of the string into words
            Chunks = Test_String.upper().split(' ')
            Chunks2 = Test_String.lower().split(' ')
            
            if len(Chunks) > 1:
                # Name and ID with quirks
                name_block = '_'.join(Chunks)
            else:
                # Name and ID with quirks
                name_block = Chunks[0]
            
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
            
             
            label_String = ""
            for element in range(len(Labels)):
                # Check for the Name of element in both files 
                if Labels.loc[element, 'Boxname'] == Test_String:
                    
                    label_String = Labels.loc[element, 'Labelname']
                    alphabets = list(string.ascii_uppercase) + list(string.ascii_lowercase) 
                    label_String2 = ""
                    
                    for num in range(len(label_String)):
                        if label_String[num] == " " or label_String[num] in alphabets:
                            label_String2 = label_String2 + label_String[num]
        
                    if label_String2 != "":
                        label_String = label_String2
                    else:
                        label_String = "Not Found"
                     
                    # Storing the HTML script
                    text = '<td>'+'<p>' + str(label_String) + ' <input id="' + name_block2 + '" name="' + name_block + '" value="yes"' + ' type="checkbox" />' + '</p>' +'</td>'+' \n'
        
                    
            if label_String == "":
                # Storing the HTML script 
                text = '<td>'+'<p>' + str(df.loc[row, 'Name']) + ' <input id="' + name_block2 + '" name="' + name_block + '" value="yes"' + ' type="checkbox" />' + '</p>' +'</td>'+' \n'
                
        else:
            # Reset the row elements flag
            Row_Elements = 0
            
            # Extract the filed name
            Test_String = str(df.loc[row, 'Name'])
            Test_String = Test_String.upper()
            
            # Split the name of the string into words
            Chunks = Test_String.split(' ')
            Chunks2 = Test_String.lower().split(' ')
            
            if len(Chunks) > 1:
                # Name and ID with quirks
                name_block = '_'.join(Chunks)
            
            else:
                # Name and ID with quirks
                name_block = Chunks[0]
            
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
            
            label_String = ""
            for element in range(len(Labels)):
                # Check for the Name of element in both files 
                if Labels.loc[element, 'Boxname'] == Test_String:
                    
                    label_String = Labels.loc[element, 'Labelname']
                    alphabets = list(string.ascii_uppercase) + list(string.ascii_lowercase) 
                    label_String2 = ""

                    for i in range(len(label_String)):
                        if label_String[i] == " " or label_String[i] in alphabets:
                            label_String2 = label_String2 + label_String[i]
        
                    if label_String2 != "":
                        label_String = label_String2
                    else:
                        label_String = "Not Found"
                     
                    # Storing the HTML script
                    text = '<td>'+'<p>' + str(label_String) + ' <input id="' + name_block2 + '" name="' + name_block + '" value="yes"' + ' type="checkbox" />' + '</p>' +'</td>'+' \n'
        
                    
            if label_String == "":
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

# Close the file
file.close()
