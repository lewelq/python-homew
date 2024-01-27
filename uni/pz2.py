alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' # len = 32

def encryption(message, key):

    '''Функция шифрования'''

    encrypted_message = ''
    for i in message:
        if i in alphabet:
            index = (alphabet.index(i) + key) % len(alphabet)
            encrypted_message += alphabet[index]
        else:
            raise NameError('Символа нет в алфавите!')
    return encrypted_message

def decryption(message, key):

    '''Функция дешифрования'''

    decrypted_message = ''
    for i in message:
        if i in alphabet:
            index = (alphabet.index(i) - key) % len(alphabet)
            decrypted_message += alphabet[index]
        else:
            raise NameError('Символа нет в алфавите!')
    return decrypted_message

def hack(message):

    ''' Функция взлома'''

    for i in range(len(alphabet)):
        decrypted_message = ''
        for j in message:
            if j in alphabet:
                index = (alphabet.index(j) - i) % len(alphabet)
                decrypted_message += alphabet[index]
            else:
                raise NameError('Символа нет в алфавите!')
        print(decrypted_message)
    
print(encryption('яблоко', 8))
print(encryption('алфавит', 16))
print(encryption('слово', 5))

print(decryption('жиуцтц', 8))
print(decryption('пыдпсшв', 16))
print(decryption('цружу', 5))

hack('пыдпсшв')