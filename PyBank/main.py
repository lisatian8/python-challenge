# Modules
import os
import csv

# Prompt user for video lookup
#video = input("What show or movie are you looking for? ")

# Lists to store data
dates = []
profitLosses = []

totalNumOfMonths = 0
totalPrfitLost = 0
maxLoss = 0
maxProfit = 0

# Set path for file
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# Bonus
# ------------------------------------------
# Set variable to check if we found the video
#found = False

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Loop through looking for the video
    for row in csvreader:

        dates.append(str(row[0]))
       # print("here")
        #print(str(row[0]))
        ####print(f'date: {row[0]}')

        profitLosses.append(float(row[1]))
       # print("here")
        #print(str(row[0]))
        ####print(f'profigLosses: {row[1]}')

    print(dates)
    print(profitLosses)
    print(f"{len(dates)}")

    totalNumOfMonths=len(dates)
    print(f'{totalNumOfMonths}')



        #print(row[0])
        #if row[0] == video:
          #  print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])

            # BONUS: Set variable to confirm we have found the video
          #  found = True

            # BONUS: Stop at first results to avoid duplicates
           # break

    # If the video is never found, alert the user
    #if found is False:
       # print("Sorry about this, we don't seem to have what you are looking for!")