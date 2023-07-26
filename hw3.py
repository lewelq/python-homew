#22
'''n = int(input("Введите количество элементов массива 1: "))
m = int(input("Введите количество элементов массива 2: "))
a = []
b = []
for i in range (n):
    y = int(input(f"Введите число массива 1 номер {i+1}: "))
    a.append(y)
for x in range (m):
    z = int(input(f"Введите число массива 2 номер {i+2}: "))
    b.append(z)    
s = a + b
print(set(sorted(s)))'''
#24
n = int(input())
a = []
for i in range (n):
    y = int(input(f"Введите число массива номер {i+1}: "))
    a.append(y)
max_berry = [a[i] + a[i-1] + a[(i+1)%n] for i in range(n)]
max_sum = max(max_berry)
print(max_sum)
