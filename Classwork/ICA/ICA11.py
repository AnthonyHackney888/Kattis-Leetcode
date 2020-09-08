'''
author: Anthony Hackney
'''

class Person:
	def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_name(self):
        print(self.name)  
    def print_age(self):
        print(self.age)  
    
class Student:
    def __init__(self, id):
        self.id = id
    def get_ID(self):
        return self.id
   
      
class Resident(Person,Student):
    def __init__(self,name,age,id):
        Person.__init__(self,name,age)
        Student.__init__(self,id)

resident = Resident("Anthony",21,626)
resident.print_name()
resident.print_age()
print(resident.getID())