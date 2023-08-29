import math

def divide_or_square():
    a = float(input("Uneti broj: "))
    if a % 5 == 0:
        print("Vrednost korena je " + str(math.sqrt(a)))
    else:
        print("Broj nije deljiv sa 5") 
divide_or_square()           

fruits = {'fruit': 'apple', 'clor': 'green'}

def longest_value(d):
    print(max(d.values(),key=len))

longest_value(fruits)    