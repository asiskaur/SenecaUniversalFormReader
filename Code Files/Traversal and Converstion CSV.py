# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:07:14 2021

@author: ca273
"""
# Import the xml traverser: install before importing
import xml.etree.ElementTree as ET
# import dependcy for data structure
import pandas as pd
# Import dependency to load csv data and load location of current directory
import os

# Get the current working directory and convert it into a iterable
path = os.getcwd()
dirs = os.listdir(path)

# Empty list to store the name of XML fiels
XML_Files = []

# Find all the XML files
for file in dirs:
    if '.xml' in file.lower():
        XML_Files.append(file)

# Empty List to store the name of CSV files
CSV_Name = []

# Create names for CSV Files to be created 
for filename in XML_Files:
    CSV_Name.append(filename[:-4]+".csv")
    
# List all the files in the directory
for num in range(len(XML_Files)):
    print("%d. - %s" % (num, XML_Files[num]))

# Choosing a file
File_Number = int(input("Please choose a file number from the above list: "))

# Load the parse from the Tree
Form = ET.parse(XML_Files[File_Number])

# get the root of the form tree
root = Form.getroot()

# demo variable to store the element attributes
name = []
width = []
height = []
x_0 = []
y_0 = []
x_1 = []
y_1 = [] 
types = []

# Looking for elements page by page
for page in root.findall("LTPage"): 
    
    # Looking for Text Box in the Page
    for layer1 in page.findall("LTTextBoxHorizontal"):
        # Looking for Interactive elements within a Text Box
        for layer2 in layer1.findall("Annot"):
            # Name of Interactive Element should not be None 
            if layer2.attrib.get("T") != None:
                
                name.append(layer2.attrib.get("T"))
                width.append(layer2.attrib.get("width"))
                height.append(layer2.attrib.get("height"))
                x_0.append(layer2.attrib.get("x0"))
                y_0.append(layer2.attrib.get("y0"))
                x_1.append(layer2.attrib.get("x1"))
                y_1.append(layer2.attrib.get("y1"))
                
                # Check if it's a blank text fillup or a checkbox
                if layer2.attrib.get("FT") == "/Tx":
                    types.append("text fillup")
                else:
                    types.append("checkbox")
    
    # Looking for Images in the Page
    for layer1 in page.findall("LTImage"):
        # Looking for Interactive elements within a Image
        for layer2 in layer1.findall("Annot"):
            # Name of Interactive Element should not be None 
            if layer2.attrib.get("T") != None:
                    
                name.append(layer2.attrib.get("T"))
                width.append(layer2.attrib.get("width"))
                height.append(layer2.attrib.get("height"))
                x_0.append(layer2.attrib.get("x0"))
                y_0.append(layer2.attrib.get("y0"))
                x_1.append(layer2.attrib.get("x1"))
                y_1.append(layer2.attrib.get("y1"))
                
                # Check if it's a blank text fillup or a checkbox
                if layer2.attrib.get("FT") == "/Tx":
                    types.append("text fillup")
                else:
                    types.append("checkbox")
        
        # Looking for Logical Figures within a Image
        for layer2 in layer1.findall("LTFigure"):
            # Looking for Interactive elements within a Figures
            for layer3 in layer2.findall("Annot"):
                
                # Name of Interactive Element should not be None 
                if layer3.attrib.get("T") != None:
            
                    name.append(layer3.attrib.get("T"))
                    width.append(layer3.attrib.get("width"))
                    height.append(layer3.attrib.get("height"))
                    x_0.append(layer3.attrib.get("x0"))
                    y_0.append(layer3.attrib.get("y0"))
                    x_1.append(layer3.attrib.get("x1"))
                    y_1.append(layer3.attrib.get("y1"))
                
                    # Check if it's a blank text fillup or a checkbox
                    if layer3.attrib.get("FT") == "/Tx":
                        types.append("text fillup")
                    else:
                        types.append("checkbox")
                        
            # Looking for Rectnagular Spaces within a Figures            
            for layer3 in layer2.findall("LTRect"):
                # Looking for Interactive elements within a Rectangular Spaces
                for layer4 in layer3.findall("Annot"):    
                    # Name of Interactive Element should not be None 
                    if layer4.attrib.get("T") != None:
                        
                        name.append(layer4.attrib.get("T"))
                        width.append(layer4.attrib.get("width"))
                        height.append(layer4.attrib.get("height"))
                        x_0.append(layer4.attrib.get("x0"))
                        y_0.append(layer4.attrib.get("y0"))
                        x_1.append(layer4.attrib.get("x1"))
                        y_1.append(layer4.attrib.get("y1"))
                            
                        # Check if it's a blank text fillup or a checkbox
                        if layer4.attrib.get("FT") == "/Tx":
                            types.append("text fillup")
                        else:
                            types.append("checkbox")
                            
                # Looking for Images within Rectangular Spaces
                for layer4 in layer3.findall("LTImage"):
                    # Looking for Logical Figures within the Images
                    for layer5 in layer4.findall("LTFigure"):
                        # Looking for Interactive Elements within the Logical Figures
                        for layer6 in layer5.findall("Annot"):
                            # Name of Interactive Element should not be None 
                            if layer6.attrib.get("T") != None:
                                    
                                name.append(layer6.attrib.get("T"))
                                width.append(layer6.attrib.get("width"))
                                height.append(layer6.attrib.get("height"))
                                x_0.append(layer6.attrib.get("x0"))
                                y_0.append(layer6.attrib.get("y0"))
                                x_1.append(layer6.attrib.get("x1"))
                                y_1.append(layer6.attrib.get("y1"))
                
                                # Check if it's a blank text fillup or a checkbox
                                if layer6.attrib.get("FT") == "/Tx":
                                    types.append("text fillup")
                                else:
                                    types.append("checkbox")
                                
                # Looking for Text Box within Rectangular Spaces
                for layer4 in layer3.findall("LTTextBoxHorizontal"):
                    # Looking for Interactive elements within Text Boxes
                    for layer5 in layer4.findall("Annot"):
                        
                        # Name of Interactive Element should not be None 
                        if layer5.attrib.get("T") != None:
                
                            name.append(layer5.attrib.get("T"))
                            width.append(layer5.attrib.get("width"))
                            height.append(layer5.attrib.get("height"))
                            x_0.append(layer5.attrib.get("x0"))
                            y_0.append(layer5.attrib.get("y0"))
                            x_1.append(layer5.attrib.get("x1"))
                            y_1.append(layer5.attrib.get("y1"))
                
                            # Check if it's a blank text fillup or a checkbox
                            if layer5.attrib.get("FT") == "/Tx":
                                types.append("text fillup")
                            else:
                                types.append("checkbox")

    # Looking for Interactive elements within a page
    for layer1 in page.findall("Annot"):
        # Name of Interactive Element should not be None 
        if layer1.attrib.get("T") != None:
                
            name.append(layer1.attrib.get("T"))
            width.append(layer1.attrib.get("width"))
            height.append(layer1.attrib.get("height"))
            x_0.append(layer1.attrib.get("x0"))
            y_0.append(layer1.attrib.get("y0"))
            x_1.append(layer1.attrib.get("x1"))
            y_1.append(layer1.attrib.get("y1"))
        
            # Check if it's a blank text fillup or a checkbox
            if layer1.attrib.get("FT") == "/Tx":
                types.append("text fillup")
            else:
                types.append("checkbox")
     
    # Looking for designated rectangular spaces within a page        
    for layer1 in page.findall("LTRect"):
        # Looking for interactive spaces within those rectangular spaces
        for layer2 in layer1.findall("Annot"):
            # Name of Interactive Element should not be None 
            if layer2.attrib.get("T") != None:
                
                name.append(layer2.attrib.get("T"))
                width.append(layer2.attrib.get("width"))
                height.append(layer2.attrib.get("height"))
                x_0.append(layer2.attrib.get("x0"))
                y_0.append(layer2.attrib.get("y0"))
                x_1.append(layer2.attrib.get("x1"))
                y_1.append(layer2.attrib.get("y1"))
        
                # Check if it's a blank text fillup or a checkbox
                if "Tx" in layer2.attrib.get("FT"):
                    types.append("text fillup")
                else:
                    types.append("checkbox")
        
        # Looking for designated rectangular spaces within rectangular spaces
        for layer2 in layer1.findall("LTRect"):
            # Looking for interactive spaces within those rectangular spaces
            for layer3 in layer2.findall("Annot"):
                # Name of Interactive Element should not be None 
                if layer3.attrib.get("T") != None:
                
                    name.append(layer3.attrib.get("T"))
                    width.append(layer3.attrib.get("width"))
                    height.append(layer3.attrib.get("height"))
                    x_0.append(layer3.attrib.get("x0"))
                    y_0.append(layer3.attrib.get("y0"))
                    x_1.append(layer3.attrib.get("x1"))
                    y_1.append(layer3.attrib.get("y1"))
        
                    # Check if it's a blank text fillup or a checkbox
                    if layer3.attrib.get("FT") == "/Tx":
                        types.append("text fillup")
                    else:
                        types.append("checkbox")
    
    # Looking for designated rectangular spaces within a page 
    for layer1 in page.findall("LTRect"):
        # Looking for Text Boxes within designated rectangular spaces
        for layer2 in layer1.findall("LTTextBoxHorizontal"):
            # Looking for Interactive elements within a Text Box
            for layer3 in layer2.findall("Annot"):
                
                name.append(layer3.attrib.get("T"))
                width.append(layer3.attrib.get("width"))
                height.append(layer3.attrib.get("height"))
                x_0.append(layer3.attrib.get("x0"))
                y_0.append(layer3.attrib.get("y0"))
                x_1.append(layer3.attrib.get("x1"))
                y_1.append(layer3.attrib.get("y1"))
        
                # Check if it's a blank text fillup or a checkbox
                if layer3.attrib.get("FT") == "/Tx":
                    types.append("text fillup")
                else:
                    types.append("checkbox")
    
    # Looking for Text Boxes within a page 
    for layer1 in page.findall("LTTextBoxHorizontal"):    
        # Looking for Text Lines within a Text Box
        for layer2 in layer1.findall("LTTextLineHorizontal"):
            # Looking for interactive elements within Text Lines
            for layer3 in layer2.findall("Annot"):
                
                name.append(layer3.attrib.get("T"))
                width.append(layer3.attrib.get("width"))
                height.append(layer3.attrib.get("height"))
                x_0.append(layer3.attrib.get("x0"))
                y_0.append(layer3.attrib.get("y0"))
                x_1.append(layer3.attrib.get("x1"))
                y_1.append(layer3.attrib.get("y1"))
        
                # Check if it's a blank text fillup or a checkbox
                if layer3.attrib.get("FT") == "/Tx":
                    types.append("text fillup")
                else:
                    types.append("checkbox")

                           
    # Looking for Text Boxes within a page 
    for layer1 in page.findall("LTTextLineHorizontal"):
        
        # Looking for Text Lines within a Text Box
        for layer2 in layer1.findall("LTTextBoxHorizontal"):
            # Looking for interactive elements within Text Lines
            for layer3 in layer2.findall("Annot"):
                
                name.append(layer3.attrib.get("T"))
                width.append(layer3.attrib.get("width"))
                height.append(layer3.attrib.get("height"))
                x_0.append(layer3.attrib.get("x0"))
                y_0.append(layer3.attrib.get("y0"))
                x_1.append(layer3.attrib.get("x1"))
                y_1.append(layer3.attrib.get("y1"))
        
                # Check if it's a blank text fillup or a checkbox
                if layer3.attrib.get("FT") == "/Tx":
                    types.append("text fillup")
                else:
                    types.append("checkbox")           
                    
    # Looking for Figures within a page 
    for layer1 in page.findall("LTFigure"):
        
        # Looking for Annots within a Figure
        for layer2 in layer1.findall("Annot"):
            
            name.append(layer2.attrib.get("T"))
            width.append(layer2.attrib.get("width"))
            height.append(layer2.attrib.get("height"))
            x_0.append(layer2.attrib.get("x0"))
            y_0.append(layer2.attrib.get("y0"))
            x_1.append(layer2.attrib.get("x1"))
            y_1.append(layer2.attrib.get("y1"))
        
            # Check if it's a blank text fillup or a checkbox
            if layer2.attrib.get("FT") == "/Tx":
                types.append("text fillup")
            else:
                types.append("checkbox")
        
        # Looking for Annots within a Figure
        for layer2 in layer1.findall("LTTextBoxHorizontal"):
            
            # Looking for interactive elements within Text Lines
            for layer3 in layer2.findall("Annot"):
                
                name.append(layer3.attrib.get("T"))
                width.append(layer3.attrib.get("width"))
                height.append(layer3.attrib.get("height"))
                x_0.append(layer3.attrib.get("x0"))
                y_0.append(layer3.attrib.get("y0"))
                x_1.append(layer3.attrib.get("x1"))
                y_1.append(layer3.attrib.get("y1"))
        
                # Check if it's a blank text fillup or a checkbox
                if layer3.attrib.get("FT") == "/Tx":
                    types.append("text fillup")
                else:
                    types.append("checkbox")
        
        # Looking for Annots within a Figure
        for layer2 in layer1.findall("LTTextLineHorizontal"):
            
            # Looking for interactive elements within Text Lines
            for layer3 in layer2.findall("Annot"):
                
                name.append(layer3.attrib.get("T"))
                width.append(layer3.attrib.get("width"))
                height.append(layer3.attrib.get("height"))
                x_0.append(layer3.attrib.get("x0"))
                y_0.append(layer3.attrib.get("y0"))
                x_1.append(layer3.attrib.get("x1"))
                y_1.append(layer3.attrib.get("y1"))
        
                # Check if it's a blank text fillup or a checkbox
                if layer3.attrib.get("FT") == "/Tx":
                    types.append("text fillup")
                else:
                    types.append("checkbox")
        
        # Looking for Annots within a Figure
        for layer2 in layer1.findall("LTTextBoxHorizontal"):
            
            # Looking for interactive elements within Text Lines
            for layer3 in layer2.findall("LTTextLineHorizontal"):
                
                # Looking for interactive elements within Text Lines
                for layer4 in layer3.findall("Annot"):
                
                    name.append(layer4.attrib.get("T"))
                    width.append(layer4.attrib.get("width"))
                    height.append(layer4.attrib.get("height"))
                    x_0.append(layer4.attrib.get("x0"))
                    y_0.append(layer4.attrib.get("y0"))
                    x_1.append(layer4.attrib.get("x1"))
                    y_1.append(layer4.attrib.get("y1"))
        
                    # Check if it's a blank text fillup or a checkbox
                    if layer4.attrib.get("FT") == "/Tx":
                        types.append("text fillup")
                    else:
                        types.append("checkbox")
                
        # Looking for Annots within a Figure
        for layer2 in layer1.findall("LTTextLineHorizontal"):
            
            # Looking for interactive elements within Text Lines
            for layer3 in layer2.findall("LTTextBoxHorizontal"):
                
                # Looking for interactive elements within Text Lines
                for layer4 in layer3.findall("Annot"):
                
                    name.append(layer4.attrib.get("T"))
                    width.append(layer4.attrib.get("width"))
                    height.append(layer4.attrib.get("height"))
                    x_0.append(layer4.attrib.get("x0"))
                    y_0.append(layer4.attrib.get("y0"))
                    x_1.append(layer4.attrib.get("x1"))
                    y_1.append(layer4.attrib.get("y1"))
        
                    # Check if it's a blank text fillup or a checkbox
                    if layer4.attrib.get("FT") == "/Tx":
                        types.append("text fillup")
                    else:
                        types.append("checkbox")
        
# Creating a mapped data dictornary for the form
data = {'Name':name, 'Width': width, 'Height': height, 
        'x0': x_0, 'y0': y_0, 'x1': x_1, 'y1': y_1, 'ObjectType': types}              

# Storing the data dictionary in a dataframe
df = pd.DataFrame(data)    

# Sorting the dataframe to align the elements 
df = df.sort_values(["y1", "x1"], ascending = False)

# Pruning the plain text 
df = df[df.ObjectType != "plain text"]

# removing all the blank elements
df.dropna(inplace = True)

# Store the dataframe as Comma Separated Excel file
df.to_csv(CSV_Name[File_Number])            
