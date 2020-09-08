'''
author: Anthony Hackney
Date: 09/05/19

problem 1
Find the longest word and the shortest word
'''
def read_file(fileName):
    '''This function reads a file and finds the largest and smallest word '''
    with open(fileName,'r') as f:
        longWord = f.readline()
        f.seek(0)
        shortWord = f.readline()
        for line in f:
            if len(line) > len(longWord):
                longWord = line
            if len(line) < len(shortWord):
                shortWord = line
        print(longWord)
        print(shortWord)

#read_file("words.txt")


#Problem 2
#Print the odd lines?

def print_odd_lines(fileName):
    '''This function reads a file and finds the odd lines and reverses them '''
    with open(fileName,'r') as f:
        longWord = f.readline()
        f.seek(0)
        count = 0
        for line in f:
            count +=1
            if count % 2 == 1:
                longWord = line
                print(longWord[::-1])
        
        
#print_odd_lines("words.txt")
#problem 3
# wrote a program to read a list of numbers, sum them, and divide by the number of lines in file

def print_numbers(file_name):
    ''' '''
    with open(file_name, 'r') as f:
        numbers = f.readline()
        f.seek(0)
        count = 0
        sum = 0
        for line in f:
            count +=1
            sum  += int(line.strip('\n'))
        print(sum/count)
        
#print_numbers("numbers.txt")


#problem 4
#write a python program to read teh contents of a file, add line numbers to the beginning of each line
# and write to a new file. 
def write_to_file(file_name):
    ''' '''
    with open(file_name, 'r') as f:
        output = open('test.txt' , 'w')
        counter = 0
        for word in f:
            counter+=1
            output.write(str(counter) + ". " + word)
        output.close()        
            
            
            
            
            
#write_to_file('words.txt')

#problem 5
#write a method to conver celcius to fahrenheit
def converting_to(celsius):
     return ((celsius * 9/5) + 32)
#print(converting_to(32))

#problem 6
#conditionals write a method to find the max of three numbers

def find_max_of_three(x, y, z):
    max = 0
    if x > y:
        max = x
    if x > z:
        max = x
    if y > z:
        max = y
    if y > x:
        max = y
    if z > y:
        max = z
    if z > x:
        max = z
    
    return max


print(find_max_of_three(1, 3, 5))

