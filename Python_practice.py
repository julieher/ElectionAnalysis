
# counties = ["Arapahoe","Denver","Jefferson"]

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for key, value in counties_dict.items():
    print(key, value)

# Skill Drill
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in the Election")
    txt_file.write("\n----------\nArapahoe\nDenver\nJefferson")