# def make_tuples(a, b):
#     if len(a) != len(b):
#         print('Lists must be equal in length')
#         exit()
#     else:
#         l = []
#         for i, j in zip(a, b):
#             t = (i, j)
#             l.append(t)
#         return l
#
#
# print(make_tuples([1, 2, 3, 4], [5, 6, 7, 8]))

def add_hash(s):
    for i in s:
        a = s.replace(' ', "#")
    return a


def add_underscore(s):
    for i in s:
        a = s.replace('#', '_')
    return a


def remove_underscore(s):
    for i in s:
        a = s.replace('_', " ")
    return a


print(remove_underscore(add_underscore(add_hash('Python'))))
