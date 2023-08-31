# def string_range(n):
#     streeng = ''
#     for i in range(n):
#         streeng =streeng + str(i) + '.'
#     return streeng
# print(string_range(6))

names = ['Joseph', 'Nathan', 'Sasha', 'Kelly', 'Muhammad', 'Jabulani', 'Sera', 'Patel', 'Sera']

def names_with_s(names):
    imena = []
    broj_ponavljanja = {}
    for i in names:
        if i[0] == 'S':
            imena.append(i)
    for i in imena:
        if i in broj_ponavljanja: 
            broj_ponavljanja[i] += 1
        else:
            broj_ponavljanja[i] = 1
    return broj_ponavljanja

print(names_with_s(names))