# import modules
import os
import csv

# Set path for file
csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

# Create empty lists
Months = []
Profit = []
ProfitChangeMonthly = []

# Open the CSV
with open(csvpath, newline="") as csvfile:
    
    # store CSV file in variable
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header row
    next(csvreader)

    # iterate through rows in CSV file
    for row in csvreader: 
        
        # add each month and profit to empty lists previously made
        Months.append(row[0])
        Profit.append(int(row[1]))


    # iterate through profit list 
    for i in range(len(Profit)-1):
        
        # find monthly change and add to profit change list
        ProfitChangeMonthly.append(Profit[i+1]-Profit[i])
        
# store largest increase and decrease in variable
MaxIncreaseProfits = max(ProfitChangeMonthly)
MaxDecreaseProfits = min(ProfitChangeMonthly)

# Pair max increase and decrease with corresponding month
MaxIncreaseMonth = ProfitChangeMonthly.index(MaxIncreaseProfits) + 1
MaxDecreaseMonth = ProfitChangeMonthly.index(MaxDecreaseProfits) + 1 

# Print 
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(Months)}")
print(f"Total: ${sum(Profit)}")
print(f"Average Change: {round(sum(ProfitChangeMonthly)/len(ProfitChangeMonthly),2)}")
print(f"Greatest Increase in Profits: {Months[MaxIncreaseMonth]} (${(str(MaxIncreaseProfits))})")
print(f"Greatest Decrease in Profits: {Months[MaxDecreaseMonth]} (${(str(MaxDecreaseProfits))})")

# set path for output file
output_file = os.path.join("output.csv")

# open the output file, 
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.write(print("Financial Analysis"))
    writer.write(print("----------------------------"))
    writer.write((f"Total Months: {len(Months)}"))
    writer.write((f"Total: ${sum(Profit)}"))
    writer.write((f"Average Change: {round(sum(ProfitChangeMonthly)/len(ProfitChangeMonthly),2)}"))
    writer.write((f"Greatest Increase in Profits: {Months[MaxIncreaseMonth]} (${(str(MaxIncreaseProfits))})"))
    writer.write((f"Greatest Decrease in Profits: {Months[MaxDecreaseMonth]} (${(str(MaxDecreaseProfits))})"))
