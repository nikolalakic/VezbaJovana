# def equal_strings(a, b):
#
#     if hash(a) == hash(b):
#         return True
#     else:
#         return False
#
#
# print(equal_strings("asd", "Asd"))

niz = [1,5,7,9]
def swap_values(l):
    n = [l[-1]]
    for i in niz[1:-1]:
        n.append(i)
    n.append(l[0])
    return n

print(swap_values(niz))

