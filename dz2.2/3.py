import fractions

a = int(input("Числитель первой дроби:"))
b = int(input("Знаменатель первой дроби:"))
c = int(input("Числитель второй дроби:"))
d = int(input("Знаменатель второй дроби:"))
if b == 0 or d == 0:
    print("Неверный ввод!")
else:
    f1 = fractions.Fraction(a, b)
    f2 = fractions.Fraction(c, d)
    print("Дроби:", f1, f2)
    summ = f1 + f2
    prod = f1 * f2
    print("Сумма дробей =", summ)
    print("Произведение дробей =", prod)