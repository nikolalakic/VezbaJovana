def divide_or_square():
    a = float(input("Uneti broj: "))
    if a % 5 == 0:
        print( a ** 0.5)
    else:
        print(f"Broj {a} nije deljiv sa 5")

divide_or_square()