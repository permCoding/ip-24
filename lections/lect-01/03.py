b = '11001'  # dec = 25

dec = 0

p = len(b) - 1
q = 0
while p >= 0:
    dec += int(b[q]) * 2**p
    p -= 1
    q += 1

print(f"dec = {dec}")

# 1*2**3 + 1*2**2 + 0*2**1 + 1*2**0
# print(b[0], b[1], b[-1], b[-2])