'''
Задача 1. Первый уникальный символ
Дана строка. Нужно найти индекс первого символа, 
который встречается ровно один раз. Если такого нет: вернуть -1.

Symbol: Перый, самый простой в реализации способ, но будет тормозить если строка большая
Сложность O(n^2)

Symbol1: Самый оптимизированный способ, но менее читабельный. 
Используется словарь known для запоминания уже встреченных символов и их индекс.
Сложность O(n + k), n - размер строки, k - размер уникальных символов

Symbol2: Самое лучшее решение - способ тот же как и в Symbol1 только более читабельный
Сложность побольше - O(2n)
'''

from collections import Counter

def Symbol(stroke):
    for i in stroke:
        if stroke.count(i) == 1:
            return stroke.index(i)
    return -1

def Symbol1(stroke):
    known = {}
    for i in range(len(stroke)):
        if stroke[i] not in known:
            known[stroke[i]] = [1, i]
            continue
        known[stroke[i]][0] += 1
    for i in known:
        if known[i][0] == 1:
            return known[i][1]
    return -1

def Symbol2(stroke):
    counts = Counter(stroke)
    for i, ch in enumerate(stroke): # i - index, ch - буква
        if counts[ch] == 1:
            return i
    return -1

symbols = input()
print(Symbol(symbols))
print(Symbol1(symbols))
print(Symbol2(symbols))