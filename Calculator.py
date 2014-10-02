#qpy:2
#qpy:console
#qpy:http://qpython.com/s/qpy-sample.py

class Calculator(object):
    #define class to simulate a simple calculator
    def __init__ (self):
        #start with zero
        self.current = 0
    def add(self, amount):
        #add number to current
        self.current += amount
    def getCurrent(self):
        return self.current

myBuddy = Calculator() # make myBuddy into a Calculator object
myBuddy.add(2) #use myBuddy's new add method derived from the Calculator class
print(myBuddy.getCurrent()) #print myBuddy's current instance variable

