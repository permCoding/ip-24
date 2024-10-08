def task_1():
    mx = -float('inf')
    for line in open('./input-1.txt'):
        num = int(line)
        if (9 < num < 100) and num > mx:
            mx = num
    print(mx)

def task_1_():
    print(max(int(e) for e in open('./input-1.txt') if 10<=int(e)<=99))
    

task_1()
task_1_()