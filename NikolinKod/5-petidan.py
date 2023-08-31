# def my_discount():
#     a = float(input('Input price: '))
#     b = float(input('Input discount [%]: '))
#     price = a * (1-b/100)
#     return(price)

# print(my_discount())

students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

def genders():
    s_lower = []
    males = 0
    females = 0
    for i in students:
        s_lower.append(i.lower())
    for i in s_lower:
        if i == 'male':
            males = males + 1
        elif i == 'female':
            females = females + 1
        else:
            print('Typo')
    return [('Male',males),('female',females)]

print(genders())




        
