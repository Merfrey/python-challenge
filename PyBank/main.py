import csv
import os
    
csvpath = os.path.join('./resources/budget_data.csv')
#csvoutput = os.path.join('output.txt')
analysis = os.path.join('./analysis/analysis.txt')

    
with open('./resources/budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_headers = next(csvreader)
    totalMonths = 0
    netTotalAmount = 0
    netChangeHolder = []
    averageChange = 0
    months = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_headers = next(csvreader)

    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    totalMonths += 1
    first_row = next(csvreader)
    previous = int(first_row[1])
    netTotalAmount += int(first_row[1])
    for x in csvreader:
        months.append(x[0])
        totalMonths += 1
        netTotalAmount += int(x[1])
        netChange = int(x[1]) - previous
        netChangeHolder.append(netChange)
        previous = int(x[1])
    averageChange = sum(netChangeHolder) / len(netChangeHolder)


with open(analysis, "a") as txtfile:
    txtfile.write(f"Financial Analysis\n"
    f"--------------------\n"
    f"total number of months is : {totalMonths}\n"
    f"net total amount is : ${netTotalAmount}\n"
    f"average change is {str(averageChange)}\n"
    f"greatest increase in profit : {months[netChangeHolder.index(max(netChangeHolder))]} {max(netChangeHolder)}\n"
    f"greates decrease in profit : {months[netChangeHolder.index(min(netChangeHolder))]} {min(netChangeHolder)}")