alphabet = 'abcdefghijklmnopqrstuvwxyz'
cipher_key = alphabet[::-1]
def encode(plain_text):
    cipher = ''
    counter = 0
    for char in plain_text:
        if char.isalpha():
            if counter  ==  5:
                cipher += ' '
                counter = 0
            index = alphabet.index(char.lower())
            cipher += cipher_key[index] 
            counter += 1
            
        elif char.isnumeric():
            if counter == 5:
                cipher += ' '
                counter = 0
            cipher += char
            counter += 1
            
            

    return cipher


def decode(ciphered_text):
    plain_text = ''

    for char in ciphered_text:
        if char.isalpha():
            index = cipher_key.index(char.lower())
            plain_text += alphabet[index]
        elif char.isnumeric():
            plain_text += char
        
    return plain_text
