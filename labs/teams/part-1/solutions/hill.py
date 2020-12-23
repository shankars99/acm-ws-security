import numpy as np
import math
import functools

from fractions import Fraction

def to_matrix(inp_text):

    inp_text = [ ord(i) for i in inp_text]

    plain_matrix = np.array( [ [inp_text[0], inp_text[1] ],
                               [inp_text[2], inp_text[3] ] ] )

    return plain_matrix

def to_charmatrix(inp_text):

    plain_matrix = [[ chr(inp_text[0][0]), chr(inp_text[0][1]) ],
                    [ chr(inp_text[1][0]), chr(inp_text[1][1]) ] ]

    plain_string = chr(inp_text[0][0]) + chr(inp_text[0][1]) + chr(inp_text[1][0]) + chr(inp_text[1][1])

    return plain_string


def encode(plain_matrix, key_matrix):
    cipher_matrix = np.dot(plain_matrix, key_matrix )
    cipher_matrix_format = cipher_matrix%26 +65
    return cipher_matrix, cipher_matrix_format

def decode(cipher_matrix, key):
    key_matrix_inv =  np.linalg.inv(key_matrix)
    plain_matrix = np.dot(cipher_matrix, key_matrix_inv)
    return(np.round(plain_matrix))


def change_size_key(key, new_size):
    return (key * (new_size//len(key) + 1))[:new_size]

inp = input("\nEnter the text:")
key = input("Enter the key:")

input_text = inp.upper()
key        = key.upper()
key        = change_size_key(key, len(input_text))

plain_matrix = to_matrix(input_text)
key_matrix = to_matrix(key)

cipher, cipher_matrix_format = encode(plain_matrix, key_matrix)
print("\nEncoded message: " + to_charmatrix(cipher_matrix_format))
plain = decode(cipher, key)
print("Decoded message: " + to_charmatrix(plain.astype(int)))
