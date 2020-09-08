'''
author: Anthony Hackney
'''
from Employee import Employee

    
def read_file(file_name):
    list_of_employees = []
    with open(file_name) as f:
        for line in f:
            line = line.strip().split(',')
            list_of_employees.append(Employee(line[0], line[1], line[2], line[3]))
            return list_of_employees

def print_employees(list_of_employees):
    for i in list_of_employees:
        i.print_description()
    
    




employees = read_file('Employee.txt')
print_employees(employees)