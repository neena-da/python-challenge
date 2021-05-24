# PyBank Assignment
# Importing modules os and csv
import csv
import os

# Setting the path for the CSV file in csvpath
csvpath = os.path.join("Resources","budget_data.csv")

# Creating lists to store data and initializing
total_months = 0
total_amount = 0
firstline = True
change_dict = {"Date": [], "Changes": []}

def currency(amount):
    return ("${}".format(amount))

with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csv_header = next(csvreader)

	for row in csvreader:
		total_months += 1
		total_amount += int(row[1])

		if firstline: # skip first line
			firstline = False
			old_value = int(row[1])
		else:
			current_value = int(row[1])
			change_dict["Date"].append(row[0])
			change_dict["Changes"].append((current_value)-(old_value))
			old_value = current_value

sum_changes = sum(change_dict["Changes"])
num_changes = len(change_dict["Changes"])
average = round((sum_changes / num_changes),2) 

maximum = max(change_dict["Changes"])
minimum = min(change_dict["Changes"])
index_maximum = (change_dict["Changes"].index(maximum))
index_minimum = (change_dict["Changes"].index(minimum))
date_maximum = (change_dict["Date"][index_maximum])
date_minimum = (change_dict["Date"][index_minimum])

print("Financial Analysis")
print("-----------------------------")
print(f"Total months: {total_months}")
print(f"Total: {currency(total_amount)}")
print(f"Average Change: {currency(average)}")
print(f"Greatest Increase in Profits: {date_maximum} ({currency(maximum)})")
print(f"Greatest Decrease in Profits: {date_minimum} ({currency(minimum)})")

output_file = os.path.join("Analysis","pybank_output.txt")

with open(output_file, 'w') as text:
    text.write("Financial Analysis")
    text.write("\n")
    text.write("-----------------------------")
    text.write("\n")
    text.write(f"Total months: {total_months}")
    text.write("\n")
    text.write(f"Total: {currency(total_amount)}")
    text.write("\n")
    text.write(f"Average Change: {currency(average)}")
    text.write("\n")
    text.write(f"Greatest Increase in Profits: {date_maximum} ({currency(maximum)})")
    text.write("\n")
    text.write(f"Greatest Decrease in Profits: {date_minimum} ({currency(minimum)})")