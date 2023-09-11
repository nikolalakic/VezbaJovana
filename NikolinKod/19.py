# def count_words():
#     words = str(input('Enter words: ')).split()
#     counter = 0
#     for i in words:
#         counter = counter + 1
#     return counter
#
# print(count_words())

def count_elements():
    words = str(input('Enter words: ')).split()
    counter = 0
    for word in words:
        for char in word:
            counter = counter + 1
    return counter

print(count_elements())
