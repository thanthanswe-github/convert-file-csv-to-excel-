# ===== Question 1.2

# Coordinate values ​​and tags are recorded in the CSV in the following folder.

#   - Folder : gw_test/Question1/Dataset

# The format of each line in each CSV file is as follows.

#   - Format : [ x(float), y(float), width(float), height(float), tag(string) ]

# Write a program to convert all CSV to JSON format.
# Write a program that meets the following specifications.

#   - The file name of the program is "question_1_2.py".
#   - Output 1 JSON file per 1 CSV.
#   - Generate the JSON file in the same folder as the CSV file.
#   - Create a JSON file name according to the following example.
#     File Name Example:
#     ------------------------------------------------------------
#       src: gw_test/Question1/Dataset/12163257_B_004_00001.csv
#       dst: gw_test/Question1/Dataset/12163257_B_004_00001.json
#     ------------------------------------------------------------
#   - Refer to the sample below for the format of the JSON file.
#     JSON File Example: gw_test/Question1/Dataset/12163257_B_004_00001.json



import csv
import pandas as pd 
import numpy as np 
import json
from collections import OrderedDict
import os


# folder location : gw_test/Question1/Dataset

dirName_path = "gw_test/Question1/Dataset"

colnames=['x', 'y', 'width', 'height','tag'] 

#create an empty list in a listOfFiles
listOfFiles =list()

#Get a list of csv files in directory and sub directory using os.walk()
for (dirpath,dirname,filenames) in os.walk(dirName_path):

    listOfFiles = [os.path.join(dirpath, file) for file in filenames]

    for file in range(len(listOfFiles)):

        if listOfFiles[file].endswith(".csv"):

            csvFiles = listOfFiles[file]

            # Given column labels and set  of a specific data type when read csv files in  pandas 

            csv_file = pd.read_csv(csvFiles, names =colnames ,dtype={'x':'float','y':'float','width':'float','height':'float','tag':'string'})

            json_create = csvFiles.split('.')


            json_file = json_create[0]+'.json'

            for index_count, row in csv_file.iterrows():
                
                new_add = csv_file.rename(index = lambda index_count : 'record_0'+str(index_count+1) if ((index_count+1)<10) else 'record_'+str(index_count+1))

                
                new_json_file = new_add.to_json(json_file,orient='index',indent=3)
