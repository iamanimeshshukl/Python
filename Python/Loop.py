#Loops in Python !!!

#For Loop

#WAP to print number between 1 to 100 
for i in range(101):
    print(i)

#WAP to print the set value
a={1,2,3,4,5,6,7,8}

for i in [a]:
    print(a)


#While Loop
a = 6
while(a<20):
    print(a)
    a += 1

print("Loop End")

#Nested Loops
for i in range(1,6):
    for j in range(1,6):
        print("*",end = '')
print()