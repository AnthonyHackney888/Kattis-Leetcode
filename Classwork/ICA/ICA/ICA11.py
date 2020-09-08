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
    def print_id(self):
      print(self.id)
      
class Resident:
    def __init__(self,name,age,id):
    Person.__init__(self,name,age)
    Student.__init__(self,id)

resident = Resident()
print(resident.getID())