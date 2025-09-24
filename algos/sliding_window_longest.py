'''
Задача 2. Длина самой длинной подстроки без повторяющихся символов
Дана строка. Нужно найти максимальную длину подстроки, в которой все символы разные.
'''

def Max_Length(line):
    max_l, temp = 0, 0
    length_word = len(line)
    for i in range(length_word):
        temp = 0
        known = []
        for j in range(i, length_word):
            if line[j] in known:
                break
            known.append(line[j])
            temp += 1
            if j == length_word - 1:
                i = length_word - 1
                break
        if temp > max_l: 
            max_l = temp
    return max_l

def Max_Length1(line):
    size, start = 0, 0
    known = {}
    for i, ch in enumerate(line):
        if ch in known and known[ch] >= start:
            start = known[ch] + 1
        known[ch] = i
        size = max(size, i - start + 1)
    return size

line = input()
print(Max_Length(line))
print(Max_Length1(line))

