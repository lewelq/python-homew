from random import randint

listd = [randint(0, 10) for i in range (10)]
print(listd)
list_new = []
for j in range (10):
    if listd.count(j) > 1:
        list_new.append(j)
print(list_new)

