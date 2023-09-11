# def capitalize():
#     words = input('Enter words: ').split()
#     capitalized = ''
#     for word in words:
#         for char in word:
#             if char == word[0]:
#                 novo = char.replace(char, char.capitalize())
#                 word = word.replace(char, novo)
#                 capitalized = capitalized + word + ' '
#     return capitalized
#
#
# print(capitalize())

str1 = 'leArning is hard, bUt if You appLy youRself ' \
'you can achieVe success'
def reversed_words(s):
    words = s.split()
    new = []
    for word in words:
        for i,j in zip(word, word):
            if i == j.capitalize() and i != ',':
                new.append(word[::-1])
    return new

print(reversed_words(str1))
