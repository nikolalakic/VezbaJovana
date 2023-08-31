# def user_name():
#     email = str(input('Enter email: '))
#     head, sep, tail = email.partition('@')
#     return(head)

# print(user_name())

lista = [2,5,7,8,9]

def zeroed(a):
    a[0] = 0
    a[-1] = 0
    return a

print(zeroed(lista))