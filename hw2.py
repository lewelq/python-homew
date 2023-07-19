#10
'''data = input().split() 
gerb = data.count('0') 
reshka = data.count('1') 
if gerb > reshka:
    print(reshka)
elif gerb < reshka:
    print(gerb)
else:
    print(0)'''
#12
'''summ = int(input("Введите сумму: "))
proizv = int(input("Введите произведение: "))
for i in range (1000):
    for n in range (1000):
        if (i + n == summ) and (i * n == proizv):
            print (i, n)
        else:
            n += 1
    i += 1'''
#14
n = int(input())
k = 0
while 2**k < n:
    print(2**k)
    k += 1