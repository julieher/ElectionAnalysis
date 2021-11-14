# Data we need to retrieve
import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Vote counter = 0
total_votes = 0
# Step 1: Candiate's Names 
candidate_options = [] 
candidate_votes = {} 

# County list 
county_options = []
county_votes = {}

wining_candidate = ""
wining_count = 0
wining_percentage =0 

# Step 2: To calc largest county turnout
county_largest_turnout = ""
county_largest_turnout = 0


# Open and read election_results
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data) 
    headers = next(file_reader)

    # For Loop that will print each row in the CSV file
    for row in file_reader:
        total_votes += 1
       
        # This will iterate through rows to get the candidate's names
        candidate_name = row[2]
        # Step 3: county name from each row
        county_name = row[1]

        # If statement: If candidate not in options then print
        if candidate_name not in candidate_options:
            # Add names to the list that will be printed
            candidate_options.append(candidate_name)
            # This will track the count for each name
            candidate_votes[candidate_name] = 0
        # This will add one vote to each name
        candidate_votes[candidate_name] += 1

        
        # Step 4a: if county name is in list
        if county_name not in county_options:
            # Step 4b: if not, add county to list
            county_options.append(county_name)
            # Step 4c: county vote to zero
            county_votes[county_name] = 0
        # Step 5: adds a vote to the county’s vote count   
        county_votes[county_name] += 1
        

# Write results to a txt file         
with open(file_to_save, "w") as txt_file:
    election_results = (f"\nElection Results\n"
                        f"-------------------------------------\n"
                        f"Total Votes: {total_votes:,}\n"
                        f"-------------------------------------\n"
                        f"County Votes:\n")

    print(election_results, end="")
    txt_file.write(election_results)


    # Step 6a: repetition statement to get the county from the county dictionary
    for county_name in county_options:
        var_votes = county_votes.get(county_name)
        county_votes_percent = float(var_votes/total_votes) * 100

        county_votes_results = (f"{county_name}: {county_votes_percent:.1f}% ({var_votes:,})\n")
        print(county_votes_results)
        txt_file.write(county_votes_results)

        if (var_votes > county_largest_turnout):
            county_largest_turnout = var_votes
            largest_county = county_name

    # Step 7:
    largest_county_summary = (
                            f"-------------------------------------\n"
                            f"Largest County Turnout: {largest_county}\n"
                            f"-------------------------------------\n")
    print(largest_county_summary)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes/total_votes) * 100
        
        if (votes > wining_count) and (vote_percentage > wining_percentage):
                wining_count = votes
                wining_percentage = vote_percentage
                wining_candidate = candidate_name

        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the total votes.")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        

    wining_candidate_summary = (
                                f"-------------------------------------\n"
                                f"Winner: {wining_candidate}\n"
                                f"Winning Vote Count: {wining_count:,}\n"
                                f"Winning Percentage: {wining_percentage:.1f}%\n"
                                f"-------------------------------------\n")
    print(wining_candidate_summary)                            
    txt_file.write(wining_candidate_summary)


    '''
    print("Total Votes:", total_votes)
    print("Candidates:", candidate_options)   
    print("Each", candidate_votes)
'''