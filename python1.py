#1
for i in range(2, 10):
    for j in range(2, 11):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()
#2
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))
if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
    if a == b == c:
        print("Треугольник равносторонний")
    elif a == b or a == c or b == c:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")
else:
    print("Треугольник не существует")
#3
num = int(input("Введите число от 2 до 100000: "))

if num <= 1 or num > 100000:
    print("Число должно быть в диапазоне от 2 до 100000")
else:
    x = True
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            x = False
            break

    if x:
        print("Число является простым")
    else:
        print("Число является составным")
#4
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)

for i in range(10):
    guess = int(input("Угадайте число от 0 до 1000: "))
    if guess == num:
        print("Поздравляем, вы угадали число!")
        break
    elif guess < num:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")

if i == 9:
    print("Вы исчерпали все попытки. Загаданное число было", num)