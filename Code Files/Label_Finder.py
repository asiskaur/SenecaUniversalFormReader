#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 13:30:26 2021

@author: owner

"""
# import dependencies for data structure
import pandas as pd
import numpy as np

# Import dependency to load csv data and load location of current directory
import os

# Get the current working directory and convert it into a iterable
path = os.getcwd()
dirs = os.listdir(path)

# Empty list to store the name of csv fiels
CSV_Files = []
New_CSV = []

# Find all the csv files
for file in dirs:
    if '.csv' in file.lower():
        CSV_Files.append(file)
        
# Create names for New CSV Files to be created 
for filename in CSV_Files:
    New_CSV.append(filename[:-4]+"_Labels.csv")

# List all the files in the directory
for num in range(len(CSV_Files)):
    print("%d. - %s" % (num, CSV_Files[num]))

# Choosing a file
File_Number = int(input("Please choose a file number from the above list: "))

# Reading the dataframe and sorting them in ascending order
dataframe = pd.read_csv(CSV_Files[File_Number])
dataframe1 = dataframe.sort_values(by=['y0'], ascending = False)

# Dictionary to store key value pairs of name and label
dicti={}
# List to store the index of the labels 
list_arrays = []

list1_x0 =  list(dataframe1['x0'])
list1_x1 =  list(dataframe1['x1'])
list1_y0 =  list(dataframe1['y0'])
list1_y1 =  list(dataframe1['y1'])
list_name = list(dataframe1['Name'])
obj_type = list(dataframe1["ObjectType"])

# Iterate over the position list     
for i in  range(len(list1_x0)):
    
    # Check if the ovject is a text box or checkbox 
    if obj_type[i] == "checkbox" or obj_type[i] == "text fillup":
        
        # Empty dictionary to store minimum values
        min_list = {}
        # Find centers with mean of the coordinates
        center_i1 = (list1_x0[i]+list1_x1[i])/2
        center_i2 = (list1_y0[i]+list1_y1[i])/2
        
        for j in range(len(list1_x0)):
            # Check if the type is a plain text
            if obj_type[j] == "plain text":
                
                # Find centers with mean of the coordinates
                center_j1 = (list1_x0[j]+list1_x1[j])/2
                center_j2 = (list1_y0[j]+list1_y1[j])/2
                
                # Find the eucleadian distance of the labels and plain text
                dis = np.sqrt(((center_i1-center_j1)**2) + ((center_i2-center_j2)**2))
                
                # Store the minimum distance and index in a dictionary
                min_list[dis] = j      
        
        # Check if dictionary has more them one entry
        if len(min_list.keys())> 1:  
            
            # Store the smallest entry and the label in find dictionary 
            minimum = min(min_list.keys())
            # Check if it's not already there
            if list_name[min_list[minimum]] not in dicti.values():
                dicti[list_name[i]] = list_name[min_list[minimum]]
            else:
                min_list.pop(minimum)
                minimum = min(min_list.keys())
                dicti[list_name[i]] = list_name[min_list[minimum]]
              
list_boxname = list(dicti.keys())
list_labelname = list(dicti.values())

new_df = pd.DataFrame(list(zip(list_boxname, list_labelname)),columns = ["Boxname","Labelname"])
new_df.to_csv(New_CSV[File_Number])



   
        
    


