#Function in Python 

def function():
    print("FUNCTION PROGRAM ")

print("Hello world") 
function()   #calling a function 
print("Done")



#WAP to enter name and date and write a letter
def letter(name,date):
    str = f"Hi sir my {name} is i will not come to college on {date}"
    print(str)

name = input("Enter your Name-")
date = input("Enter date-")
letter(name,date)
