
def s_box_transposition(inp_box, order, order_name):

    new_inp = [ [],[] ]

    for row in range(len(inp_box)):
        for char in range(len(inp_box[row])):
            val = int(inp_box[row][char], 2)
            new_inp[row].append(order[val])

    transpose_display(order_name, new_inp)
    return new_inp


def MC_box_transposition(inp_box, MC_box_order, order_name = "MC"):
    MC_new_box = [ [],[] ]

    for r_num in range(len(inp_box)):
        val = inp_box[0][r_num] + inp_box[1][r_num]

        for row in range(len(MC_box_order)):
            val_code_transform=""
            for MC_transform in MC_box_order[row]:
                val_transform = 0
                for MC_code in MC_transform:
                    val_transform = val_transform ^ int(val[int(MC_code)])
                val_code_transform += str(val_transform)
            MC_new_box[row].append(val_code_transform)


    transpose_display(order_name, MC_new_box)
    return(MC_new_box)

def get_s_box():
    s_box_order = ["1001", "0100", "1010", "1011",
                   "1101", "0001", "1000", "0101",
                   "0110", "0010", "0000", "0011",
                   "1100", "1110", "1111", "0111"]
    return s_box_order

def s_box(inp_box, inp_name = "S-Box"):
    s_box_order = get_s_box()
    s_box_key = s_box_transposition(inp_box, s_box_order, inp_name)
    return s_box_key

def SR(inp):
    inp[1][0], inp[1][1] = inp[1][1], inp[1][0]
    transpose_display("SR", inp)
    return inp


def MC(inp_box):
    MC_box_order = [ ["06", "147", "245", "35"],
                     ["24", "035", "016", "17"] ]
    MC_box_key = MC_box_transposition(inp_box, MC_box_order)
    return MC_box_key


def transpose_display(order_name, inp_box):
    print(order_name + ":")

    for row in inp_box:
        print(row)
    print()

def SN(inp_box):
    SN_box = get_s_box()
    new_inp = []
    for char in range(len(inp_box)):
        val = int(inp_box[char], 2)
        new_inp.append(SN_box[val])
    print("\nSN:")
    print(new_inp)
    return(new_inp)

def key_gen(key):
    w = [ [key[0], key[1]], [key[2], key[3]] , []]
    keys = [ key[0]+key[1], "", "" ]

    r_con = [["1000", "0000"],[ "0011","0000"] ]

    w_new = SR(w)

    sn = SN(w_new[1])

    print("\nRound constant")
    y = RC(sn, r_con[0])

    print("\nW0 ^ W2")
    y = t = RC(w_new[0], y)
    keys[1] = keys[1].join(y)

    print("\nW1 ^ W3")
    y = q = RC(sn,y)
    w[2] = y
    keys[0] = keys[0] + "".join(sn)
    keys[1] = keys[1] + "".join(y)

    w[0] = w[1]
    w[1] = w[2]
    w_new = SR(w)

    sn = SN(w_new[1])

    print("\nRound constant")
    y = RC(sn, r_con[1])

    print("\nW2 ^ W4")
    y = RC(y, t)
    keys[2] = "".join(y)

    print("\nW3 ^ W5")
    print(q[::-1])
    y = RC(q[::-1], y)
    keys[2] = keys[2] + "".join(y)

    print("\nKeys = ")
    print(keys)

    return keys

def RC(x, r_con):
    rc = [A_xor_B(x[0], r_con[0]), A_xor_B(x[1], r_con[1])]
    #print("\nRC = ")
    print(rc)
    return rc

def A_xor_B(A, B):
    bit_xor = ""
    for i in range(len(A)):
        bit_xor += str(int(A[i]) ^ int(B[i]))
    #print(bit_xor)
    return bit_xor

def key_to_list(key):
    key_list = [key[:4], key[8:12], key[4:8], key[12:16]]
    print(key_list)
    return key_list

def list_xor(A, B):
    res = [[],[]]
    for i in range(4):
        #print(A[i//2][i%2] + "^" + B[i])
        res[i//2].append(A_xor_B(A[i//2][i % 2], B[i]))
    return res

def MC_inv():
    MC_box_order = [["2", "4", "6", "8", "A", "C", "E", "3", "1", "7", "5", "B", "9", "F", "D"],
                    ['4', '8', 'C', '3', '7', 'B', 'F', '6', '2', 'E', 'A', '5', '1', 'D', '9'],
                    ['9', '1', '8', '2', 'B', '3', 'A', '4', 'D', '5', 'C', '6', 'F', '7', 'E']]
    
    return MC_box_order

def enc(inp, keys):
    AK1 = list_xor(inp, key_to_list(keys[0]) )
    print(AK1)
    inp = s_box(AK1)
    inp = SR(inp)
    inp = MC(inp)

    AK2 = list_xor(inp, key_to_list(keys[1]))
    print(AK2)
    inp = s_box(AK2)
    inp = SR(inp)

    AK3 = list_xor(inp, key_to_list(keys[2]))
    print("Encoded")
    for row in AK3:
        print(row)


key = ["1010", "0111", "0011", "1011"]
inp = [["0110", "0110"], ["1111", "1011"]]
keys = key_gen(key)

enc(inp,keys)
