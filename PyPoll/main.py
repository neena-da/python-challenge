import csv
import os

csvpath = os.path.join("Resources","election_data.csv")

vote_count = 0
count = 1
candidates_votes = 0
candidates = []
unique = []
s = set()
i = 0
y = 0
candidate_list = []
count_list = []
set_list = []
sum_candidate = 0
dict_of_counts = {}
sorted_dict = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        vote_count += 1
        candidates.append(row[2])

for candidate in candidates:
    s.add(candidate)

set_length = 0

set_list = sorted(list(s))

for item in set_list:
    dict_of_counts[item] = candidates.count(item)
    
print(dict_of_counts)
sorted_values = sorted((dict_of_counts.values()), reverse = True)
for sortedkey in sorted_values:
    for key, value in dict_of_counts.items():
        if value == sortedkey:
            sorted_dict[key] = value

winner = max(sorted_dict, key=sorted_dict.get)
print(sorted_dict)

keys = []
values = []
items = sorted_dict.items()

for item in items:
    keys.append(item[0]), values.append(item[1])
print ("keys : ", str(keys))
print ("values : ", str(values))
print(len(keys))

def percent(amount):
    return ("{:.3%}".format((amount/vote_count)))


print("Election Results")
print("-----------------------------")
print(f"Total Votes: {vote_count}")
print("-----------------------------")
for i in range(len(keys)):
    print(f"{keys[i]} : {percent(values[i])}  ({values[i]})")
print("-----------------------------")
print(f"Winner : {winner}")
print("-----------------------------")

output_file = os.path.join("Analysis","pypoll_output.txt")

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
    text.write(f"Winner : {winner}")
    text.write("\n")
    text.write("-----------------------------")