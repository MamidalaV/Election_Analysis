#Retreive data
import csv
import os

#assign file path to a variable
file_to_load = os.path.join('..','resources', 'election_results.csv')

#create a filename variable to direct or indiret path to the file.
file_to_save = os.path.join('..','analysis',"election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

#1. A total number of votes cast
#2. List of candidate names who received votes
#3. percentage of votes
#4. Total votes each candiate received
#5. The winner