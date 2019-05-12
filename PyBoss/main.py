# Modules
import os
import csv
#import math

# Prompt user for video lookup
#video = input("What show or movie are you looking for? ")

# Lists to store data
empIDs = []
firstNames = []
lastNames = []
DOBs = []
states = []
stateAbbrs = []


maxLossDate = ""
maxGain = 0
maxGainDate = ""
totalLoss = 0
averageChange = 0
totalChanges = 0
count = 0
currentChange = 0


# Set path for file
csvpath = os.path.join(".", "Resources", "employee_data.csv")

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


        if count <= 0:
             count = int(count) +1
        else:     
            currentChange = float(row[1]) - float(profitLosses[int(count)-1])    
            totalChanges = float(totalChanges) + float(row[1]) - float(profitLosses[int(count)-1])
            changes.append(currentChange)

            if float(currentChange) > float(maxGain):
                 maxGain = float(currentChange)
                 maxGainDate = str(row[0])

            elif float(currentChange) < float(maxLoss):
                  maxLoss = float(currentChange)
                  maxLossDate = str(row[0])
                  totalLoss = totalLoss + float(row[1])
            
            count = int(count) + 1
             


    #print(dates)
    #print(profitLosses)
    #print(f"{len(dates)}")
    ####print(f'{totalChanges}')

    totalNumOfMonths=len(dates)
    #averageChange = float(totalChanges/float(len(totalChanges)))
    #averageChange = float(totalLoss)/float(totalNumOfMonths)
    averageChange = float(totalChanges)/float(totalNumOfMonths -1)
    
    #### print on terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {int(totalNumOfMonths)}')
    print(f'Total: ${int(totalPrfitLoss)}')
    print(f'Average Change: ${float(averageChange)}')
    # print(f'{float(totalLoss)}')
    print(f'Great Increase in Profits: {str(maxGainDate)} (${round(float(maxGain))})')

    #print(f'{float(maxProfit)}')
    print(f'Greatest Decrease in Profits: {str(maxLossDate)} (${round(float(maxLoss))})')
    #print(f'{float(maxLoss)}')

   # print(changes)


#### write to file
# Specify the file to write to
#output_path = os.path.join(".", "output", "pypoll_output.txt")

f = open('./output/pybank_output.txt', 'w')

f.write('\nFinancial Analysis')
f.close()

f = open('./output/pybank_output.txt', 'a')
#f.write('\n')
f.write('\n----------------------------')
f.write('\n')
f.write('Total Months: : ')
f.write(str(totalNumOfMonths))
f.write('\n')
f.write('Total: $')
f.write(str(round(totalPrfitLoss)))
f.write('\n')
f.write('Average Change: $')
f.write(str(averageChange))
f.write('\n')
f.write('Great Increase in Profits: ')
f.write(maxGainDate)
f.write(' $(')
f.write(str(round(maxGain)))
f.write(')\n')
f.write('Greatest Decrease in Profits: ')
f.write(maxGainDate)
f.write(' $(')
f.write(str(round(maxLoss)))
f.write(')\n')
f.close()

