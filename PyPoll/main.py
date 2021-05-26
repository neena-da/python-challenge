# PyPoll Assignment
# Import modules os and csv
import csv
import os

# Set the path for the CSV file in csvpath
csvpath = os.path.join("Resources","election_data.csv")

# Create lists, dictionaries and variables to store data and initialize
vote_count = 0
i = 0
s = set()
candidates = []
dict_of_counts = {}
sorted_dict = {}

# Read the csv file and skip / store the header in variable csv_header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# Read each row of the csvfile and count the total votes 
    for row in csvreader:
        vote_count += 1
        candidates.append(row[2])  # Create a list of the candidates for each row

for candidate in candidates:       # Get unique values from the candidate list to a Set
    s.add(candidate)

# Store the unique sorted candidates (Key) and Votes count (Value) in a dictionary
for item in list(s):
    dict_of_counts[item] = candidates.count(item)

# Sort the dictionary in descending order of the vote counts
sorted_values = sorted((dict_of_counts.values()), reverse = True)
for sortedkey in sorted_values:
    for key, value in dict_of_counts.items():
        if value == sortedkey:
            sorted_dict[key] = value

# Determine the winner based on the maximum amount of value in the dictionary(Votes)
winner = max(sorted_dict, key=sorted_dict.get)

keys = []       # List to store keys in dictionary
values = []     # List to store values in dictionary
items = sorted_dict.items()

# Store the dictionary in 2 lists
for item in items:
    keys.append(item[0]), values.append(item[1])

# Function to format the percent in final output
def percent(amount):
    return ("{:.3%}".format((amount/vote_count)))

# Print final output # Calling function to format into percent
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {vote_count}")
print("-----------------------------")
for i in range(len(keys)):
    print(f"{keys[i]} : {percent(values[i])}  ({values[i]})")
print("-----------------------------")
print(f"Winner: {winner}")
print("-----------------------------")

# Set path for the output text file
output_file = os.path.join("Analysis","pypoll_output.txt")

# Write the output into the output text file
with open(output_file, 'w') as text:
    text.write("Election Results")
    text.write("\n")
    text.write("-----------------------------")
    text.write("\n")
    text.write(f"Total Votes: {vote_count}")
    text.write("\n")
    text.write("-----------------------------")
    text.write("\n")
    for i in range(len(keys)):
        text.write(f"{keys[i]} : {percent(values[i])}  ({values[i]})")
        text.write("\n")
    text.write("-----------------------------")
    text.write("\n")
    text.write(f"Winner: {winner}")
    text.write("\n")
    text.write("-----------------------------")