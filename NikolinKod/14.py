# a = [[2, 4, 5, 6]]
# def flat_list(l):
#     b = []
#     for i in l:
#         for j in i:
#             b.append(j)
#     return b
#
# print(flat_list(a))

def your_salary():
    name = str(input('Enter teachers name: '))
    periods = int(input('Enter number of periods: '))
    rate1 = 20
    rate2 = 25
    if periods > 100:
        salary = 100*rate1 + (periods - 100)*rate2
    else:
        salary = periods*rate1
    print('Name:', name)
    print('Periods:', periods)
    print('Gross salary:', salary)

your_salary()
