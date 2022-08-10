"""
1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
наприклад:
st = 'as 23 fdfdg544' введена строка
2,3,5,4,4        #вивело в консолі.
"""

# a = input('Enter any string: ')
# l = list(a)
# res = []
# for i in l:
#     if i.isdigit():
#         res.append(i)
# print(','.join(res))
# import statistics

"""
2)написати прогу яка вибирає зі введеної строки числа і виводить їх 
так як вони написані
наприклад:
  st = 'as 23 fdfdg544 34' #введена строка
  23, 544, 34              #вивело в консолі
"""

# print(', '.join(''.join(i if i.isdigit() else ' ' for i in st).split()))

"""
1)є строка:
greeting = 'Hello, world'
записати кожний символ як окремий елемент списку і зробити його заглавним:
['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
"""

# greeting = 'Hello, world'
# l=list(greeting.upper())
# print(l)

"""
2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
приклад:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
"""
# l=[]
# for i in range(51):
#     if i%2!=0:
#         l.append(i**2)
# print(l)

"""
- створити функцію яка виводить ліст
- створити функцію яка приймає три числа та виводить та повертає найбільше.
- створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
- створити функцію яка повертає найбільше число з ліста
- створити функцію яка повертає найменьше число з ліста
- створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
- створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
"""

# def func(l):
#     print(l)
# func([1,2,3,4])

# def maxfunc(a,b,c):
#     print (max(a,b,c))
#     return max(a,b,c)
# maxfunc(11,8,4)

# def func(*args):
#     print(max(*args))
#     return min(*args)
# func(2,5,8,4,7,45)

# def func(l):
#     l.sort(reverse=True)
#     print(l[0])
#     return l[0]
# func([2,5,4,8,5,9,7])

# def func(l):
#     l.sort
#     print(l[0])
#     return l[0]
# func([2,5,4,8,5,9,7])

# def func(l):
#     s=sum(l)
#     print(s)
#     return s
# func([2,5,4,8,5,9,7])

# def func(l):
#     s=statistics.mean(l)
#     print(s)
#     return s
# func([2,2,4,4,2,4])

"""
1)Дан list:
  list = [22, 3,5,2,8,2,-23, 8,23,5]
  - знайти мін число
  - видалити усі дублікати
  - замінити кожне 4-те значення на 'X'
2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
3) вывести табличку множення за допомогою цикла while
4) переробити це завдання під меню
"""

list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5, 2, 6, 7]
def minimum():
    resmin = min(list)
    print(resmin)


def removedublicate():
    res = []
    res.append(list[0])
    for i in list:
        s = len(res)
        n = 0
        for k in res:
            n = n + 1
            if i == k:
                break
            if n == s:
                res.append(i)
    print(res)


def replacetox():
    for i in range(3, len(list), 4):
        list[i]='x'
    print(list)


def square(number):
    a='*'
    print(a*number)
    for i in range(0,number-2):
        print(a+' '*(number-2)+a)
    print(a*number)


def table():
    i = 1
    while i <= 9:
        k = 1
        while k <= 9:
            result = k * i
            print(f'{result:4}', end='')
            k += 1
        i += 1
        print()

while True:
    print('1) minimum')
    print('2) remove_duplicate')
    print('3) replace_to_x')
    print('4) square')
    print('5) table')
    print('9) exit')

    select = input('Make your selection: ')

    if select == '1':
        minimum()
    elif select == '2':
        removedublicate()
    elif select == '3':
        replacetox()
    elif select == '4':
        square(10)
    elif select == '5':
        table()
    elif select == '9':
        break