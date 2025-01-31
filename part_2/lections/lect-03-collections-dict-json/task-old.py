import os
import random


def change(word):
    first, last, other = word[0], word[-1], word[1:-1]
    t = list(other)
    random.shuffle(t)
    return first + "".join(t) + last


def create_string(from_files):
    lines = [line for line in from_files.split('\n') if len(line)>0]
    new_lines = []
    for line in lines:
        words = line.split(" ")
        line = " ".join([change(word) for word in words if word != ""])
        new_lines.append(line)
    return new_lines


os.system("cls")

from_files = \
"""
Вы можете соглашаться или не соглашаться с тем, 
что прочитаете в этой книге.
Возможно, вам покажется, что какие-то мысли уже устарели.
Но вы должны обязательно подумать и обосновать, 
почему вы так считаете
"""

lines = create_string(from_files)

for line in lines:
    print(line)

# r w a
