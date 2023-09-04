def only_float():
    #a = input("Uneti prvi broj")
    #b = input("Uneti drugi broj")
    a=12.2
    b=6
    if isinstance(a,float) == True and isinstance(b,float) == True:
        return 2
    elif isinstance(a,float) == False and isinstance(b,float) == True:
        return 1
    elif isinstance(a,float) == True and isinstance(b,float) == False:
        return 1
    else:
        return 0
    
print(only_float())    

