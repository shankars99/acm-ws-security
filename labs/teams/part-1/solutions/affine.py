def modinv(a, m):
    mod_inv = pow(a, -1, m)

    return mod_inv


def enc(text, key):
    return ''.join([chr(((key[0]*(ord(t) - ord('A')) + key[1]) % 26)
                        + ord('A')) for t in text.upper().replace(' ', '')])

def dec(cipher, key):
    return ''.join([chr(((modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
                         % 26) + ord('A')) for c in cipher])


option = input("\n1. Encode\n2. Decode\nEnter your option:")

text = input("Enter the text:")
key_raw  = (input("Enter the key pair:").split(" "))

key = [int(i) for i in key_raw]

print(key)
if option == '1':
    cipher = enc(text, key)
    print(cipher)
else:
    plain  = dec(text, key)
    print(plain)
