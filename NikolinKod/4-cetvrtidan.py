import numpy as np

words1 = ['Hate', 'remorse', 'vengeance', 'kuracpalackriminalac']
words2 = ['a', 'Hate', 'Hate', 'a']

def only_floats(a,b):
    niz = np.array([a, b], dtype=float)
    j = 0
    for i in niz:
        if i % 1 !=0:
            j = j+1
        else:
            pass
    print(j)

def word_index(w):
    len_reci = []
    for j in w:
        len_reci.append(len(j))
    print(len_reci.index(max(len_reci)))


only_floats(5.5, 1)
word_index(words2)
