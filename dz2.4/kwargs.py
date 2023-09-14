def create_dict(**kwargs):
    result_dict = {}
    for key, value in kwargs.items():
        if not hash(key):
            key = str(key)
        result_dict[value] = key
    return result_dict

result = create_dict(fdsf="1233", keyyy="[13,12]", xss3="value3")
print(result)
