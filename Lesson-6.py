 # == >= <= < >

a = int (input ())
b = int (input ())
c = int (input ())

if a + b > c :
    print ("Verno")
    if a + c > b:
        print ("Verno")
        if b + c > a :
            print ("Verno")
else:
    print ("Ne verno")    
