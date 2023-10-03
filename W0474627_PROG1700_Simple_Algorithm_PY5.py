#Author: Johnjie Alzate
#Student ID: W0474627
#Course: PROG1700
#Project: Simple_Algorithm
#Repository: https://github.com/johnjiealzate/PROG1700/blob/main/W0474627_PROG1700_Simple_Algorithm_PY5.py
#Programming Language: Python
#Licence: Creative Commons
#Date:09-27-23
#Version: 1.0

#Represents the age as "x" variable
x = input("Please enter your age: ")

#Exports the YTD-Year to Date as "y" variable
import datetime
y = datetime.datetime.now().year

#Displays the year you were born with a notification and provided an error for wrong input type
if x.isdigit():
    #Calculates the YOB-Year of Birth
    z = y - int(x)
    print("You're awesome! You are born on", z, ".")
else:
    print("Please enter a valid value.")