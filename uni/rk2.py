alphabet = 'abcdefghijklmnopqrstuvwxyz'

def vigenere_cipher(text, key: str):
    
    '''Шифрование'''

    result = ''
    key_index = 0
    for char in text:
        shift = alphabet.index(key[key_index])
        result += alphabet[(alphabet.index(char) + shift) % len(alphabet)]
        key_index = (key_index + 1) % len(key)
    return result

def vigenere_decipher(text, key: str):

    '''Дешифрование'''

    result = ''
    key_index = 0
    for char in text:
        shift = alphabet.index(key[key_index])
        result += alphabet[(alphabet.index(char) - shift) % len(alphabet)]
        key_index = (key_index + 1) % len(key)
    return result

# Пример использования
message = "secretmessage"
keyword = "key"
encrypted_message = vigenere_cipher(message, keyword)
print(encrypted_message)

print(vigenere_decipher('kffpavhkbnhr', 'key'))