register = {'Michael':'yes', 'John': 'no', 'Peter':'yes', 'Mary': 'yes'}
names = ['kerry', 'dickson', 'John', 'Mary', 'carol', 'Rose', 'adam']

def register_check(d):
    counter = 0 
    for key in d:
        if d[key] == 'yes':
            counter = counter + 1
        else:
            pass
    print('Number of attending students is:', counter)

def lowcase(n):
    lowcase_names = []
    for i in n:
        if i.islower() == True:
            lowcase_names.append(i)
        else:
            pass
    lowcase_names.sort(reverse=True)
    print(lowcase_names)

register_check(register)
lowcase(names)

