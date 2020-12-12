import string
from random import choice
from sys import exit


r = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
b = [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]
z = 0
m = 10000


while m > 0:
    
    if m >= 20000:
        v1 = input('Ваш баланс достиг приличной суммы. Не желаете вывести?\ny (Да, хочу вывести!) / n (Нет, продолжу играть.)\n')
        if v1 in ('Y','y','Д','д'):
            print('Поздравляю, вы вывели деньги. До свидания!')
            break
        elif v1 in ('N','n','Н','н'):
            print('Вы продолжаете играть.')
                    
    while True:
        print('У вас есть {} $.'.format(m))
        try:
            stavka = int(input('Сколько ставим?\n'))
        except ValueError:
            print('Повторите ввод.')
        else:
            while stavka > 0 and stavka <= m:
                rlt = input('На что ставим? r - красный, b - чёрный, z - ноль\n')
                if rlt in ('r','R','b','B','z','Z'):
                    s = choice('rbz')
                    if s in ('r'):
                        rr = choice(r)
                        print(rr, ' - красный')
                    elif s in ('b'):
                        bb = choice(b)
                        print(bb, ' - черный')
                    elif s in ('z'):
                        print(z, ' - зеро')
                    if rlt.lower() == s:
                        m += stavka
                    else:
                        m -= stavka

                else:
                    print('Повторите ввод.')
                break

        if m == 0:
            print('У вас кончились деньги. Игра закончена.')
            exit(0)