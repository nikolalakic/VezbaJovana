import numpy as np
niz = np.array(['1','3','5'])
fruits =np.array(['apple', 'orange', 'banana', 'apple'])
names = np.array(['Yoda', 'Moses', 'Joshua', 'Mark'])

# def convert_add(lista):
#     konvertovano = np.array([lista], dtype=int)
#     suma = np.sum(konvertovano)
#     print('Suma je: ', suma)

# convert_add(niz)

def check_duplicates(niz):
    lista_jedinstvenih = np.array([])
    lista_duplikata = np.array([])
    for x in niz:
        if x not in lista_jedinstvenih:
            lista_jedinstvenih = np.append(lista_jedinstvenih, x)
        else:
            lista_duplikata = np.append(lista_duplikata, x)
    if len(lista_jedinstvenih) == len(niz):
        print('Nema duplikata')
    else:
        print('Duplikati su: ', lista_duplikata)

check_duplicates(fruits)



