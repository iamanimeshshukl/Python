#Conditionals Statement in Python 

#Write a Program to check that person is 18+ or not !! 

age = int(input("Enter Your Age-"))

if(age>18):
    print("You are 18+")
else:
    print("You are not 18+")


 #Write a program to check Number  

a = int(input("Enter A number-"))
b = int(input("Enter B number-"))

if(a>b):
    print("B is smaller than A")
elif(a==b):
    print("A and B both are Equals")
else:
    print("B is grater then A ")
      

#WAP to find month in case condiction !!!

m = int(input("Enter month Number-"))

match m:
    case 1:
        print("Jan")
    case 2:
        print("feb")
    case 3:
        print("march")
    case 4:
        print("april")
    case 5:
        print("May")
    case 6:
        print("june")
    case 7:
        print("July")
    case 8:
        print("augest")
    case 9:
        print("sept")
    case 10:
        print("oct")
    case 11:
        print("nov")
    case 12:
        print("dec")
    case _:
        print("enter correct value")
    