import os
import csv


csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

Months = []
Profit = []
ProfitChangeMonthly = []

with open(csvpath, newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for row in csvreader: 
        
        Months.append(row[0])
        Profit.append(int(row[1]))

    for i in range(len(Profit)-1):
        
        ProfitChangeMonthly.append(Profit[i+1]-Profit[i])

MaxIncreaseProfits = max(ProfitChangeMonthly)
MaxDecreaseProfits = min(ProfitChangeMonthly)

MaxIncreaseMonth = ProfitChangeMonthly.index(MaxIncreaseProfits) + 1
MaxDecreaseMonth = ProfitChangeMonthly.index(MaxDecreaseProfits) + 1 

print("Financial Analysis")#import budget data 
import os
import csv 
#working directory

csvpath=os.path.join('..','Resources','budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []
    
    print(f"Header: {csv_header}")               


    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    print(len(month))

    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    print(total_revenue)


    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])

        revenue_change.append(profit_loss)
    Total = sum(revenue_change)

    monthly_change = Total / len(revenue_change)
    print(monthly_change)

    
    profit_increase = max(revenue_change)
    print(profit_increase)
    k = revenue_change.index(profit_increase)
    month_increase = month[k+1]
    

    profit_decrease = min(revenue_change)
    print(profit_decrease)
    j = revenue_change.index(profit_decrease)
    month_decrease = month[j+1]




print(f'Financial Analysis'+'\n')
print(f'----------------------------'+'\n')


print("Total number of months: " + str(len(month)))

print("Total Revenue in period: $ " + str(total_revenue))
      
print("Average monthly change in Revenue : $" + str(monthly_change))

print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")

print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")
print("----------------------------")
print(f"Total Months: {len(Months)}")
print(f"Total: ${sum(Profit)}")
print(f"Average Change: {round(sum(ProfitChangeMonthly)/len(ProfitChangeMonthly),2)}")
print(f"Greatest Increase in Profits: {Months[MaxIncreaseMonth]} (${(str(MaxIncreaseProfits))})")
print(f"Greatest Decrease in Profits: {Months[MaxDecreaseMonth]} (${(str(MaxDecreaseProfits))})")

output_file = os.path.join("output.csv")

with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.write(print("Financial Analysis"))
    writer.write(print("----------------------------"))
    writer.write((f"Total Months: {len(Months)}"))
    writer.write((f"Total: ${sum(Profit)}"))
    writer.write((f"Average Change: {round(sum(ProfitChangeMonthly)/len(ProfitChangeMonthly),2)}"))
    writer.write((f"Greatest Increase in Profits: {Months[MaxIncreaseMonth]} (${(str(MaxIncreaseProfits))})"))
    writer.write((f"Greatest Decrease in Profits: {Months[MaxDecreaseMonth]} (${(str(MaxDecreaseProfits))})"))
