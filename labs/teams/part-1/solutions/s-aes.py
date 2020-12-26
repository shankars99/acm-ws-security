
def s_box_transposition(inp_box, order, order_name = "S-Box"):
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

def s_box(inp_box):
    s_box_order = ["1001", "0100", "1010", "1011",
                   "1101", "0001", "1000", "0101",
                   "0110", "0010", "0000", "0011",
                   "1100", "1110", "1111", "0111"]

    s_box_key = s_box_transposition(inp_box, s_box_order)
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



inp = [ ["1100","0101"], ["1000","0000"] ]

inp = s_box(inp)
inp = SR(inp)
MC(inp)
