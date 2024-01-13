#Modules in Python

#Time Module 
import time
current = time.ctime(2649877305.6210002)
print("Current time:", current)

#Math Module
import math
print(math.sqrt(23))

#SYS Module
import sys 
print(sys.exit)
print(sys.path)
print(sys.version)

#Dir Function
lang = ("c","c++","java","python")
att = dir(lang)
print(att)