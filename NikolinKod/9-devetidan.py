list1 = [1, 4, 8, 0, 7, 0, 9]
list2 = [2, 1, 4, 7, 6]


# def biggest_odd(s):
#     s = str(s)
#     number = max([i for i in s if (int(i) % 2) == 1])
#     return number
#
#
# print(biggest_odd(23569))

def zeroes_last(s):

    for i in s:
        if i == 0:
            s.remove(i)
            s.append(i)
        elif (i == 0) not in s:
            s.sort()
    return s


print(zeroes_last(list2))
