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
    CSV_Name.append(filename[:-4]+"_WithText.csv")
    
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
    
    # Looking for Text Boxes within a page        
    for layer1 in page.findall("LTTextBoxHorizontal"):
        # Looking for Text Lines within a Text Box
        for layer2 in layer1.findall("LTTextLineHorizontal"):
            # Text should not be Null Object or empty (without alphabest) 
            if layer2.text != " " and layer2.text != None and layer2.text != "":
                # Text should not be repetitive (avoids clash with annots)
                if layer2.text not in name:
                    # Remove "☐" symbol
                    if "☐" not in layer2.text:
                    
                        name.append(layer2.text)
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
                # Text should not be repetitive (avoids clash with annots)
                if layer2.text not in name:
                    # Remove "☐" symbol
                    if "☐" not in layer2.text:
                    
                        name.append(layer2.text)
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
                    # Text should not be repetitive (avoids clash with annots)
                    if layer3.text not in name:
                        # Remove "☐" symbol
                        if "☐" not in layer3.text: 
                            
                            name.append(layer3.text)
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
                    # Text should not be repetitive (avoids clash with annots)
                    if layer3.text not in name:
                        # Remove "☐" symbol
                        if "☐" not in layer3.text:
                            
                            name.append(layer3.text)
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
                # Text should not be repetitive (avoids clash with annots)
                if layer1.text not in name:
                    # Remove "☐" symbol
                    if "☐" not in layer1.text:
                        
                        name.append(layer1.text)
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
                                # Text should not be repetitive (avoids clash with annots)
                                if layer5.text not in name:
                                    # Remove "☐" symbol
                                    if "☐" not in layer5.text:
                        
                                        name.append(layer5.text)
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
                                # Text should not be repetitive (avoids clash with annots)
                                if layer5.text not in name:
                                    # Remove "☐" symbol
                                    if "☐" not in layer5.text:
                        
                                        name.append(layer5.text)
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
                    # Text should not be repetitive (avoids clash with annots)
                    if layer3.text not in name:
                        # Remove "☐" symbol
                        if "☐" not in layer3.text:
                                
                            name.append(layer3.text)
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
                    # Text should not be repetitive (avoids clash with annots)
                    if layer3.text not in name:
                        # Remove "☐" symbol
                        if "☐" not in layer3.text:
                            
                            name.append(layer3.text)
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
                        # Text should not be repetitive (avoids clash with annots)
                        if layer4.text not in name:
                            # Remove "☐" symbol
                            if "☐" not in layer4.text:
                                
                                name.append(layer4.text)
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
                        # Text should not be repetitive (avoids clash with annots)
                        if layer4.text not in name:
                            # Remove "☐" symbol
                            if "☐" not in layer4.text:
                                
                                name.append(layer4.text)
                                width.append(layer4.attrib.get("width"))
                                height.append(layer4.attrib.get("height"))
                                x_0.append(layer4.attrib.get("x0"))
                                y_0.append(layer4.attrib.get("y0"))
                                x_1.append(layer4.attrib.get("x1"))
                                y_1.append(layer4.attrib.get("y1"))
                                types.append("plain text")    
                                
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
                        
        # Looking for Annots within a Figure
        for layer2 in layer1.findall("LTTextBoxHorizontal"):
            
            # Text should not be Null Object or empty (without alphabest)
            if layer2.text != " " and layer2.text != None and layer2.text != "":
                # Text should not be repetitive (avoids clash with annots)
                if layer2.text not in name:
                    # Remove "☐" symbol
                    if "☐" not in layer2.text:
                                
                        name.append(layer2.text)
                        width.append(layer2.attrib.get("width"))
                        height.append(layer2.attrib.get("height"))
                        x_0.append(layer2.attrib.get("x0"))
                        y_0.append(layer2.attrib.get("y0"))
                        x_1.append(layer2.attrib.get("x1"))
                        y_1.append(layer2.attrib.get("y1"))
                        types.append("plain text")
            
            # Looking for interactive elements within Text Lines
            for layer3 in layer2.findall("LTTextLineHorizontal"):  
                
                # Text should not be repetitive (avoids clash with annots)
                if layer3.text not in name:
                    # Remove "☐" symbol
                    if "☐" not in layer3.text:
                            
                        name.append(layer3.text)
                        width.append(layer3.attrib.get("width"))
                        height.append(layer3.attrib.get("height"))
                        x_0.append(layer3.attrib.get("x0"))
                        y_0.append(layer3.attrib.get("y0"))
                        x_1.append(layer3.attrib.get("x1"))
                        y_1.append(layer3.attrib.get("y1"))
                        types.append("plain text")   
            
        # Looking for Annots within a Figure
        for layer2 in layer1.findall("LTTextLineHorizontal"):
            
            # Text should not be Null Object or empty (without alphabest)
            if layer2.text != " " and layer2.text != None and layer2.text != "":
                # Text should not be repetitive (avoids clash with annots)
                if layer2.text not in name:
                    # Remove "☐" symbol
                    if "☐" not in layer2.text:
                                
                        name.append(layer2.text)
                        width.append(layer2.attrib.get("width"))
                        height.append(layer2.attrib.get("height"))
                        x_0.append(layer2.attrib.get("x0"))
                        y_0.append(layer2.attrib.get("y0"))
                        x_1.append(layer2.attrib.get("x1"))
                        y_1.append(layer2.attrib.get("y1"))
                        types.append("plain text")
            
            # Looking for interactive elements within Text Lines
            for layer3 in layer2.findall("LTTextBoxHorizontal"):  
                
                # Text should not be repetitive (avoids clash with annots)
                if layer3.text not in name:
                    # Remove "☐" symbol
                    if "☐" not in layer3.text:
                            
                        name.append(layer3.text)
                        width.append(layer3.attrib.get("width"))
                        height.append(layer3.attrib.get("height"))
                        x_0.append(layer3.attrib.get("x0"))
                        y_0.append(layer3.attrib.get("y0"))
                        x_1.append(layer3.attrib.get("x1"))
                        y_1.append(layer3.attrib.get("y1"))
                        types.append("plain text")    
        
        # Looking for Annots within a Figure
        for layer2 in layer1.findall("LTRect"):
            # Looking for Annots within a Figure
            for layer3 in layer2.findall("LTRect"):  
                # Looking for Text Box within the Rectangular Space         
                for layer4 in layer3.findall("LTTextBoxHorizontal"):
                    # Looking for Text Line within the Text Box
                    for layer5 in layer4.findall("LTTextLineHorizontal"):
                        # Text should not be Null Object or empty (without alphabest)
                        if layer5.text != " " and layer5.text != None and layer5.text != "":
                            # Text should not be repetitive (avoids clash with annots)
                            if layer5.text not in name:
                                # Remove "☐" symbol
                                if "☐" not in layer5.text:
                                
                                    name.append(layer5.text)
                                    width.append(layer5.attrib.get("width"))
                                    height.append(layer5.attrib.get("height"))
                                    x_0.append(layer5.attrib.get("x0"))
                                    y_0.append(layer5.attrib.get("y0"))
                                    x_1.append(layer5.attrib.get("x1"))
                                    y_1.append(layer5.attrib.get("y1"))
                                    types.append("plain text")
        
data = {'Name':name, 'Width': width, 'Height': height, 
        'x0': x_0, 'y0': y_0, 'x1': x_1, 'y1': y_1, 'ObjectType': types}              
df = pd.DataFrame(data)    
df = df.sort_values(["y1", "x1"], ascending = False)

df.to_csv(CSV_Name[File_Number])            