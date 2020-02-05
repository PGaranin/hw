#!/usr/bin/python
# -*- coding: utf-8 -*-
 
#Задача с именами

f = open('taskName/names.txt', 'r')

sourse = [line.replace('"','').split(',') for line in f]
res = []
for arr in sourse:
    res += arr

#1) Отсортировать все имена в лексикографическом порядке
res.sort()

#2) Посчитать для каждого имени алфавитную сумму – сумму порядковых номеров букв (MAY: 13 + 1 + 25 = 39)
def alphabetical_amount(name):
    sum = 0
    for character in name:
        sum += ord(character) - 64
    return sum
#3) Умножить алфавитную сумму каждого имени на порядковый номер имени в отсортированном списке (индексация начинается с 1). Например, если MAY находится на 63 месте в списке, то результат для него будет 63 * 39 = 2457.
#4) Просуммировать произведения из п. 3 для всех имен из файла и получить число. Это число и будет ответом.
answer = 0
for i in range(len(res)):
    answer += (i+1)*alphabetical_amount(res[0])

print(answer)

