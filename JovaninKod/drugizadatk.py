#laksi nacin

# import math
# from collections import Counter

# lista = ['1','3','5']

# def convert_add(a):
#     a1 = [eval(i) for i in a]
#     print(sum(a1))

# convert_add(lista)    

#brzi nacin
import numpy as np

# lista = np.array(['1','3','5'])

# def convert_add(a):
#     a1 = a.astype(int)
#     print(sum(a1))

# convert_add(lista)  

fruits = np.array(['apple','orange','banana','apple'])
names = np.array(['Yoda','Moses','Joshua','Mark'])

def check_duplicates(a):
   return a.size != np.unique(a).size

print(check_duplicates(fruits))
print(check_duplicates(names))