def enc(plain_text, key):
    cipher_text = ""
    for plain_char in plain_text:
        shift_char = ord(plain_char) + key - ord('A')
        cipher_char = chr((shift_char) % 26 + ord('A'))
        cipher_text += cipher_char

    return(cipher_text)


def dec(cipher_text, key):
    plain_text = ""
    for cipher_char in cipher_text:
        shift_char = ord(cipher_char) - key % 26
        if shift_char < ord('A'):
            shift_char = ord('Z') - (ord('A') - shift_char) + 1
        plain_char = chr(shift_char)
        plain_text += plain_char
    return(plain_text)


inp = input("\nEnter the text:")

input_text = inp.upper()


for key in range(25):
    cipher = dec(input_text, key)
    print(cipher)
