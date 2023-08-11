# # #3.6.1 Напишите цикл while, который находит максимальное натуральное число, квадрат которого меньше 1000.
# #
# # S = 1
# #
# # while S*S < 1000:
# #     S += 1
# #     print("Ещё считаю ...")
# #
# # print("Сумма равна: ", S-1)
#
# # ЗАДАНИЕ 3.7.2 (НА САМОПРОВЕРКУ) Попробуйте теперь самостоятельно подсчитать произведение всех чисел от 1 до N включительно.
# P = 1  # создаём переменную-счётчик, в которой мы будем считать произведение.
# #подумайте, чему она должна быть равна
# N = 5
#
# for i in range(1, N+1):
#     P *= i
# print(P)
#
# # ЗАДАНИЕ 3.7.3 (НА САМОПРОВЕРКУ)
# #
# # Напишите программу, которая будет печатать лесенку следующего типа:
# N = 4
# for i in range(1, N+1):
#     print('*'*i)
#
# ЗАДАНИЕ 3.8.1 (НА САМОПРОВЕРКУ) Напишите цикл, который ищет наибольший элемент в матрице.
# test_matrix = [[1, 2, 3],
#                [70, -1, 2],
#                [123, 2, -1]]
# max_value = 0
# for row in test_matrix:
#     for col in row:
#         if col > max_value:
#             max_value = col
# print(max_value)

# Итоговый проект Часть 2. Циклы
# Помните, в прошлом модуле мы с вами разбирали, как определить, содержит ли число цифры цифры, 5, 7 или 9:
# if ‘5’ in str(num):
# # ✍️ Ваша задача Напишите алгоритм, который делает то же самое, но работает только с числом, не приводя его в строку.
# # Для этого вам понадобится цикл while, операции деления на 10 и поиска остатка от деления на 10.
# # Вычисляя остаток от деления на 10, мы получаем крайнюю правую цифру числа, а деля число на 10 —
# # следующее число для итерации.
# num = 164863
# while num > 0:
#     num2 = num % 10
#     num = num//10
#     if num2 % 5 == 0 or num2 % 7 == 0 or num2 % 9 == 0:
#         print('Число содержит 5, 7 или 9')
#         break
# else:
#     print('В числе нет 5, 7 или 9')
# Задание 4.2.6
# Задание на самопроверку.
#
# Напишите функцию, которая проверяет, является ли данная строка палиндромом или нет,
# и возвращается результат проверки. Пример:
# def poly(text):
#     text = text.replace(' ','')
#     if text == text[::-1]:
#         print('Yes')
#     else:
#         print('No')
# poly('qw ere wq')

# Задание 4.3.2
# Задание на самопроверку.
#
# Написать функцию, которая будет перемножать любое количество переданных ей аргументов.
# def multy(*num):
#     sum = 1
#     for n in num:
#         sum *= n
#     return sum
# print(multy(4,5,6))

# Задание 4.3.3
# Задания на самопроверку.
#
# С помощью рекурсивной функции найдите сумму чисел от 1 до n.
# def sum(n):
#     if n == 1:
#         return 1
#     return n + sum(n-1)
#
# print(sum(5))

# Задание 4.3.4
# С помощью рекурсивной функции развернуть строку.
# def reverse_str(string):
#    if len(string) == 0:
#        return ''
#    else:
#        return string[-1] + reverse_str(string[:-1])
#
# reverse_str('test')  # tset

# Задание 4.3.5
# Дано натуральное число N. Вычислите сумму его цифр.
#
# При решении этой задачи нельзя использовать строки, списки, массивы (ну и циклы, разумеется).
# def sum_digit(n):
#    if n < 10:
#        return n
#    else:
#        return n % 10 + sum_digit(n // 10)
#
# sum_digit(123)  # 6

# Задание 4.4.1
# Задание на самопроверку.
#
# Создать функцию-генератор, возвращающую бесконечную последовательность натуральных чисел.
# По умолчанию, она начинается с единицы и шагом 1, но пользователь может указать любой шаг и
# любое число в качестве аргумента функции, с которого будет начинаться последовательность.
#
# def gen(start=1, step=1):
#     n = start
#     while True:
#         yield n
#         n += step
# a = gen(1,5)
# print(next(a))
# print(next(a))

# Задание 4.4.2
# Задание на самопроверку.
#
# Создайте генератор, который по переданному списку создаёт последовательность, в которой элементы
# этого списка бесконечно циклично повторяются.
#
# Например, для списка [1, 2, 3] генератор создаст бесконечную последовательность 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, ... .
#
# def repeat_list(list_):
#    list_values = list_.copy()
#    while True:
#        value = list_values.pop(0)
#        list_values.append(value)
#        yield value
#
# for i in repeat_list([1, 2, 3]):
#    print(i)
#
# Задание 4.5.1
# Задание на самопроверку.
#
# Возьмите из предыдущего примера декорированные функции, которые возвращают время работы
# основной функции. Найдите среднее время выполнения для 100 выполнений каждой функции.
#
# import time
#
# N = 100
#
#
# def decorator_time(fn):
#    def wrapper():
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        return dt
#    return wrapper
#
#
# def pow_2():
#    return 10000000 ** 2
#
#
# def in_build_pow():
#    return pow(10000000, 2)
#
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
# mean_pow_2 = 0
# mean_in_build_pow = 0
# for _ in range(N):
#    mean_pow_2 += pow_2()
#    mean_in_build_pow += in_build_pow()
#
# print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
# print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / N:.10f}")
#
# Задание 4.5.2
# Задание на самопроверку.
#
# Напишите декоратор, который будет подсчитывать количество вызовов декорируемой функции.
# Для хранения переменной содержащей, количество вызовов, используйте nonlocal область декоратора.
#
# def decor(fun):
#     count = 0
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         fun(*args, **kwargs)
#         count += 1
#         print(f'Функцию {fun} вызвали {count} раз')
#         return count
#     return wrapper
#
# @decor
# def prt(Hello):
#     print(Hello)
# for i in range(3):
#     prt('Hi')

#
# Задание 4.5.3
# Задание на самопроверку.
#
# Напишите декоратор, который будет сохранять результаты выполнения декорируемой функции в словаре.
# Словарь должен находиться в nonlocal области в следующем формате: по ключу располагается аргумент
# функции, по значению результат работы функции, например, {n: f(n)}.
#
# def cache(func):
#    cache_dict = {}
#    def wrapper(num):
#        nonlocal cache_dict
#        if num not in cache_dict:
#            cache_dict[num] = func(num)
#            print(f"Добавление результата в кэш: {cache_dict[num]}")
#        else:
#            print(f"Возвращение результата из кэша: {cache_dict[num]}")
#        print(f"Кэш {cache_dict}")
#        return cache_dict[num]
#    return wrapper

# Задание 5.3.8
# Задание на самопроверку.
#
# Программа должна выводить «Обе переменные ложные», если они являются таковыми.
# Дополните условный оператор последним блоком.
# if a and b :
#     print("Обе переменные истинные")
#     print(a,b)
# elif a or b:
#     print("Одна из переменных истинная")
#     print(a or b ) # печать одной переменной, которая является истинной
# else:
#     print("Обе переменные ложные")
#
# Задание 6.3.13
# Задание на самопроверку.
#
# При помощи генератора списков создайте таблицу умножения чисел от 1 до 10.
# tab = [[i*o for i in range(1,10)] for o in range(1,10)]
# print(tab)

# Задание 6.3.14
# Задание на самопроверку.
#
# Модифицируйте последний пример таким образом,
# чтобы в список сохранялось True, если элемент четный, и False, если элемент нечетный.
# L = [int(input()) % 2 == 0 for i in range(5)]
# print(L)

# Задание 6.3.17
# Задание на самопроверку.
#
# Используя функцию zip() внутри генераторов списков, вычислите поэлементные произведения списков L и M.
# a = [i for i in range(10)]
# b = [i for i in range(10,0,-1)]
# c = [aa*bb for aa,bb in zip(a,b)]
# print(c)

# Задание 6.3.18
# Задание на самопроверку.
#
# Реализуйте программу, которая сжимает последовательность символов. На вход подается последовательность вида:
#
# aaabbccccdaa
# Необходимо вывести строку, где каждая последовательность из одинаковых символов,
# идущих подряд, заменяется на один символ, и длину этой последовательности
# (включая последовательности единичной длины). Вывод должен выглядеть так:
#
# a3b2c4d1a2
#
# text = input()  # получаем строку
#
# last = text[0]  # сохраняем первый символ
# count = 0  # заводим счетчик
# result = ''  # и результирующую строку
#
# for c in text:
#     if c == last:  # если символ совпадает с сохраненным,
#         count += 1  # то увеличиваем счетчик
#     else:
#         result += last + str(count)  # иначе - записываем в результат
#         last = c  # и обновляем сохраненный символ с его счетчиком
#         count = 1
#
# result += last + str(count)  # и добавляем в результат последний символ
# print(result)

# Задание 5.4.9
# Задание на самопроверку.
#
# Напишите рекурсивную функцию, находящую минимальный элемент
# списка без использование циклов и встроенной функции min().
# def min_list(L):
#     if len(L) == 1:
#         return L[0]
#     return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])
#
# b = [1,2,4]
# a = min_list(b)
# print(a)

# Задание 5.4.10
# Задание на самопроверку.
#
# Напишите рекурсивную функцию, которая зеркально разворачивает число. Предполагается, что число не содержит нули.
#
# def razv(num):
#     a = str(num)
#     if len(a) == 1:
#         return a
#     else:
#         return a[-1] + razv(a[0:-1])
#
# def mirror(a, res=0):
#     return mirror(a // 10, res*10 + a % 10) if a else res
#
# a = 1234
# print(mirror(a))
#
# Задание 5.4.11
# Задание на самопроверку.
# Поработаем над более сложной рекурсивной функцией. Сейчас попробуем реализовать функцию equal(N, S),
# проверяющую, совпадает ли сумма цифр числа N с числом S. При написании программы следует обратить
# внимание на то, что, если S стала отрицательной, то необходимо сразу вернуть False.
# Реализуйте описанную выше функцию.
#
# def equal(N, S):
#     if S < 0:
#         return False
#     if N < 10:
#         return N == S
#     else:
#         return equal(N // 10, S - N % 10)
#
# Задание 5.4.15
# Задание на самопроверку.
#
# Реализуйте функцию-декоратор, которая проверяет доступ к функции по username пользователя.
# Все username пользователей хранятся в глобальной области видимости в списке USERS.
# При согласии пользователя на авторизацию ему предлагается ввести username, который также хранится
# в глобальной области видимости. Функция должна использовать два декоратора: один для проверки авторизации
# вообще (реализован выше), второй — для проверки доступа.
#
# yesno = input("""Введите Y, если хотите авторизоваться или N,
#              если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
#
#
# def is_auth(func):
#     def wrapper():
#         if auth:
#             print("Пользователь авторизован")
#             func()
#         else:
#             print("Пользователь неавторизован. Функция выполнена не будет")
#     return wrapper
#
#
# @is_auth
# def from_db():
#     print("some data from database")
#
#
# from_db()
# USERS = ['admin', 'guest', 'director', 'root', 'superstar']
#
# yesno = input("""Введите Y, если хотите авторизоваться или N,
#              если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
#
# if auth:
#     username = input("Введите ваш username:")
#
# @is_auth
# @has_access
# def from_db():
#     print("some data from database")
#
# from_db()
# Ответ
# def has_access(func):
#     def wrapper():
#         if username in USERS:
#             print("Авторизован как", username)
#             func()
#         else:
#             print("Доступ пользователю", username, "запрещен")
#     return wrapper
#
# Задание 1.9.1
# Выполните задание, взяв за основу код из примера выше.
#
# Добавьте еще один класс — круг ( class Circle), конструктор которого содержит параметр радиус. Добавьте метод для расчета площади круга (вспомните формулу).
#
# Далее сделайте вывод информации о площади в консоль.
#
# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def get_area(self):
#         return self.a * self.b
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_area_square(self):
#         return self.a ** 2
#
# class Circle:
#     def __init__(self, r):
#         self.r = r
#     def get_area_circle(self):
#         return (self.r ** 2) * 3.14
#
#
# rect_1 = Rectangle(3, 4)
# rect_2 = Rectangle(12, 5)
# square_1 = Square(5)
# square_2 = Square(10)
# circle_1 = Circle(1)
# circle_2 = Circle(2)
#
# figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
# for figure in figures:
#     if isinstance(figure, Square):
#         print(figure.get_area_square())
#     elif isinstance(figure, Rectangle):
#         print(figure.get_area())
#     else:
#         print(figure.get_area_circle())
#
# Игра ТИР
#
# import pygame
# import random as rnd
#
#
# # ============================================
# class Pos:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y
#
#
# # ------------------------------------
# class Figure:
#     def __init__(self, pos) -> None:
#         self.setPos(pos)
#
#     def setPos(self, pos):
#         self.pos = pos
#
#     def getPos(self):
#         return self.pos
#
#     def setColor(self, color):
#         self.color = color
#
#     def getColor(self):
#         return self.color
#
#     def isIn(self, x, y) -> bool:
#         return False
#
#
# class Square(Figure):
#     def __init__(self, pos, w, h) -> None:
#         super().__init__(pos)
#         self.w = w
#         self.h = h
#
#     def getWidth(self):
#         return self.w
#
#     def getHeight(self):
#         return self.h
#
#     def isIn(self, x, y) -> bool:
#         _pos = super().getPos()
#         if (_pos.x < x) and ((_pos.x + self.w) > x) and (_pos.y < y) and ((_pos.y + self.h) > y):
#             return True
#         return False
#
#
# # ----------------------------------
# class HitMark:
#     def __init__(self, cost) -> None:
#         self.setCost(cost)
#         self.setState(HitMark.State_Normal)
#
#     def setCost(self, cost):
#         self.cost = cost
#
#     def getCost(self):
#         return self.cost
#
#
# class SquareHitMark(Square, HitMark):
#     def __init__(self, pos, w, h, cost) -> None:
#         super().__init__(pos, w, h)
#         HitMark.setCost(self, cost)
#
#
# # ---------------------------------
# # класс внутриигрового сообщения
# class GameEvent:
#     # пустое событие
#     Event_None = 0
#     # событие таймера
#     Event_Tick = 1
#     # событие "выстрела" по цели
#     Event_Hit = 2
#
#     def __init__(self, type, data) -> None:
#         self.type = type
#         self.data = data
#
#     def getType(self):
#         return self.type
#
#     def getData(self):
#         return self.data
#
#
# class GameLogic:
#     def __init__(self, w, h) -> None:
#         self.gameboard_width = w
#         self.gameboard_height = h
#         self.marks = []
#         self.hitMarks = []
#         self.score = 0
#
#     def processEvent(self, event):
#         if event.type == GameEvent.Event_Tick:
#             markRandPos = Pos(rnd.randint(20, self.gameboard_width - 20)
#                               , rnd.randint(20, self.gameboard_height - 20))
#
#             markSize = rnd.randint(10, 20)
#             markCost = 30 - markSize
#             markColor = (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255))
#             mark = SquareHitMark(markRandPos, markSize, markSize, markCost)
#             mark.setColor(markColor)
#             self.addHitMark(mark)
#
#         if event.type == GameEvent.Event_Hit:
#             self.hit(event.data)
#
#     def addHitMark(self, mark):
#         self.marks.append(mark)
#
#     def hit(self, pos):
#         for markIndex in range(len(self.marks)):
#             mark = self.marks[markIndex]
#             if mark.isIn(pos.x, pos.y):
#                 self.score += mark.getCost()
#                 self.marks.pop(markIndex)
#                 self.hitMarks.append(mark)
#                 break
#
#     def getBoard(self):
#         return self.marks
#
#     def getScore(self):
#         return self.score
#
#
# # -----------------------------------------
# class PyGameGui:
#     def __init__(self, w, h, logic) -> None:
#         self.main_w = w
#         self.main_h = h
#         self.screen = pygame.display.set_mode([self.main_w, self.main_h])
#         self.logic = logic
#         self.font = pygame.font.SysFont('Consolas', 30)
#
#     def run(self):
#         running = True
#         pygame.time.set_timer(pygame.USEREVENT + GameEvent.Event_Tick, 1000)
#         while running:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#                 else:
#                     self.processEvent(event)
#
#             self.draw()
#
#     def processEvent(self, event):
#         if (event.type >= pygame.USEREVENT) and (event.type < pygame.NUMEVENTS):
#             myevent = GameEvent(event.type - pygame.USEREVENT, None)
#             self.logic.processEvent(myevent)
#
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             pypos = event.pos
#             myevent = GameEvent(GameEvent.Event_Hit, Pos(pypos[0], pypos[1]))
#             self.logic.processEvent(myevent)
#
#     def draw(self):
#         # Fill the background with white
#         self.screen.fill((255, 255, 255))
#
#         marks = self.logic.getBoard()
#         for mark in marks:
#             pygame.draw.rect(self.screen, mark.getColor(),
#                              pygame.Rect(mark.getPos().x, mark.getPos().y, mark.getWidth(), mark.getHeight()))
#
#         score = self.logic.getScore()
#         self.screen.blit(self.font.render(f'score:{score}', True, (0, 0, 0)), (32, 48))
#
#         # Flip the display
#         pygame.display.flip()
#
#
# # --------------------------------------------
# if __name__ == "__main__":
#     pygame.init()
#     width = 800
#     height = 600
#     gui = PyGameGui(width, height, GameLogic(width, height))
#     gui.run()
#     pygame.quit()
#
# Задание 3.3.7
# Задание на самопроверку.
#
# Вам нужно написать два модуля:
#
# Первый должен содержать число Пи в виде константы 3.14 и две функции,
# которые будут считать площадь круга и прямоугольника.
# Второй модуль должен импортировать первый, далее запрашивать у пользователя
# размеры круга и квадрата. В результате выводить, какая из фигур больше.
#
# from math import pi
# PI = pi
# def Circle_Square(r):
#     return PI * r * r
# def Square_Area(s):
#     return s * s
#
#
# from square import *
#
#
# def Compare():
#     a = int(input())
#     b = int(input())
#     if Circle_Square(a) > Square_Area(b):
#         print('Площадь круга больше')
#     else: print('Площадь квадрата больше')
#
#
# Compare()

# Задание 3.4.3
# Задание на самопроверку.
#
# Сделайте функцию, которая принимает от пользователя путь и выводит
# всю информацию о содержимом этой папки. Для реализации используйте
# функцию встроенного модуля os.walk(). Если путь не указан, то
# сравнение начинается с текущей директории.
#
# import os
#
#
# def walk_desc(path = None):
#     start_path = path if path is not None else os.getcwd()
#
#     for root, dirs, files in os.walk(start_path):
#         print("Текущая директория", root)
#         print("---")
#
#         if dirs:
#             print("Список папок", dirs)
#         else:
#             print("Папок нет")
#         print("---")
#
#         if files:
#             print("Список файлов", files)
#         else:
#             print("Файлов нет")
#         print("---")
#
#         if files and dirs:
#             print("Все пути:")
#         for f in files:
#             print("Файл ", os.path.join(root, f))
#         for d in dirs:
#             print("Папка ", os.path.join(root, d))
#         print("===")
#
#
# walk_desc()

# Задание 3.4.4
# Задание на самопроверку.
#
# Создайте любой файл на операционной системе под название input.txt и построчно перепишите его в файл output.txt.
#
# import os
# with open('input.txt', 'r', 'UTF-8') as input_file:
#     with open('output.txt', 'w', 'UTF-9') as output_file:
#         for line in input_file:
#             output_file.write(line)


# Задание 3.4.5
# Задание на самопроверку.
#
# Дан файл numbers.txt, компоненты которого являются действительными числами
# (файл создайте самостоятельно и заполните любыми числам, в одной строке одно число).
# Найдите сумму наибольшего и наименьшего из значений и запишите результат в файл output.txt.
#
#
# filename = 'numbers.txt'
# output = 'output.txt'
#
# with open(filename) as f:
#    min_ = max_ = float(f.readline())  # считали первое число
#    for line in f:
#        num =  float(line)
#        if num > max_:
#            max_ = num
#        elif num < min_:
#            min_ = num
#
#    sum_ = min_ + max_
#
# with open(output, 'w') as f:
#    f.write(str(sum_))
#    f.write('\n')
#
# Задание 3.4.6
# Задание на самопроверку.
#
# В текстовый файл построчно записаны фамилии и имена учащихся класса и их
# оценки за контрольную. Выведите на экран всех учащихся, чья оценка меньше 3 баллов. Cодержание файла:
#
# Иванов О. 4
# Петров И. 3
# Дмитриев Н. 2
# Смирнова О. 4
# Керченских В. 5
# Котов Д. 2
# Бирюкова Н. 1
# Данилов П. 3
# Аранских В. 5
# Лемонов Ю. 2
# Олегова К. 4
# Решение
# with open('input.txt', encoding="utf8") as file:
#     for line in file:
#         points = int(line.split()[-1])
#         if points < 3:
#             name = " ".join(line.split()[:-1])
#             print(name)

# Задание 3.4.7
# Задание на самопроверку.
#
# Выполните реверсирование строк файла (перестановка строк файла в обратном порядке).
#
# Решение
# with open('input.txt', 'r') as input_file:
#    with open('output.txt', 'w') as output_file:
#        for line in reversed(input_file.readlines()):
#            output_file.write(line)

#
# Задание 3.5.6
# Напишите контекстный менеджер, который умеет безопасно работать с файлами.
#
# В конструктор объекта контекстного менеджера передаются два аргумента: первый —
# путь к файлу, который надо открыть, второй — тип открываемого файла (для записи, для чтения и т. д.).
#
# При входе в контекстный менеджер должен открываться файл, и возвращаться объект для работы с этим файлом.
#
# При выходе из контекстного менеджера файл должен закрываться.
# (Эталоном работы можно считать контекстный менеджер open).
#
#
# class OpenFile:
#     def __init__(self, path, type):
#         self.file = open(path, type)
#
#     def __enter__(self):
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#
# with OpenFile('hello.txt', 'wt') as f:
#     f.write('Мой контекстный менеджер делает тоже самое!')

# Задание 4.4.5
# Задание на самопроверку.
#
# Модифицируйте функцию проверки баланса скобок для двух видов скобок: круглых и квадратных.
#
# Для реализации такого алгоритма может быть полезным создание словаря, в котором закрывающая
# скобка — ключ, открывающая — значение.
#
# pars = {")": "(", "]": "["}
#
#
# def par_checker_mod(string):
#     stack = []
#
#     for s in string:
#         if s in "([":
#             stack.append(s)
#         elif s in ")]":
#             if len(stack) > 0 and stack[-1] == pars[s]:
#                 stack.pop()
#             else:
#                 return False
#     return len(stack) == 0
#
# Очередь
#
# Задание 4.4.6
# Задание 4.4.7
# Задание 4.4.8
# Задание 4.4.9
# Задание 4.4.10
#
#
# # Создадим класс Queue - нужная нам очередь
# class Queue:
#     # Конструктор нашего класса, в нём происходит нужная инициализация объекта
#     def __init__(self, max_size):
#         self.max_size = max_size  # размер очереди
#         self.task_num = 0  # будем хранить сквозной номер задачи
#
#         self.tasks = [0 for _ in range(self.max_size)]  # инициализируем список с нулевыми элементами
#         self.head = 0  # указатель на начало очереди
#         self.tail = 0  # указатель на элемент следующий за концом очереди
#
#     # !!! Класс далее нужно дополнить методами !!!
#     def is_empty(self):  # очередь пуста?
#         # да, если указатели совпадают и в ячейке нет задачи
#         return self.head == self.tail and self.tasks[self.head] == 0
#
#     def size(self):  # получаем размер очереди
#         if self.is_empty():  # если она пуста
#             return 0  # возвращаем ноль
#         elif self.head == self.tail:  # иначе, если очередь не пуста, но указатели совпадают
#             return self.max_size  # значит очередь заполнена
#         elif self.head > self.tail:  # если хвост очереди сместился в начало списка
#             return self.max_size - self.head + self.tail
#         else:  # или если хвост стоит правее начала
#             return self.tail - self.head
#
#     def add(self):
#         self.task_num += 1  # увеличиваем порядковый номер задачи
#         self.tasks[self.tail] = self.task_num  # добавляем его в очередь
#         print(f"Задача №{self.tasks[self.tail]} добавлена")
#
#         # увеличиваем указатель на 1 по модулю максимального числа элементов
#         # для зацикливания очереди в списке
#         self.tail = (self.tail + 1) % self.max_size
#
#     def show(self):  # выводим приоритетную задачу
#         print(f"Задача №{self.tasks[self.head]} в приоритете")
#
#     def do(self):  # выполняем приоритетную задачу
#         print(f"Задача №{self.tasks[self.head]} выполнена")
#         # после выполнения зануляем элемент по указателю
#         self.tasks[self.head] = 0
#         # и циклично перемещаем указатель
#         self.head = (self.head + 1) % self.max_size
#
#
# # Используем класс
# size = int(input("Определите размер очереди: "))
# q = Queue(size)
#
# while True:
#     cmd = input("Введите команду:")
#     if cmd == "empty":
#         if q.is_empty():
#             print("Очередь пустая")
#         else:
#             print("В очереди есть задачи")
#     elif cmd == "size":
#         print("Количество задач в очереди:", q.size())
#     elif cmd == "add":
#         if q.size() != q.max_size:
#             q.add()
#         else:
#             print("Очередь переполнена")
#     elif cmd == "show":
#         if q.is_empty():
#             print("Очередь пустая")
#         else:
#             q.show()
#     elif cmd == "do":
#         if q.is_empty():
#             print("Очередь пустая")
#         else:
#             q.do()
#     elif cmd == "exit":
#         for _ in range(q.size()):
#             q.do()
#         print("Очередь пустая. Завершение работы")
#         break
#     else:
#         print("Введена неверная команда")
#
# Задание 4.5.1
# Задание 4.5.2
# Задание 4.5.3
#
# G = {
#     "Адмиралтейская": {
#         "Садовая": 4},
#     "Садовая": {
#         "Сенная площадь": 4,
#         "Спасская": 3,
#         "Адмиралтейская": 4,
#         "Звенигородская": 5},
#     "Сенная площадь": {
#         "Садовая": 4,
#         "Спасская": 4},
#     "Спасская": {
#         "Садовая": 3,
#         "Сенная площадь": 4,
#         "Достоевская": 6},
#     "Звенигородская": {
#         "Пушкинская": 3,
#         "Садовая": 5},
#     "Пушкинская": {
#         "Звенигородская": 3,
#         "Владимирская": 4},
#     "Владимирская": {
#         "Достоевская": 3,
#         "Пушкинская": 4},
#     "Достоевская": {
#         "Владимирская": 3,
#         "Спасская": 6}
# }
# D = {k : 100 for k in G.keys()}  # расстояния
# start_k = 'Адмиралтейская'  # стартовая вершина
# D[start_k] = 0  # расстояние от нее до самой себя равно нулю
# U = {k : False for k in G.keys()}  # флаги просмотра вершин
# P = {k : None for k in G.keys()}  # предки
#
# for _ in range(len(D)):
#     # выбираем среди непросмотренных наименьшее по расстоянию
#     min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])
#
#     for v in G[min_k].keys():  # проходимся по всем смежным вершинам
#          if D[v] > D[min_k] + G[min_k][v]:  # если расстояние от текущей вершины меньше
#             D[v] = D[min_k] + G[min_k][v]  # то фиксируем его
#             P[v] = min_k  # и записываем как предок
#     U[min_k] = True  # просмотренную вершину помечаем


1.13