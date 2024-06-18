def decor(func):
    def wrapper():
        print('some text')
        func()
        print('end text')
    return wrapper

@decor
def somefunc():
    print('the text')

somefunc()