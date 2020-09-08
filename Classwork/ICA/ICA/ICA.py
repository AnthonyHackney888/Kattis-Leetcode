# author: Anthony Hackney
# 280S
#In class activity 5

#problem 1
#Write a funciton that prints numbers 1-10 skipping numbers divisible by 3

def print_numbers(start, end):
    for i in range(start ,end):
        if i % 3 == 0:
            continue
        else:
            print(i)
print_numbers(1, 11)


#problem 2
# Write a function to sum the items in a list
def sum_list(numbers):
    
    
    sum = 0
    for i in numbers:
        sum += i
    return sum 

numbers = [1,2,3,4,5,6]
print(sum_list(numbers))

#problem 3
#write a function to find common items from two lists



def two_sets(list_one, list_two):
        for i in list_one:
            for j in list_two:
                if i == j:
                    return i        
list_one = [1,2,3]
list_two = [3,4,5]    
print(set(list_one) & set(list_two))
print(two_sets(list_one, list_two))

#probelm 4
#write a function to loop over key/value pairs in a dict and print them out

def dictionary_print():
    dict = { 'a':1, 'b':2, 'c':3}
    for k,v in dict.items():
        print(k,'->',v)
dictionary_print()        