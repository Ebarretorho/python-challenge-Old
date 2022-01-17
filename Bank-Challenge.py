#Import modules

import os
import csv
from statistics import mean
from tkinter.tix import INTEGER

#Define file path

budget_data_path = os.path.join("Resources","budget_data.csv")

#Set Data storage

report_month = []
results = []
MoM_change = []

# Variables
last_month_results = 867884

with open(budget_data_path,'r') as budgetfile:
    budget_data = csv.reader(budgetfile,delimiter=',')

    header = next(budget_data)

    for row in budget_data:

        report_month.append(row[0])
        results.append(int(row[1]))

        
        MoM_change.append(int(row[1]) - int(last_month_results))

        #Change Last month variable

        last_month_results = row[1]

    
number_of_months = len(report_month)
average_change = int(sum(MoM_change))/(int(number_of_months)-1)
highest_month = int(max(MoM_change))
lowest_month = int(min(MoM_change))
total = int(sum(results))


#Zipping the lists together to loop through and find the variables

#new_data = zip(report_month,results,MoM_change)

#new_data_2 = list(new_data)

print(f"Total months: {number_of_months}")
print(f"Total: {total}")
print(f"Average Change: {average_change}")
print(f"The greatest increase: {highest_month}")
print(f"Greatest Decrease: {lowest_month}")

