# def same_in_reverse(s):
#     sr = s[::-1]
#     if hash(sr) != hash(s):
#         return False
#     else:
#         return True
#
# print(same_in_reverse('dad'))

def your_age():
    names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}
    name = str(input('Enter your name: '))
    name = name.lower()
    age = names_age[name]
    print(f'Hi {name}, you are {age} years old')

your_age()