def enc_vig_char(plain_char, key):
    cipher_char = ""

    shift_char = ord(plain_char) + ord(key) - 2*ord('A')
    cipher_char = chr((shift_char) % 26 + ord('A'))

    return(cipher_char)

def dec_vig_char(cipher_char, key):
    plain_char = ""

    shift_char = ord(cipher_char) - ord(key)
    plain_char = chr((shift_char) % 26 + ord('A'))

    return(plain_char)



def enc(plain_text, key):
    cipher_text = ""
    for i in range(len(plain_text)):
        cipher_text += enc_vig_char(plain_text[i], key[i])

    return cipher_text

def dec(cipher, key):
    plain_text = ""
    for i in range(len(cipher)):
        plain_text += dec_vig_char(cipher[i], key[i])
    return plain_text

def change_size_key(key, new_size):
    return (key * (new_size//len(key) + 1))[:new_size]


option = input("\n1. Encode\n2. Decode\nEnter your option:")

inp = input("\nEnter the text:").upper()
key = input("Enter the key:").upper()

key = change_size_key(key, len(inp))

if option == '1':
    cipher = enc(inp, key)
    print("\nEncoding is=" + cipher)
else:
    plain = dec(inp, key)
    print("Decoding is=" + plain)
