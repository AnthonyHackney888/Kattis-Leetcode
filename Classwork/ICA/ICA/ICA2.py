
'''
In-class Assignment 2
08/29/2019

author: Antony Hackney
'''


#problem 1
print("Anthony")
print(1,2,3,4,5,sep = "\n")

#problem 5
course_description = "Alternative Programming Languages"
print(course_description[::-1])
print(course_description[0:11])
print(course_description[11:23])
print(course_description[:23:-1])
print(course_description[0::2])

#problem 6
celsius = 15
print((celsius * 9/5) + 32)

#problme 7
userInput = int(input("what is the time?"))
if userInput < 11:
    print("Good Morning")
elif userInput > 11 & userInput < 13:
    print("time for lunch")
