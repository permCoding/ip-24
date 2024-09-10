def bin_to_dec(b):
    dec = 0
    i = 0
    while i < len(b):
        dec += int(b[i]) * 2**(len(b)-1-i)
        i += 1
    return dec


b = input('Введите двоичное число - ')
print(f"dec = {bin_to_dec(b)}")
