'''
author: Anthony Hackney
date 09/03/19

'''

#problem 3
letterGrade = int (input("Enter your letter grade: "))

if letterGrade >= 90:
    print("A")
elif letterGrade >= 80 and letterGrade < 90:
    print("B")
elif letterGrade >= 70 and letterGrade < 80:
    print("C")
elif letterGrade >= 60 and letterGrade < 70:
    print("D")
else:
    print("F")

print("")

print("Problem 1 and 2: Reading a file line by line\n")

#problem 1 & 2
with open("ZenOfPython.txt","r") as file:
    for line in file:
        print (line.strip("\n"))