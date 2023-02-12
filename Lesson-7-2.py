try:

    a = int(input ('Введите Ваш год рождения '))
    b = int(input ('Введите Ваш месяц рождения '))
    c = int(input ('Введите Ваш день рождения '))

    d = int(input ('Введите сегодняшний год '))
    e = int(input ('Введите сегодняшний месяц '))
    f = int(input ('Введите сегодняшнюю дату '))
    k = d - a

    if d < a:
        print ("Ты еще не вылез из животика!")
        # if 12<b<1 or 12<e<1 or 31<c<1 or 31<f<1:
        #     print ("Такого месяца или дня нет!")
    else:
        if e < b:
            print (k -1)
        elif e == b:
            if f < a:
                print (k-1)
            else:
                print (k)
        else:
            print (k)
   
except: 
    print ('Слова вводить нельзя!')