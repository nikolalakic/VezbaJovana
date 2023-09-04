register = {'Michael':'yes',
            'John':'no',
            'Peter':'yes',
            'Mary':'yes'}

def register_check(r):
    count = 0

    for name, attendance in r.items():
        if attendance == "yes":
            count +=1
    return count

print(register_check(register))        
