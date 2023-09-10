def your_vat():
    while True:
        try:
            a = float(input('Enter price: '))
            b = float(input('Enter VAT [%]: '))
            break
        except ValueError:
            print('Enter valid values for price and VAT')
    s = a + a * b/100
    return s


print(your_vat())
