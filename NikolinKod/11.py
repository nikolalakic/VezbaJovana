# def equal_strings(a, b):
#
#     if hash(a) == hash(b):
#         return True
#     else:
#         return False
#
#
# print(equal_strings("asd", "Asd"))

niz = [2,4,67,7]
def swap_values(l):
    n = [l[-1]]
    for i in niz[1:-1]:
        n.append(i)
    n.append(l[0])
    return n

print(swap_values(niz))

