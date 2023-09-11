# def sum_list(l):
#     suma = 0
#     for i in l:
#         for j in i:
#             suma = suma + j
#     return suma
#
#
# print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))

nested_list = [[12, 34, 56, 67], [34, 68, 78]]
allow_list = [34, 67, 78]

def unpack_list(nl):
    a = []
    for i in nl:
        for j in i:
            if j not in a and j in allow_list:
                a.append(j)

    return a

print(unpack_list(nested_list))

