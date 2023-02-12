try:
    a = int (input("Введите четырехзначное число: "))
    if 1000<=a<10000:
        sum = int(str(a)[0]) + int(str(a)[1]) + int(str(a)[2]) + int(str(a)[3])
        print (sum)
    else:
        print ('введите четырехзначное число!')
except ValueError:
    print ("Введи число, а не строку")
finally:
    print ('Ты молодец!')