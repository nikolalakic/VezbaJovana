# def count_dots(s):
#     counter = 0
#     for i in s:
#         if i == '.':
#             counter = counter + 1
#     return counter
#
# print(count_dots('h.e.lp.'))

import datetime

date = datetime.date.today()
year = date.year
def age_in_minutes():
    while True:
        try:
            a = int(input('Enter year of birth: '))
            if len(str(a)) != 4 and (a > year):
                print(f'Whats the value of bitcoin in year {year}?')
            elif len(str(a)) !=4:
                print('Age must be 4 numerals long.')
            elif a < 1900:
                print('Enter year younger than 1900')
            else:
                starost = year - a
                minutes = round(starost*365*24*60,0)
                print(f'You are {minutes} minutes old.')
                break
        except ValueError:
            print('Age must be number.')


age_in_minutes()
