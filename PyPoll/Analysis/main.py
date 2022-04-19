#You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

  #The total number of votes cast

  #A complete list of candidates who received votes

  #The percentage of votes each candidate won

  #The total number of votes each candidate won

  #The winner of the election based on popular vote.

#As an example, your analysis should look similar to the one below:

  #`text
  #Election Results
  #-------------------------
  #Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
 # Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
 # -------------------------
 # Winner: Khan
  #-------------------------
  #```

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import math
import csv
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

votes = []
unique_candidates = []

with open(csvpath) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  # print(csvreader)
  next(csvreader)
  for row in csvreader:
    votes.append(row[0])
    unique_candidates.append(row[2])

print("Total votes: " + str(len(votes)))

def unique(row[2]):
 
    # initialize a null list
    unique_candidate = []
     
    # traverse for all elements
    for candidate in row[2]:
        # check if exists in unique_list or not
        if candidate not in unique_candidate:
            unique_candidate.append(candidate)
    # print list
    for candidate in unique_candidate:
        print("Candidates in the race included: "+ (candidate))





