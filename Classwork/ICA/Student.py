''' 
author Anthony Hackney, hackn1a

calculates a grade taking in the first name, last name, and grade. 
returning the letter grade of that list
'''


class student
    def __init__(self, Fname,Lname,Mscore,Epoints):
        self.Fname = Fname
        self.Lname = Lname
        self.Grade = abc_list = [Mscore, Epoints]
        
        
        
    def __str__(self):
        return (self.Fname, self.Lname + "Letter Grade: " + str(self.Epoints)
    
    #setters
    @Fname.setter
    def Fname(self, Fname):
        self._Fname = Fname
    @Lname.setter
    def Lname(self, Lname):
        self._Lname = Lname
    #getters
    @property
    def Fname(self):
        return self._Fname
    @property
    def Lname(self):
        return self._Lname
    @property
    def Grade(self):
        return self._Grade
    @Grade.setter
    def Grade(self, iterable):
        sum = 0
        max_score = iterable[0]
        for i in range(1,len(iterabel[1])):
            sum += iterable[1][i]
        percent = sum/max_score
            
        if percent < .15
            self._Grade = 'E'
    