# import random as rng
#
#
# def user_name():
#     name = str(input('Enter name: '))
#     name = name[::-1] + str(rng.randint(0, 9))
#     return name
#
#
# print(user_name())

names = ["Peter", "Jon", "Andrew"]

def sort_lenght(l):
    for i in range(len(l)):
        for j in range(len(l)-1):
            if len(l[j]) > len(l[j+1]):
               l[j], l[j+1] = l[j+1], l[j]
    return l

print(sort_lenght(names))
