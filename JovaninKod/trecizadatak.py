'''register = {'Michael':'yes',
            'John':'no',
            'Peter':'yes',
            'Mary':'yes'}

def register_check(r):
    count = 0

    for name, attendance in r.items():
        if attendance == "yes":
            count +=1
    return count

print(register_check(register))      '''

names = ["kerry", "dickson", "John", "Mary", 
 "carol", "Rose", "adam"]

def lowercase(name):
    filter = [word for word in name if not any(c.isupper() for c in word)]
    rezultat = tuple(filter)
    return rezultat

print(lowercase(names))        
    
