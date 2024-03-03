import math
import os
import random
import re
import sys
import string

#Version 1.1.0

security_info = []
##Need to add a student.py file with student info attached. Then create a list and import it here for use in the def student_log().
##need a next list for students tht shows who enters and leaves
student_visits = []
student_details = []
non_visitor_rand = 6
non_visitor_id = []
student_info = [] #stored as name, uwi id num, room number.
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
    #name,student (yes or no), id num, entry time, room visited
def student_log():
    global student_visits
    visitor_personnel = input('Is the visitor a student?\n')
    if visitor_personnel == 'Yes' or 'YES' or 'yes':
        student_visits.append(visitor_personnel)
        visitor_name = input('Enter visitor first name and last name.\n')
        student_visits.insert(0, visitor_name)
        visitor_id = input('Enter visitor 9 digit UWI ID number.\n')
        if len(visitor_id)>9 or len(visitor_id)<9:
            visitor_id=input("The given UWI ID number does not equal 9 digits. Please double check and enter the correct ID number.\n")
        student_visits.append(visitor_id)
        entry_time= input('Please enter the arrival time.\n')
        student_visits.append(entry_time)
        room_number = input('Please enter the room number being visited.')
        student_visits.append(room_number)
        print(+visitor_name+ ' has been added to the arrival system for ' +entry_time+ '.\n')
    else:
        visitor_name = input('Enter visitor first name and last name.\n')
        student_visits.append(visitor_name)
        student_visits.append("No")
        non_visitor_id = ''.join(random.choices(string.digits, k=non_visitor_rand))
        student_visits.append(non_visitor_id)
        entry_time= input('Please enter the arrival time.\n')
        student_visits.append(entry_time)
        room_number = input('Please enter the room number being visited.')
        student_visits.append(room_number)
        print(+visitor_name+ ' has been added to the arrival system for ' +entry_time+ '.\n')

##Will add the proceeding section to a student.py file later.
def create_student():
    global student_info
    student_name = input('Enter your first and last name.\n')
    input('Is ' +student_name+ ' correct?\n')
    if input('Is ' +student_name+ ' correct?\n') == 'Yes' or 'YES' or 'yes':
        print(student_name+ ' has been added.\n')
        student_info.append(student_name)
        student_id = input('Enter current UWI Mona 9 digit ID number.\n')
        student_info.append(student_id)
        student_room = input('Enter your current room number.\n')
        student_info.append(student_room)
        print('Your information has been logged.\n')
    if input('Is ' +student_name+ ' correct?\n') == 'No' or 'NO' or 'no':
        student_name = input('Enter correct first and last name.\n')
        student_info.append(student_name)
        student_id = input('Enter current UWI Mona 9 digit ID number.\n')
        student_info.append(student_id)
        student_room = input('Enter your current room number.\n')
        student_info.append(student_room)
        print('Your information has been logged.\n')
        

def get_studentname():
    return student_info[0]
