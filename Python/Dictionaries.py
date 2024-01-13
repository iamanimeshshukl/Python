stu = {"name": "Animesh", "Age": 19 , "test": True}
print(stu)

#WAP  of Dict
n=int(input("how many students-"))
backpaper = {}
for a in range(n):
    key = input("Enter Name of Student-")
    value = int(input("How many backs-"))
    backpaper[key] = value
print("The dictionary now is:")
print(backpaper)

#Sorting Dictionaries

print(sorted(stu.keys()))
print(sorted(stu.items()))
