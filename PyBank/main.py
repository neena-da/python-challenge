# PyBank Assignment
# Import modules os and csv
import csv
import os

# Set the path for the CSV file in csvpath
csvpath = os.path.join("Resources","budget_data.csv")

# Create lists to store data and initialize
total_months = 0
total_amount = 0
firstline = True
change_dict = {"Date": [], "Changes": []}

# Function to format amount to $ in the final output
def currency(amount):
    return ("${}".format(amount))

# Read the csv file and skip / store the header in variable csv_header
with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csv_header = next(csvreader)

	for row in csvreader:                 # read each row in csv file to calcualte the total months
		total_months += 1
		total_amount += int(row[1])       # calculate the total profit/loss  

		if firstline:                     # skip first line while calculating the average change
			firstline = False
			old_value = int(row[1])
		else:
			current_value = int(row[1])   # from 2nd row, calculate the difference in profits/loss 
			change_dict["Date"].append(row[0])   # save in a dictionary with dates and difference as keys
			change_dict["Changes"].append((current_value)-(old_value))
			old_value = current_value

sum_changes = sum(change_dict["Changes"])   
num_changes = len(change_dict["Changes"])
average = round((sum_changes / num_changes),2) # find the average of the change in profit/loss using dictionary

# find the greatest increase and decrease in Profits from dictionary. Also find the corressponding dates using index
maximum = max(change_dict["Changes"])
minimum = min(change_dict["Changes"])
index_maximum = (change_dict["Changes"].index(maximum))
index_minimum = (change_dict["Changes"].index(minimum))
date_maximum = (change_dict["Date"][index_maximum])
date_minimum = (change_dict["Date"][index_minimum])

# Display the output to show the total months, amount, average change, greatest increase and decrease in profit
print("Financial Analysis")
print("-----------------------------")
print(f"Total months: {total_months}")
print(f"Total: {currency(total_amount)}")       # calling function to format currency
print(f"Average Change: {currency(average)}")   # calling function to format currency
print(f"Greatest Increase in Profits: {date_maximum} ({currency(maximum)})")  # calling function to format currency
print(f"Greatest Decrease in Profits: {date_minimum} ({currency(minimum)})")  # calling function to format currency

# Set path for the output text file
output_file = os.path.join("Analysis","pybank_output.txt")

# Write the output into the output text file
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