#OOPS IN PYTHON 


#class in python 

class Car:
    def __init__(self, modelname, year):
        self.modelname = modelname
        self.year = year
    
    def display(self):
        print(self.modelname, self.year)

c1 = Car("abs", 2323)
c1.display()
