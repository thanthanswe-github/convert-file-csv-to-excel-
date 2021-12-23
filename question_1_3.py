
# ===== Question 1.3

# Coordinate values ​​and tags are recorded in the CSV in the following folder.

#   - Folder : gw_test/Question1/Dataset

# The format of each line in each CSV file is as follows.

#   - Format : [ x(float), y(float), width(float), height(float), tag(string) ]

# Write a program to convert all CSV to XML format.
# Write a program that meets the following specifications.

#   - The file name of the program is "question_1_3.py".
#   - Output 1 XML file per 1 CSV.
#   - Generate the XML file in the same folder as the CSV file.
#   - Create a XML file name according to the following example.
#     File Name Example:
#     ------------------------------------------------------------
#       src: gw_test/Question1/Dataset/12163257_B_004_00001.csv
#       dst: gw_test/Question1/Dataset/12163257_B_004_00001.xml
#     ------------------------------------------------------------
#   - Refer to the sample below for the format of the XML file.
#     XML File Example: gw_test/Question1/Dataset/12163257_B_004_00001.xml

import csv
import pandas as pd 
import os



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
            
            #Before creating an xml file, csv file must include column names so that I created an updated csv file that is included columns with specific data type

            csv_file.to_csv('edit_file.csv',mode = 'w', index=False)

            csvFile = 'edit_file.csv'

            xml_create = csvFiles.split('.')

            xmlFile = xml_create[0]+'.xml'

            csvData = csv.reader(open(csvFile))
            xmlData = open(xmlFile, 'w')
            xmlData.write('<annotation>' + "\n")
            rowNum = 0
            count=0
            for row in csvData:
                if rowNum == 0:
                    tags = row
                    for i in range(len(tags)):
                        tags[i] = tags[i]
                else: 
                    for i in range(len(tags)):
                        xmlData.write('\t<object>' + "\n")
                        count = len(tags)-1
                        xmlData.write('\t\t' + '<' + tags[count] + '>' \
                                      + row[count] + '</' + tags[count] + '>' + "\n")
                        xmlData.write('\t\t<bndbox>' + "\n")
                        for j in range(len(tags)-1):
                            xmlData.write('\t\t\t' + '<' + tags[j] + '>' \
                                          + row[j] + '</' + tags[j] + '>' + "\n")
                        xmlData.write('\t\t</bndbox>' + "\n")
                        xmlData.write('\t</object>' + "\n")
                            
                rowNum +=1
            xmlData.write('</annotation>' + "\n")
            xmlData.close()

#finally , I deleted an updated csv file 
os.remove('edit_file.csv')
print('Remove')