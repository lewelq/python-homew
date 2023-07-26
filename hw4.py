#30
'''first = int(input("Введите первый элемент прогрессии: "))
razn = int(input("Введите разность прогрессии: "))
count = int(input("Введите количество элементов прогрессии: "))

a = [first + (i-1) * razn for i in range(1, count+1)]

print("Арифметическая прогрессия:", a)'''
#32
progression = [4, 7, 564, 4544, 10000]
minn = int(input("Минимальное значение диапазона: "))
maxx = int(input("Максимальное значение диапазона: "))

a = [i for i in range(len(progression)) if minn <= progression[i] <= maxx]

print("Индексы элементов:", a)