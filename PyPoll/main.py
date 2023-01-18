import os
import csv
#Create path
election_csv = os.path.join("Resources", "election_data.csv")
#Analysis
print(f"Election Results\n"
  f"----------------------------")
#Set variables
total_votes = []
candidate_list = []
unique_candidates = []
candidate_name = []
candidate_votes = {}
percentage_votes = 0
#candidate_votes = []
winner = 0
#Read file
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
#Count total votes
        total_votes.append(row[1])
print(f'Total Votes: {len(total_votes)}')
#Separate
print(f"----------------------------")
#List candidates
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        candidate_name = row[2]
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
            #candidate_list.append(row[2])
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        #for i in set(candidate_list):
            
            #unique_candidates.append(i)
            
        # Total votes per candidate
            #y = candidate_list.count(i)
            #candidate_votes.append(y)
        #print(candidate_name)
    print(candidate_votes)

