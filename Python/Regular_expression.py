#Regular Expressions In Python
import re

NameAge =''' Animesh is 21 and Arpit is 22 
Ravi is 23 Kumar is 21'''

age = re.findall(r'\d{1,3}', NameAge)
name = re.findall(r'[A-Z][a-z]*', NameAge)
print(age,name)

#make a dic

agedict = {}
x=0
for eachname in name:
    agedict[eachname]=age[x]
    x+=1
print(agedict)


str="rat hat mat sat wat bat cat dat eat"
x= re.findall('[a-z]at',str)
print(x)