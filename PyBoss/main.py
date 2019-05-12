# Modules
import os
import csv
import re
#import math

# Prompt user for video lookup
#video = input("What show or movie are you looking for? ")

# Lists to store data
empID = []
firstName = []
lastName = []
name = []
DOB = []
month = []
day = []
year = []
SSN = []
state = []
stateAbbs = []
name2 = []
ssnPart1 =[]
ssnPart2=[]
ssnpart3=[]

occurrence = 0

maxLossDate = ""
maxGain = 0
maxGainDate = ""
totalLoss = 0
averageChange = 0
totalChanges = 0
count = 0
currentChange = 0

idx=0
idx2=0
idx3=0
idx4=0
idx5=0
idx6=0
ssnstring1 = ""
ssnstring2 = ""
ssnstring3 = ""

workingstring = ""


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

        empID.append(row[0])
       # print("here")
        #print(str(row[0]))
        ####print(f'date: {row[0]}')
 
       ### three lists, name, first name, last name
        name.append(row[1])
        occurrence = row[1].count(' ')
        if occurrence > 1:
             name2.append(row[1])
        else:
            idx = row[1].index(' ')
            firstName.append(row[1][0:idx])
            lastName.append(row[1][idx+1:])
        

        DOB.append(row[2])
        ###append year, month, day
        year.append(row[2][0:4])
        month.append(row[2][5:7])
        day.append(row[2][9:11])


        SSN.append(row[3])
        #idx4 = row[3].index('-')
        ssnPart1.append(row[3][0:3])
        ssnPart2.append(row[3][4:6])
        ssnpart3.append(row[3][7:11])

   

        state.append(row[4])


        #print("here")
        #print(str(row[0]))
        ####print(f'profigLosses: {row[1]}')

     #   totalPrfitLoss = float(totalPrfitLoss) + float(row[1])

        #if float(row[1]) > 0 && float(row[1]) > float(maxProfit):


       # if count <= 0:
       #      count = int(count) +1
        #else:     
        #    currentChange = float(row[1]) - float(profitLosses[int(count)-1])    
       #     totalChanges = float(totalChanges) + float(row[1]) - float(profitLosses[int(count)-1])
       #     changes.append(currentChange)

      #      if float(currentChange) > float(maxGain):
      #           maxGain = float(currentChange)
      #           maxGainDate = str(row[0])

      #      elif float(currentChange) < float(maxLoss):
     #             maxLoss = float(currentChange)
      #            maxLossDate = str(row[0])
      #            totalLoss = totalLoss + float(row[1])
            
      #      count = int(count) + 1
             

    print(empID)
    print(name)
    print(DOB)
    print(SSN)
    print(state)
    print(firstName)
    print(lastName)
    print(name2)
    print(month)
    print(day)
    print(year)
    print(ssnPart1)
    print(ssnPart2)
    print(ssnpart3)

    



    
    #print(f"{len(dates)}")
    ####print(f'{totalChanges}')

    #totalNumOfMonths=len(dates)
    #averageChange = float(totalChanges/float(len(totalChanges)))
    #averageChange = float(totalLoss)/float(totalNumOfMonths)
    #averageChange = float(totalChanges)/float(totalNumOfMonths -1)
    
    #### print on terminal
    #print("Financial Analysis")
   # print("----------------------------")
   # print(f'Total Months: {int(totalNumOfMonths)}')
   # print(f'Total: ${int(totalPrfitLoss)}')
   # print(f'Average Change: ${float(averageChange)}')

   # print(f'Great Increase in Profits: {str(maxGainDate)} (${round(float(maxGain))})')

    #print(f'Greatest Decrease in Profits: {str(maxLossDate)} (${round(float(maxLoss))})')


   # print(changes)


#### write to file
# Specify the file to write to
#output_path = os.path.join(".", "output", "pypoll_output.txt")



