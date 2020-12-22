import numpy as np
import math
import functools

from fractions import Fraction

def to_matrix(inp_text):

    inp_text = [ ord(i) for i in inp_text]

    plain_matrix = np.array( [ [inp_text[0], inp_text[1] ],
                               [inp_text[2], inp_text[3] ] ] )

    return plain_matrix

def calc_lcm(matrix):
    list_matrix = [ matrix[0][1], matrix[0,0], matrix[1][0], matrix[1,1]]
    matrix_denom = []
    for x in list_matrix:
        t = str(Fraction(x).limit_denominator())
        matrix_denom.append(int(t[t.find('/')+1:]))

    lcm = functools.reduce(math.lcm, matrix_denom)
    return lcm

def to_charmatrix(inp_text):

    plain_matrix = [[ chr(inp_text[0][0]), chr(inp_text[0][1]) ],
                    [ chr(inp_text[1][0]), chr(inp_text[1][1]) ] ]

    plain_string = chr(inp_text[0][0]) + chr(inp_text[0][1]) + chr(inp_text[1][0]) + chr(inp_text[1][1])

    return plain_string


def encode(plain_text, key):
    plain_matrix = to_matrix(plain_text)
    print(plain_matrix)
    key_matrix = to_matrix(key) -65
    cipher_matrix = np.dot(plain_matrix, key_matrix )
    cipher_matrix_format = cipher_matrix% 26 + 65
    #cipher_matrix = to_charmatrix(cipher_matrix.astype(int))
    return cipher_matrix, cipher_matrix_format

def decode(cipher_matrix, key):
    #cipher_matrix = to_matrix(cipher_text)
    key_matrix     = to_matrix(key)
    key_matrix_inv =  np.linalg.inv(key_matrix)
    lcm            = calc_lcm(key_matrix_inv)

    key_matrix_inv = np.round_(key_matrix_inv*lcm % 26)
    print(key_matrix_inv)
    print(lcm)
    plain_matrix = (26-np.dot(cipher_matrix, key_matrix_inv)%26).astype(int) +65
    #plain_matrix = to_charmatrix(plain_matrix)
    return plain_matrix


def change_size_key(key, new_size):
    return (key * (new_size//len(key) + 1))[:new_size]

inp = input("\nEnter the text:")
key = input("Enter the key:")

input_text = inp.upper()
key        = key.upper()
key        = change_size_key(key, len(input_text))

cipher, cipher_matrix_format = encode(input_text, key)
print("Encoded message: " + to_charmatrix(cipher_matrix_format))
print(cipher)
plain = decode(cipher, key)
print(plain)
