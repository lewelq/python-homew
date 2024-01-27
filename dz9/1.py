import os
from random import randint
import csv
import json
from math import sqrt


def deco(path):
    def csv_read(func):
        with open(path, "r", encoding='utf-8') as file:
                reader = csv.reader(file)
        def wrapper(*args, **kwargs):
                for row in reader:
                    func(*args, **kwargs)
        return wrapper
    return csv_read
                    
def to_json(path):
    def inner(func):
        def wrapper(*args, **kwargs):
            with open(path, "w") as file:
                writer = json.dump(func(*args, **kwargs), file)
        return wrapper
    return inner

@deco("dz9/numbers.csv")
@to_json("dz9/js.json")
def quad(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-(b) + sqrt(D)) / (2 * a)
        x2 = (-(b) - sqrt(D)) / (2 * a)
        return x1, x2
    elif D == 0:
        x = -(b) / (2 * a)
        return x
    else:
        return "error"

def csv_write():
    strings_count = randint(100, 1000)
    with open("dz9/numbers.csv", 'w', newline = '', encoding='utf-8') as file:
        writer = csv.writer(file)
        for i in range(strings_count):
            row = [randint(1, 100) for j in range(3)]
            writer.writerow(row)
            
            
csv_write()


            
