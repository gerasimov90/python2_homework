#Задача 10
#некоторые – гербом. Определите минимальное число монеток, которые нужно
#перевернуть, чтобы все монетки были повернуты вверх одной и той же
#стороной. Выведите минимальное количество монет, которые нужно
#перевернуть.
#n = int(input('Введите количество монеток, лежащих на столе: '))
#tails = 0
#eagle = 0
#for i in range(n):
#    x = int(input('Обозначьте сторону каждой монетки 1 - орел, 0 - решка: '))
#    if x == 0:
#        tails += 1
#    else:
#        eagle += 1
#if eagle > tails:
#    print('Минимальное количество переворачиваний: ', tails)
#else:
#    print('Минимальное количество переворачиваний: ',eagle)

#Задача 12  Петя и Катя – брат и сестра. Петя – студент, 
#а Катя – школьница. Петя помогает Кате по математике. 
#Он задумывает два натуральных числа X и Y (X,Y≤1000), 
#а Катя должна их отгадать. Для этого Петя делает две подсказки. 
#Он называет сумму этих чисел S и их произведение P. 
#Помогите Кате отгадать задуманные Петей числа.
#x = int(input('Введите сумму двух загаданных чисел: '))
#y = int(input('Введите произведение двух загаданных чисел: '))
#for i in range(x):
#    for j in range(y):
#        if x == i + j and y == i * j:
#            print('Загаданные числа:', i, 'и', j)

#Задача 14 Требуется вывести все целые степени двойки 
#(т.е. числа вида 2k), не превосходящие числа N.
n = int(input('Введите граничное число: '))
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1