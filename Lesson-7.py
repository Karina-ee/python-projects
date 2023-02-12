
try:
    a = 5+ "b"
except: 
    print ("Type error")


c = input ("Введите первое число: ")
d = input ("Введите второе число: ")
try:
    print(int(c)+int(d))
except:
    print ("Введите числа")


