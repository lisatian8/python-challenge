# Modules
import os
import csv
#import math

# Prompt user for video lookup
#video = input("What show or movie are you looking for? ")

# Lists to store data
dates = []
profitLosses = []

totalNumOfMonths = 0
totalPrfitLoss = 0
maxLoss = 0
maxLossDate = ""
maxProfit = 0
maxProfitDate = ""
totalLoss = 0
averageChange = 0


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
    #print(f"CSV Header: {csv_header}")

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

        totalPrfitLoss = float(totalPrfitLoss) + float(row[1])

        #if float(row[1]) > 0 && float(row[1]) > float(maxProfit):
        if float(row[1]) > float(maxProfit):
            maxProfit = float(row[1])
            maxProfitDate = str(row[0])

        elif float(row[1]) < float(maxLoss):
            maxLoss = float(row[1])
            maxLossDate = str(row[0])
            totalLoss = totalLoss + float(row[1])

    #print(dates)
    #print(profitLosses)
    #print(f"{len(dates)}")

    totalNumOfMonths=len(dates)
    averageChange = float(totalPrfitLoss)/float(totalNumOfMonths)
    #averageChange = float(totalLoss)/float(totalNumOfMonths)
    

    print(f'Total Months: {int(totalNumOfMonths)}')
    print(f'Total: ${int(totalPrfitLoss)}')
    print(f'Average Change: ${int(averageChange)}')
    # print(f'{float(totalLoss)}')
    print(f'Great Increase in Profits: {str(maxProfitDate)} (${float(maxProfit)})')

    #print(f'{float(maxProfit)}')
    print(f'Greatest Decrease in Profits: {str(maxLossDate)} (${float(maxLoss)})')
    #print(f'{float(maxLoss)}')



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