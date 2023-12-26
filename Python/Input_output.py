#I/O in Python
#Read Only
with open("animesh.txt","r") as f:
    s = f.read()
    print(s)

#Write Only
f = open("animesh.txt", "w")
s = f.write("I am Good Boy")
print(s)
f.close()

#Append
with open("animesh.txt","a") as f:
    s = f.write("I am Good BOY")
    print(s)


