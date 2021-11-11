# Data we need to retrieve
import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
   
    '''for row in file_reader:
        print(row)'''
        
    headers = next(file_reader)
    print(headers)

# 1. Total number of votes cast (Open the data file)

# 2. Complete list of candidates who received votes (Names of all candidates)

# 3. Percentage of votes each candidate won (Vote count for each candidate)

# 4. Total number of votes each candidate wom (total votes for each candidate)

# 5. The winner of the election based on popular vote (total votes cast for the election)


