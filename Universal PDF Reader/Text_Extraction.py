# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:32:17 2021

@author: ca273
"""
# Import the xml traverser: install before importing
import xml.etree.ElementTree as ET
# import dependency for data structure
import pandas as pd
# Import dependency to load csv data and load location of current directory
import os

# Get the current working directory and convert it into a iterable
path = os.getcwd()
dirs = os.listdir(path)

# Empty list to store the name of csv fiels
XML_Files = []

# Find all the csv files
for file in dirs:
    if '.xml' in file.lower():
        XML_Files.append(file)

# Empty List to store the name of html files
CSV_Name = []

# Create names for HTML Files to be created 
for filename in XML_Files:
    CSV_Name.append(filename[:-4]+"_Text.csv")

# Load the parse from the Tree
Form = ET.parse(XML_Files[0])

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
    
    # Looking for Text Boxes within a page        
    for layer1 in page.findall("LTTextBoxHorizontal"):
        
        # Looking for Text Lines within a Text Box
        for layer2 in layer1.findall("LTTextLineHorizontal"):
            
            # Text should not be Null Object or empty (without alphabest) 
            if layer2.text != " " and layer2.text != None and layer2.text != "":
                
                # Avoid symbol 
                if "☐" not in layer2.text:
                    
                    test_string = layer2.text
                    new_string = ""

                    for char in test_string:
                        if char.isalpha() or char == " " or char.isdigit():
                            new_string += "".join(char)
                    
                        
                    name.append(new_string)
                    width.append(layer2.attrib.get("width"))
                    height.append(layer2.attrib.get("height"))
                    x_0.append(layer2.attrib.get("x0"))
                    y_0.append(layer2.attrib.get("y0"))
                    x_1.append(layer2.attrib.get("x1"))
                    y_1.append(layer2.attrib.get("y1"))
                    types.append("plain text")
    
    # Looking for Text Line within a page
    for layer1 in page.findall("LTTextLineHorizontal"):
        
        # Looking for Text Boxes within a Text Line
        for layer2 in layer1.findall("LTTextBoxHorizontal"):
            
            # Text should not be Null Object or empty (without alphabest) 
            if layer2.text != " " and layer2.text != None and layer2.text != "":
                    
                # Remove "☐" symbol
                if "☐" not in layer2.text:
                
                    test_string = layer2.text
                    new_string = ""

                    for char in test_string:
                        if char.isalpha() or char == " " or char.isdigit():
                            new_string += "".join(char)
                    
                    name.append(new_string)
                    width.append(layer2.attrib.get("width"))
                    height.append(layer2.attrib.get("height"))
                    x_0.append(layer2.attrib.get("x0"))
                    y_0.append(layer2.attrib.get("y0"))
                    x_1.append(layer2.attrib.get("x1"))
                    y_1.append(layer2.attrib.get("y1"))
                    types.append("plain text")    
    
    # Looking for Logically Tree Curve within a page
    for layer1 in page.findall("LTCurve"):
        
        # Looking for Text Line within the Curve 
        for layer2 in layer1.findall("LTTextLineHorizontal"):
           
            # looking for Text Box within the Text Line 
            for layer3 in layer2.findall("LTTextBoxHorizontal"):
                
                # Text should not be Null Object or empty (without alphabest) 
                if layer3.text != " " and layer3.text != None and layer3.text != "":
                        
                    # Remove "☐" symbol
                    if "☐" not in layer3.text:
                        
                        test_string = layer3.text
                        new_string = ""

                        for char in test_string:
                            if char.isalpha() or char == " ":
                                new_string += "".join(char)
                            
                        name.append(new_string)
                        width.append(layer3.attrib.get("width"))
                        height.append(layer3.attrib.get("height"))
                        x_0.append(layer3.attrib.get("x0"))
                        y_0.append(layer3.attrib.get("y0"))
                        x_1.append(layer3.attrib.get("x1"))
                        y_1.append(layer3.attrib.get("y1"))
                        types.append("plain text")
         
        # Looking for Text Box within the Curve            
        for layer2 in layer1.findall("LTTextBoxHorizontal"):
            
            # looking for Text Line within the Text Box
            for layer3 in layer2.findall("LTTextLineHorizontal"):
                
                # Text should not be Null Object or empty (without alphabest)
                if layer3.text != " " and layer3.text != None and layer3.text != "":
                
                    # Remove "☐" symbol
                    if "☐" not in layer3.text:
                        
                        test_string = layer3.text
                        new_string = ""

                        for char in test_string:
                            if char.isalpha() or char == " ":
                                new_string += "".join(char)
                            
                        name.append(new_string)
                        width.append(layer3.attrib.get("width"))
                        height.append(layer3.attrib.get("height"))
                        x_0.append(layer3.attrib.get("x0"))
                        y_0.append(layer3.attrib.get("y0"))
                        x_1.append(layer3.attrib.get("x1"))
                        y_1.append(layer3.attrib.get("y1"))
                        types.append("plain text")    
        
        # Looking for Tex Boxes in Pages 
        for layer1 in page.findall("LTTextBoxHorizontal"):
            
            # Text should not be Null Object or empty (without alphabest)
            if layer1.text != " " and layer1.text != None and layer1.text != "":
                    
                # Remove "☐" symbol
                if "☐" not in layer1.text:
                    
                    test_string = layer1.text
                    new_string = ""

                    for char in test_string:
                        if char.isalpha() or char == " ":
                            new_string += "".join(char)
                            
                    name.append(new_string)
                    width.append(layer1.attrib.get("width"))
                    height.append(layer1.attrib.get("height"))
                    x_0.append(layer1.attrib.get("x0"))
                    y_0.append(layer1.attrib.get("y0"))
                    x_1.append(layer1.attrib.get("x1"))
                    y_1.append(layer1.attrib.get("y1"))
                    types.append("plain text")
        
        # Looking for Images in the pages
        for layer1 in page.findall("LTImage"):
            
            # Looking for Figures in the Images
            for layer2 in layer1.findall("LTFigure"):
                
                # Looking for rectangular spaces in the Figures 
                for layer3 in layer2.findall("LTRect"):
                    
                    # Looking for Text Lines in the Rectangular Spaces
                    for layer4 in layer3.findall("LTTextLineHorizontal"):
                        
                        # Looking for Text Boxes in the Text Lines
                        for layer5 in layer4.findall("LTTextBoxHorizontal"):
                            
                            # Text should not be Null Object or empty (without alphabest)
                            if layer5.text != " " and layer5.text != None and layer5.text != "":
                                    
                                # Remove "☐" symbol
                                if "☐" not in layer5.text:
                                    
                                    test_string = layer5.text
                                    new_string = ""

                                    for char in test_string:
                                        if char.isalpha() or char == " ":
                                            new_string += "".join(char)
                            
                                    name.append(new_string)
                                    width.append(layer5.attrib.get("width"))
                                    height.append(layer5.attrib.get("height"))
                                    x_0.append(layer5.attrib.get("x0"))
                                    y_0.append(layer5.attrib.get("y0"))
                                    x_1.append(layer5.attrib.get("x1"))
                                    y_1.append(layer5.attrib.get("y1"))
                                    types.append("plain text")
                    
                    # Looking for Text Boxes in the Rectangular Space
                    for layer4 in layer3.findall("LTTextBoxHorizontal"):
                        
                        # Looking for Text Lines in the Text Boxes
                        for layer5 in layer4.findall("LTTextLineHorizontal"):
                            
                            # Text should not be Null Object or empty (without alphabest)
                            if layer5.text != " " and layer5.text != None and layer5.text != "":
                                    
                                # Remove "☐" symbol
                                if "☐" not in layer5.text:
                                    
                                    test_string = layer5.text
                                    new_string = ""

                                    for char in test_string:
                                        if char.isalpha() or char == " ":
                                            new_string += "".join(char)
                            
                                    name.append(new_string)
                                    width.append(layer5.attrib.get("width"))
                                    height.append(layer5.attrib.get("height"))
                                    x_0.append(layer5.attrib.get("x0"))
                                    y_0.append(layer5.attrib.get("y0"))
                                    x_1.append(layer5.attrib.get("x1"))
                                    y_1.append(layer5.attrib.get("y1"))
                                    types.append("plain text")
                            
        
    # Looking for designated rectangular spaces within a page                    
    for layer1 in page.findall("LTRect"):
        
        # Looking for Text Line within the Rectangular Space
        for layer2 in layer1.findall("LTTextLineHorizontal"):
            
            # Looking for Text Box within the Text Line
            for layer3 in layer2.findall("LTTextBoxHorizontal"):
                
                # Text should not be Null Object or empty (without alphabest)
                if layer3.text != " " and layer3.text != None and layer3.text != "":
                        
                    # Remove "☐" symbol
                    if "☐" not in layer3.text:
                        
                        test_string = layer3.text
                        new_string = ""

                        for char in test_string:
                            if char.isalpha() or char == " ":
                                new_string += "".join(char)
                            
                        name.append(new_string)
                        width.append(layer3.attrib.get("width"))
                        height.append(layer3.attrib.get("height"))
                        x_0.append(layer3.attrib.get("x0"))
                        y_0.append(layer3.attrib.get("y0"))
                        x_1.append(layer3.attrib.get("x1"))
                        y_1.append(layer3.attrib.get("y1"))
                        types.append("plain text")
         
        # Looking for Text Box within the Rectangular Space            
        for layer2 in layer1.findall("LTTextBoxHorizontal"):
            
            # Looking for Text Line within the Text Box
            for layer3 in layer2.findall("LTTextLineHorizontal"):
                
                # Text should not be Null Object or empty (without alphabest)
                if layer3.text != " " and layer3.text != None and layer3.text != "":
                        
                    # Remove "☐" symbol
                    if "☐" not in layer3.text:
                        
                        test_string = layer3.text
                        new_string = ""

                        for char in test_string:
                            if char.isalpha() or char == " ":
                                new_string += "".join(char)
                            
                        name.append(new_string)
                        width.append(layer3.attrib.get("width"))
                        height.append(layer3.attrib.get("height"))
                        x_0.append(layer3.attrib.get("x0"))
                        y_0.append(layer3.attrib.get("y0"))
                        x_1.append(layer3.attrib.get("x1"))
                        y_1.append(layer3.attrib.get("y1"))
                        types.append("plain text")   
                        
        
        # Looking for Rectangular Space within the Rectangular Space            
        for layer2 in layer1.findall("LTRect"):
            
            # Looking for Text Line within the Rectangular Space 
            for layer3 in layer2.findall("LTTextLineHorizontal"):
                
                # Looking for Text Box within the Text Line
                for layer4 in layer3.findall("LTTextBoxHorizontal"):
                    
                    # Text should not be Null Object or empty (without alphabest)
                    if layer4.text != " " and layer4.text != None and layer4.text != "":
                 
                        # Remove "☐" symbol
                        if "☐" not in layer4.text:
                            
                            test_string = layer4.text
                            new_string = ""

                            for char in test_string:
                                if char.isalpha() or char == " ":
                                    new_string += "".join(char)
                            
                            name.append(new_string)
                            width.append(layer4.attrib.get("width"))
                            height.append(layer4.attrib.get("height"))
                            x_0.append(layer4.attrib.get("x0"))
                            y_0.append(layer4.attrib.get("y0"))
                            x_1.append(layer4.attrib.get("x1"))
                            y_1.append(layer4.attrib.get("y1"))
                            types.append("plain text")   
             
            # Looking for Text Box within the Rectangular Space         
            for layer3 in layer2.findall("LTTextBoxHorizontal"):
                
                # Looking for Text Line within the Text Box
                for layer4 in layer3.findall("LTTextLineHorizontal"):
                    
                    # Text should not be Null Object or empty (without alphabest)
                    if layer4.text != " " and layer4.text != None and layer4.text != "":
                        
                        # Remove "☐" symbol
                        if "☐" not in layer4.text:
                                
                            test_string = layer4.text
                            new_string = ""

                            for char in test_string:
                                if char.isalpha() or char == " ":
                                    new_string += "".join(char)
                            
                            name.append(new_string)
                            width.append(layer4.attrib.get("width"))
                            height.append(layer4.attrib.get("height"))
                            x_0.append(layer4.attrib.get("x0"))
                            y_0.append(layer4.attrib.get("y0"))
                            x_1.append(layer4.attrib.get("x1"))
                            y_1.append(layer4.attrib.get("y1"))
                            types.append("plain text")
                            
data = {'Name':name, 'Width': width, 'Height': height, 
        'x0': x_0, 'y0': y_0, 'x1': x_1, 'y1': y_1, 'ObjectType': types}              
df = pd.DataFrame(data)    
df = df.sort_values(["y1", "x1"], ascending = False)
df.to_csv(CSV_Name[0])            