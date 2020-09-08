'''
author: Anthony Hackney
date: 10/03/19
program: FizzBuzz
'''

''' create a class called FizzBuzz (instance num, instance fbn, ) '''
class FizzBuzz:
    def __init__(self, num):
        self.num = num
        self.fbn = num
        
    @property    
    def number(self):
        return self._num
            
    @number.setter
    def number(self, num):
        self._num = int(num)
    @property
    def fbn(self):
        return self._fbn
            
    @fbn.setter
    def fbn(self, num):
        if num %3 == 0 and num %5 == 0:
            self._fbn ="FizzBuzz"
        elif num %3 == 0:
            self._fbn ="Fizz"
        elif num %5 == 0:
            self._fbn ="Buzz"
        else:
            self._fbn = str(num)
        
        


