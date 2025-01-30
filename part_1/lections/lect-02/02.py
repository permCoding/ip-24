def bin_to_dec(b):  # '1100'
    dec = 0
    i = 0
    while i < len(b):
        dec += int(b[i]) * 2**(len(b)-1-i)
        i += 1
    return dec



for shift in range(0, 8):  # 0 .. 7
    print(2**shift)
# x = 1  # 00000001
# y = x << 2  # 00000100
# print(y)  # 4
