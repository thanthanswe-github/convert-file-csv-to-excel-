
# ===== Question 1.1

# Create a program that outputs the number of all CSV files stored in the following folder.

#   - Folder : gw_test/Question1/Dataset

# Write a program that meets the following specifications.

#   - The file name of the program is "question_1_1.py".
#   - Output the result to standard output according to the following output example.
#     Output Example: ( "?" is a number )
#     ------------------------------------------------
#       CSV File Count: ?? files
#     ------------------------------------------------

import os, os.path


# Given Folder Path : gw_test/Question1/Dataset 


dirName_path = "gw_test/Question1/Dataset"


#Assigned number of csv file count is zero
num_of_csv_count =0


#create an empty list in a listOfFiles
listOfFiles =list()

#Get a list of csv files in directory and sub directory using os.walk()
for (dirpath,dirname,filenames) in os.walk(dirName_path):

	listOfFiles = [os.path.join(dirpath, file) for file in filenames]

	for file in range(len(listOfFiles)):

		if listOfFiles[file].endswith(".csv"):

			num_of_csv_count +=1


## Display all csv files 
print("CSV File Count : ",num_of_csv_count ,"files")



