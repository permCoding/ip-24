import string
import random


def generate_random_string(chars, length=12):
    return ''.join(random.choice(chars) for _ in range(length))

chrs = string.ascii_lowercase + string.ascii_uppercase
print(chrs)
print(random.choice(chrs))

lst = []
for _ in range(5):
    lst.append( generate_random_string(chrs) )

print(lst)
