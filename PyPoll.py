# Data we need to retrieve
import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Vote counter = 0
total_votes = 0
# Candiate's Names
candidate_options = [] 
# Empty dictionary. To count each candidate's votes
candidate_votes = {} 

wining_candidate = ""
wining_count = 0
wining_percentage =0 

# Open and read election_results
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data) 
    headers = next(file_reader)

    # For Loop that will print each row in the CSV file
    for row in file_reader:
        total_votes += 1
       
        # This will iterate through rows to get the candidate's names
        candidate_name = row[2]

        # If statement: If candidate not in options then print
        if candidate_name not in candidate_options:
            # Add names to the list that will be printed
            candidate_options.append(candidate_name)
            # This will track the count for each name
            candidate_votes[candidate_name] = 0
        # This will add one vote to each name
        candidate_votes[candidate_name] += 1

print("------")
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes/total_votes) * 100
    
    if (votes > wining_count) and (vote_percentage > wining_percentage):
            wining_count = votes
            wining_percentage = vote_percentage
            wining_candidate = candidate_name
    
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes})\n")
    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the total votes.")

wining_candidate_summary = (f"------\n"
                            f"Winner: {wining_candidate}\n"
                            f"Winning Vote Count: {wining_count:,}\n"
                            f"Winning Percentage: {wining_percentage:.1f}%\n"
                            f"------\n")
print(wining_candidate_summary)


'''
print("Total Votes:", total_votes)
print("Candidates:", candidate_options)   
print("Each", candidate_votes)
'''



















# 1. Total number of votes cast (Open the data file)

# 2. Complete list of candidates who received votes (Names of all candidates)

# 3. Percentage of votes each candidate won (Vote count for each candidate)

# 4. Total number of votes each candidate wom (total votes for each candidate)

# 5. The winner of the election based on popular vote (total votes cast for the election)


