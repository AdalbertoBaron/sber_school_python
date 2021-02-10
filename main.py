# -*- coding: utf-8 -*-
# import tests_1 as test
from __future__ import print_function

# def find_min(var_1, var_2):
#     if (var_1 < var_2):
#       min = var_1
#     else:
#       min = var_2
#     return min

# if __name__ == '__main__':

#     for i in test.cases:
#         if find_min(i[1], i[2]) == i[3]:
#             print("Test #" + str(i[0]) + ': OK!')
#         else:
#             print("Test #" + str(i[0]) + ': KO!')


#																					ЦИКЛЫ

# # Допишите функцию, которая принимает массив из 10 чисел и возвращает их сумму.
# import tests as test

# # Функция find_sum принимает массив чисел mass
# # Необходимо произвести сумму чисел массива
# # Результат необходимо присвоить переменной sum

# def find_sum(mass):
#     #Вставьте свой код ниже
# 	j = 0
# 	sum = 0
# 	while (j < 10):
# 		sum += mass[j]
# 		j += 1
# 	return sum

# if __name__ == '__main__':

#     for i in test.cases:
#         if find_sum(i[1]) == i[2]:
#             print("Test #" + str(i[0]) + ': OK!')
#         else:
#             print("Test #" + str(i[0]) + ': KO!')




# # Допишите функцию, которая принимает массив чисел и возвращает количество чисел равных нулю.

# import tests1 as test

# # Функция find_null принимает массив чисел mass
# # Необходимо произвести подсчет количества чисел массива равных нулю
# # Результат необходимо присвоить переменной sum

# def find_null(mass):
#     #Вставьте свой код ниже
# 	sum = 0
# 	j = 0
# 	for j in mass:
# 		if j == 0:
# 			sum += 1
# 	return sum

# if __name__ == '__main__':

#     for i in test.cases:
#         if find_null(i[1]) == i[2]:
#             print("Test #" + str(i[0]) + ': OK!')
#         else:
#             print("Test #" + str(i[0]) + ': KO!')




# # Напишите программу, в которой задается  натуральное число n и выводится лестница из n ступенек,
# # i-я ступенька должна состоять из чисел от 1 до i без пробелов.

# #Вставьте свой код ниже
# i = 0
# n = 10
# j = 0
# range(1, n)
# while (i < n):
#   for j in range(1, i+1):
#     print(j, end='')
#   if (i != 0):
#     print(' ')
#   i += 1




# #Напишите программу, в которой задается натуральное число n и выводится пирамида из n ступенек,
# # i-я ступень должна состоять из чисел от 1 до i и обратно без пробелов.

# i = 0
# n = 6
# j = 0
# h = 0
# range(1, n)
# while (i < n):
#   for j in range(1, n - i):
#     print(' ', end='')
#   for j in range(1, i + 2):
#     print(j, end='')
#   if i > 0:
#     j -= 1
#     while (j > 0):
#       print(j, end='')
#       j -= 1
#   print(' ')
#   i += 1




# # Напишите программу, в которой задается натуральное число n и выводится ромб из n*2-1 ступенек,
# # i-я ступень должна состоять из чисел от 1 до i и обратно без пробелов.

# i = 0
# n = 6
# j = 0
# h = 0
# range(1, n)
# while (i < n):
#   for j in range(1, n - i):
#     print(' ', end='')
#   for j in range(1, i + 2):
#     print(j, end='')
#   if i > 0:
#     j -= 1
#     while (j > 0):
#       print(j, end='')
#       j -= 1
#   print(' ')
#   i += 1

# i = 0
# while (i < n - 1):
#   k = 0
#   while (k <= i):
#     print(' ', end='')
#     k += 1
#   j = n - i
#   for h in range(1, n - i):
#     print(h, end='')
#   while (h > 0):
#     h -= 1
#     if (h != 0):
#       print(h, end='')
#   print(' ')
#   i += 1




# Бонусное задание будет поделено на 4 варианта.

i = 0
n = 6
j = 0
h = 0
range(1, n)
while (i < n):
  for j in range(1, n - i):
    print(' ', end='')
  for j in range(1, i + 2):
    print(j, end='')
  print(' ')
  i += 1

i = 0
while (i < n - 1):
  k = 0
  while (k <= i):
    print(' ', end='')
    k += 1
  j = n - i
  for h in range(1, n - i):
    print(h, end='')
  print(' ')
  i += 1