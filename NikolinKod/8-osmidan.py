# numbers = [1, 2, 4, 6]

# def odd_even(a):
#     if (max(a) % 2 == 0) and (min(a) % 2) == 1:
#         odd = max(a)
#         even = min(a)
#         diff = odd - even
#     else:
#         diff = None
#         print('There are no odd or even numbers')
#     return diff

# print(odd_even(numbers))

# https://en.wikipedia.org/wiki/Primality_test
from math import isqrt

def prime_test(n):
    limit = isqrt(n)
    if n <= 1:
        return False
    for i in range(2, int(limit) + 1):
        if (n % i) == 0:
            return False
    return True
        
def prime_numbers():
    primes = []
    number = int(input('Enter positive integer: '))
    for num in range(2, number + 1):
        if prime_test(num) == True:
            primes.append(num)
    return primes
                  
print(prime_numbers())

