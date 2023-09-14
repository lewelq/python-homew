def backpack(items, max_weight):
    possible = []
    for item, weight in items.items():
        if weight <= max_weight:
            possible.append(item)
            max_weight -= weight
    return possible
items = {"Одежда": 4, "Еда": 2, "Вода": 1, "Обувь": 4}
max_weight = 10
print (backpack(items, max_weight))