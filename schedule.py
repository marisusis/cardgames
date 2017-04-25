classes = []

import lib

# Get Student
student = lib.Student(input("What is your first name? "),input("What is your last name? "))

# Use ASCII char codes to create ID based on name
student.setID(int(input("Student ID: ")))

while (True):
    clsName = input("Enter the next class, STOP to end. ")
    if (clsName == "STOP"):
        break
    else:
        num = int(input("Enter the room number. "))
        student.addClass(Class(clsName,num))
