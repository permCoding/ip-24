def bin_to_dec(b):
    dec = 0
    p2 = 1
    for smb in b[::-1]:
        dec += int(smb) * p2
        p2 <<= 1
    return dec


b = '11001'
print(bin_to_dec(b))



# print(b[::-1])
# for smb in b:
#     print(smb)
