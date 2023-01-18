#Import dependencies
import os
import csv

#Create path
budget_csv = os.path.join("Resources", "budget_data.csv")

#Analysis
print(f"Financial Analysis\n"
  f"----------------------------")

#Set variables
total_months = []
total_profits = []
profit_changes = 0
monthly_changes = []
previous_value = 0

#Read file
with open(budget_csv) as csvfile: 
    csv_reader = csv.reader(csvfile)

    #Skip headers
    header = next(csv_reader)

    for row in csv_reader:

#Total months and Profits/Losses
        total_months.append(row[0])
        total_profits.append(row[1])

    print(f'Total Months: {len(total_months)}')

#Net total amounts of Profits/Losses over time

    total_profits_conv = [int(x)for x in total_profits]
    total_profits=(sum(total_profits_conv))
    print(f'Total Profits: (${total_profits})')

#Changes in "Profit/Losses over the entire period"

for i in total_profits_conv:
    monthly_change = i - previous_value
    monthly_changes.append(monthly_change)
    previous_value = i
# print(monthly_changes)

#Average of changes

monthly_changes.pop(0)
avg = sum(monthly_changes)/85
print(f'Average Change: (${avg})')

#Greatest increase and greatest decrease in Profits

greatest_increase = max(monthly_changes)
greatest_date = total_months[monthly_changes.index(greatest_increase)+1]
print(f'Greatest Increase: {greatest_date} (${greatest_increase})')
greatest_decrease = min(monthly_changes) 
smallest_date = total_months[monthly_changes.index(greatest_decrease)+1]
print(f'Greatest Decrease: {smallest_date} & (${greatest_decrease})')


