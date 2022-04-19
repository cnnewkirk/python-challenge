#Your task is to create a Python script that analyzes the records to calculate each of the following:

  #The total number of months included in the dataset

  #The net total amount of "Profit/Losses" over the entire period

  #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

  #The greatest increase in profits (date and amount) over the entire period

  #The greatest decrease in profits (date and amount) over the entire period

#As an example, your analysis should look similar to the one below:

  #text
  #Financial Analysis
  #----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
  #```

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import math
import csv
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

months = []
prev_net = []

with open(csvpath) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  # print(csvreader)
  next(csvreader)
  for row in csvreader:
    months.append(row[0])


net = int(row[1]) - (prev_net)
prev_net = int(row[1])
average_change = sum(net) / str(len(months))
greatest_increase = net.max
greatest_loss = net.min

print("Total months: " + str(len(months)))
print("Net total profit loss: " + str(profit_loss))
print("Mean net: " + str(net))
print("Greatest increase: " + str(greatest_increase))
print("Greatest loss: " + str(greatest_loss))
