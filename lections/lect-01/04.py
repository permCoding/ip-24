b = '11001'  # dec = 25
dec = 0

i = 0
while i < len(b):
    dec += int(b[i]) * 2**(len(b)-1-i)
    i += 1

print(f"dec = {dec}")

# 1*2**3 + 1*2**2 + 0*2**1 + 1*2**0
# print(b[0], b[1], b[-1], b[-2])