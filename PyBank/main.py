import csv
from pathlib import Path

#C:\Users\aMysllinj\Desktop\python-challenge\PyBank\Recources

#input/output

input_file=Path("recources/budget_data.csv")
output_file=Path("analysis/results_PyBank.txt")

with open(input_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    data = list(csvreader)


#set variables

total_revenue = 0
greatest_increase = 0
greatest_increase_mo = ""
greatest_decrease = 0
greatest_decrease_mo = ""
previous_revenue = 0
change =[]


# looping thru all the data

for row in data:
    date = row[0]
    revenue = int(row[1])

#net total amount of Profit/Loss
    total_revenue += revenue
    change.append(int(row[1])- previous_revenue)
    previous_revenue = revenue


 #total number of months
months = len(data)

print(months)
print(total_revenue)



# Changes in Profit/Loss for the entire perios
average = (int(data[-1][1]) - int(data[0][1])) / (months -1)
print(average)

# greatest increase in profit for the entire period
  
      
for n in range(1, len(change)):
        

    if change[n] > greatest_increase:
        greatest_increase = change[n]
        greatest_increase_mo = data[n][0]
                     
    if change[n] < greatest_decrease:
        greatest_decrease = change[n]
        greatest_decrease_mo = data[n][0]

print(f'{greatest_increase_mo}, {greatest_increase},{greatest_decrease},{greatest_decrease_mo}')
    



with open("Analysis/Pybank.txt", 'w') as file_PythonChallenge:
     file_PythonChallenge.write(f"""Financial_Analysis
----------------------------------
total_months: {months}
total: {total_revenue}
avg_change: {round(average,2)}
greatest_increase: {greatest_increase_mo}  ($ {greatest_increase})
greatest_decrease: {greatest_decrease_mo}  ($ {greatest_decrease})
     """)



