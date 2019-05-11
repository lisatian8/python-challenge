# Modules
import os
import csv
#import math

# Prompt user for video lookup
#video = input("What show or movie are you looking for? ")

# Lists to store data
candidates = ["Correy", "Khan", "Li", "O'Tooley"]
votes = [0,0,0,0]
percentages=[]

ranking = []

totalVotes = 0
#totalPrfitLoss = 0
maxVote = 0
winner = ""


# Set path for file
csvpath = os.path.join(".", "Resources", "election_data.csv")



# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Loop through looking for the video
    for row in csvreader:

       totalVotes = int(totalVotes) + 1

       votes[int(candidates.index(str(row[2])))] = votes[int(candidates.index(str(row[2])))]  + 1


    ####print(candidates)
    ####print(votes)

    

   #### print(f'Total Votes {totalVotes}')

    for vote in votes:
      ranking.append(vote)
      percentages.append(float((vote/totalVotes)*100))
      if vote > maxVote:
         maxVote = vote
    
    winner = candidates[votes.index(maxVote)]
    ####print(f'{maxVote}')
    #ranking.append(str(winner)
    ####print(f'{winner}')
    ####print(percentages)
    ####print(ranking)
    #sort votes in decending
    ####ranking.sort(reverse = True)
    ####print(ranking)

print("Election Results")
print("------------------------")
print(f'Total Votes: {totalVotes}')
print("------------------------")
####print(ranking)
for rank in ranking:
  print(f'{candidates[int(votes.index(rank))]}:  {round(percentages[int(votes.index(rank))], 3)}%  ({rank})')
print("------------------------")
print(f'Winner: {winner}')
print("------------------------")


