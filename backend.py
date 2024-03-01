import math
import os
import random
import re
import sys

security_info = []
##Need to add a student.py file with student info attached. Then create a list and import it here for use in the def student_log().

def helloWorld():
    print('Hello World')

def num_there(s):
    return any(i.isdigit() for i in s)

def security_create():
    global security_info
    firstName = input("Enter first name.\n")
    while num_there(firstName) == True:
        firstName = input('Given name contains a number. Please enter a name without a number(s).\n')
    if input("Is "+firstName+' correct?\n') == 'No' or 'NO':
        firstName = input('Enter correct first name.\n')
        security_info.append(firstName)
    if input("Is "+firstName+' correct?\n') == 'Yes' or 'YES':    
        security_info.append(firstName)
    lastName = input('Enter last name.\n')
    if input("Is "+firstName+' correct?\n') == 'No' or 'NO':
        firstName = input('Enter correct first name.\n')
        security_info.append(lastName)
    if input("Is "+firstName+' correct?\n') == 'Yes' or 'YES':    
        security_info.append(lastName)
    work_idNum = input('Enter your work ID number.\n')
    security_info.append(work_idNum)
    return "You have successfully been added to the system.\n"
    
def student_log():
    
    