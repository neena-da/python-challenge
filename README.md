# python-challenge - Python Assignment - Data Analytics Bootcamp

## Python Homework - PyBank and PyPoll

### Setting up folders in Github

1. Created a new repository for the project called python-challenge in Github. Cloned the repository to the local computer.

2. Created new directories within python challenge for PyBank and PyPoll

3. Inside each of the of the 2 new directories, created a main.py file, a folder Resources to hold the csv file and and a folder Analysis to save the output file into.

4. Pushed the updated to github main

### PyBank

   * Imported the csv and os modules
```
import csv
import os
```
   * Set the path for the CSV file
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
  * Set the path for the CSV file
```
csvpath = os.path.join("Resources","budget_data.csv")
```Save the Dates and the Change in