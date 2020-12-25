def transposition(key, order, order_name):
    new_key = ""
    for pos in order:
        new_key += key[pos-1]

    print("Permuted "+ order_name +" = "+ new_key)
    return new_key


def P10(key):
    P10_order = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    P10_key = transposition(key, P10_order, "P10")

    return P10_key


def P8(LS1_key):
    P8_order = [6, 3, 7, 4, 8, 5, 10, 9]
    P8_key = transposition(LS1_key, P8_order, "P8")

    return P8_key

def LS1(P10_key):
    P10_key_left = P10_key[:5]
    P10_key_right = P10_key[5:]

    LS1_key_left = P10_key_left[1:5] + P10_key_left[0]
    LS1_key_right = P10_key_right[1:5] + P10_key_right[0]

    LS1_key = LS1_key_left+LS1_key_right
    #print("LS-1 = " + LS1_key)
    return LS1_key


def IP(LS1_key):
    IP_order = [2, 6, 3, 1, 4, 8, 5, 7]
    IP_key = transposition(LS1_key, IP_order, "IP")

    return IP_key

def IP_inv(LS1_key):
    IP_inv_order = [4, 1, 3, 5, 7, 2, 8, 6]
    IP_inv_key = transposition(LS1_key, IP_inv_order, "IP-1")

    return IP_inv_key

def key_gen(key):
    LS1_key = LS1(P10(key))

    key_1 = P8(LS1_key)
    key_2 = P8(LS1(LS1_key))

    #print("Key-1:"+ key_1 +"\nKey-2:"+ key_2)
    return (key_1,key_2)

def encrypt_plain(plain_text):
    enc = IP(plain_text)
    dec = IP_inv(enc)

    #print("ENC:"+ enc +"\nDEC:"+ dec)
    return(enc, dec)

def f_key(enc_plain, SK):
    L = enc_plain[:4]
    R = enc_plain[4:]
    F = F_func(R, SK)
    #print(L)
    #print(R)
    f = A_xor_B(L, SK) + R
    #print(f)
    return f


def F_func(R, SK):
    EP_order = [4, 1, 2, 3, 2, 3, 4, 1]
    EP_key   = transposition(R, EP_order, "EP")
    P        = A_xor_B(EP_key, SK)
    P4       = s_box(P)
    return P4

def A_xor_B(A,B):
    bit_xor = ""
    for i in range(len(A)):
        bit_xor += str  ( int(A[i]) ^ int(B[i]) )
    #print(bit_xor)
    return bit_xor

def s_box(P):
    P0 = P[:4]
    P1 = P[4:]

    S0_order = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
    S1_order = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]
    P4_order = [2, 4, 3, 1]

    S0 = sbox_calc(P0, S0_order)
    S1 = sbox_calc(P1, S1_order)

    P4 = transposition( S0+S1, P4_order, "P4" )

    #print(P4)
    return P4


def sbox_calc(P, S):
    row = int( (P[0] + P[3]) , 2 )
    col = int( (P[1] + P[2]) , 2 )

    s_val = bin(S[row][col])[2:].zfill(2)

    return(s_val)

def SW(key):
    key_new = key[:4] + key[4:]
    #print(key_new)
    return key_new


option = input("\n1. Encode\n2. Decode\nEnter your option:")

key = input("Enter the key:")
inp = input("Enter the text:")

key_1, key_2 = key_gen(key)
#enc_plain, dec_plain = encrypt_plain(plain_text)

if option == '1':
    print()
    IP_1 = IP(inp)
    fk_1 = f_key(IP_1, key_1)
    switch = SW(fk_1)
    fk_2 = f_key(switch, key_2)
    IP_2 = IP_inv(fk_2)

    print("\nEncoded = " + IP_2)
else:
    print()
    plain_text = inp
    IP_1 = IP(plain_text)
    fk_2 = f_key(IP_1, key_2)
    switch = SW(fk_2)
    fk_1 = f_key(switch, key_1)
    IP_2 = IP_inv(fk_1)

    print("\nDecoded = " + IP_2)
