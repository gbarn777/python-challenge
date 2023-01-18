import os
import csv

#Create path
election_csv = os.path.join("Resources", "election_data.csv")
analysis_txt = os.path.join("analysis", "election_analysis.txt")

#Analysis
print(f"Election Results\n"
  f"----------------------------")

#Set variables
total_votes = 0
candidate_list = []
unique_candidates = []
candidate_name = []
candidate_votes = {}
percentage_votes = 0
#candidate_votes = []
winning_candidate = ""
winner = 0

#Read file
with open(election_csv) as csvfile: 
    csv_reader = csv.reader(csvfile)

    #Skip headers
    header = next(csv_reader)

    for row in csv_reader:

#Count total votes
       total_votes = total_votes + 1
print(f'Total Votes: (len(total_votes))')

#Separate
print(f"----------------------------")

#List candidates
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile)

    #Skip headers
    header = next(csv_reader)

    for row in csv_reader:
        candidate_name = row[2]
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
            #candidate_list.append(row[2])
        candidate_votes[candidate_name] = candidate_votes[candidate_name] 
        for i in set(candidate_list):
            unique_candidates.append(i)

 #Total votes per candidate
        y = candidate_list.count(i)
        candidate_votes.update({candidate_name: candidate_votes})
        #print(candidate_name)
    print(candidate_votes)

#Separate
print(f"----------------------------")

#Sort list
sorted_list = sorted(candidate_votes)
arrange_list = sorted_list

count_candidate = candidate_votes(arrange_list)
candidate_votes.append(count_candidate.most_common())

for item in candidate_votes:
       
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
        fourth = format((item[3][1])*100/(sum(count_candidate.values())),'.3f')