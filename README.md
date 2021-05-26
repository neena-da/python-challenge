# python-challenge - Python Assignment - Data Analytics Bootcamp

## Python Homework - PyBank and PyPoll

### Setting up folders in Github

1. Created a new repository for the project called python-challenge in Github. Cloned the repository to the local computer.

2. Created new directories within python-challenge for PyBank and PyPoll

3. Inside each of the of the 2 new directories, created a main.py file, a folder Resources to hold the csv file and and a folder Analysis to save the output file into.

4. Executed the python scripts for both PyBank and PyPoll

### PyBank

   * Imported the csv and os modules
```
import csv
import os
```
   * Set the path for the CSV file and read the csv file, skipping the header
```
csvpath = os.path.join("Resources","budget_data.csv")
```
```
with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csv_header = next(csvreader)
```

* Read each row in the csv file to calculate the Total months and the Total profit and loss
```
for row in csvreader:                
		total_months += 1
		total_amount += int(row[1])  
```
  * Save the Dates and Difference in Profits/Losses over months in a dictionary. Calculate the average of the changes.
```
	sum_changes = sum(change_dict["Changes"])   
	num_changes = len(change_dict["Changes"])
	average = round((sum_changes / num_changes),2)
```
 * Calculate the greatest increase and decrease in profits / losses along with the months.
```
	maximum = max(change_dict["Changes"])
	minimum = min(change_dict["Changes"])
	index_maximum = (change_dict["Changes"].index(maximum))
	index_minimum = (change_dict["Changes"].index(minimum))
	date_maximum = (change_dict["Date"][index_maximum])
	date_minimum = (change_dict["Date"][index_minimum])
```
* Print desired outout and write it into the output file.
```
	print("Financial Analysis")
	print("-----------------------------")
	print(f"Total months: {total_months}")
	print(f"Total: {currency(total_amount)}")        
	print(f"Average Change: {currency(average)}")    
	print(f"Greatest Increase in Profits: {date_maximum} ({currency(maximum)})")   
	print(f"Greatest Decrease in Profits: {date_minimum}

	output_file = os.path.join("Analysis","pybank_output.txt")
	with open(output_file, 'w') as text:
```

### PyPoll

* Imported the csv and os modules
```
import csv
import os
```
   * Set the path for the CSV file and read the csv file, skipping the header
```
csvpath = os.path.join("Resources","election_data.csv")
```
```
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
```

* Read each row in the csv file to calculate the Total votes and save the candidate records in a list. Store unique values in a set.
```
for row in csvreader:
        vote_count += 1
        candidates.append(row[2])
```
```
	for candidate in candidates:       
    		s.add(candidate)
```
  * Store the unique candidates and total votes in a dictionary
```
	for item in list(s):
    		dict_of_counts[item] = candidates.count(item)
```
```
	sorted_values = sorted((dict_of_counts.values()), reverse = True)
	for sortedkey in sorted_values:
    		for key, value in dict_of_counts.items():
        		if value == sortedkey:
            			sorted_dict[key] = value
```
 * Determine the winner and the votes and percentage for each candidate using lists
```
	winner = max(sorted_dict, key=sorted_dict.get)
```
```
	for item in items:
    		keys.append(item[0]), values.append(item[1])

```
* Print desired outout and write it into the output file.
```
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
```