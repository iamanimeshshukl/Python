#Exception Handling in Python

try:
    x = int(input("Enter your age-"))
    print("Your Age is-",x)
except Exception as e:
    print("Something is wrong",e)



#Use of Assert keyword 
a = 4
b = 0

assert b!=0 
print(a/b)


#use of raise keyword

def divide(a,b):
   if b == 0:
      raise ValueError("CANNOT DIVIDE ZERO")
   return a/b 

try:
   result = divide(10,2)
   print(result)
except ValueError as e:
   print(e)

