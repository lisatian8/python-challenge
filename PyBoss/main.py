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

idx=0
idx2=0
idx3=0
idx4=0
idx5=0
idx6=0
counter = 0


us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


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
        stateAbbs.append(us_state_abbrev[row[4]])
        

             

    #print(empID)
    #print(name)
   # print(DOB)
   # print(SSN)
    #print(state)
   # print(firstName)
   # print(lastName)
   # print(name2)
   # print(month)
   # print(day)
    #print(year)
   # print(ssnPart1)
   # print(ssnPart2)
    #print(ssnpart3)
    #print(stateAbbs)
    print("appending list is done")
    print("writing to csv file...")

    


# Specify the file to write to
output_path = os.path.join(".", "output", "pyboss_output.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

    # Write the second row
    #csvwriter.writerow(['101','Caleb', 'Frost', '12/04/1985','505-80-2901', 'NY'])
    for empid in empID:
       idx = empID.index(empid)
       csvwriter.writerow([empid, firstName[idx], lastName[idx], month[idx]+'/'+day[idx]+'/'+year[idx],'***-**-'+ssnpart3[idx], stateAbbs[idx]])

    
 

