'''
author: Anthony Hackney, hackn1a
date:09/12/19

'''

#problem 1
#write a program that prompts the user for inches and converts into meters

user = int(input("Enter in an integer value to convert: "))

user = (user * .0254)
print("This measurment in meters is:", user)

#problem 2
#write a function that returns a correct amount

def get_admission_price(age):
    '''This function calculates the addmission prices dependant on age'''
   
    admission = 100
    if age > 0 and age < 3:
        admission = admission * 0 
    if age > 4 and age < 12:
        admission = admission - (admission * .15)
    if age > 13 and age < 55:
        admission = admission
    else:
        admission = admission - (admission *.15)
    return admission
print(get_admission_price(16))


def read_numbers(file_name):
    '''This method reads from a file and 
        prints the odd numbers and count
        and the evens get sent to a text file''' 
    with open(file_name, 'r') as f:
        with open('evens.txt', 'w') as g:
            sum = 0
            counter = 0
            for line in f:
                if int(line) % 2 == 1:
                    sum += int(line.strip('\n'))
                    counter +=1
            print(sum)
            print(counter)
            for line in f:
                if int(line) % 2 == 0:
read_numbers('numbers.txt')