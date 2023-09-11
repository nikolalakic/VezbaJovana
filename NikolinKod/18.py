# def any_number():
#     lista = input('Enter numbers separated by space: ').split()
#     numbers = []
#     for i in lista:
#         numbers.append(float(i))
#     suma = 0
#     for i in numbers:
#         suma = suma + i
#     return suma/len(lista)
#
#
# print(any_number())

lista1 = [10, 12, 34]
lista2 = [12, 56, 78]
def add_reverse(l1, l2):
    nova_lista = []
    for i,j in zip(l1, l2):
        nova_lista.append(i + j)
    nova_lista = nova_lista[::-1]
    return nova_lista

print(add_reverse(lista1, lista2))


