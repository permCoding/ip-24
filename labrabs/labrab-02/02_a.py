def task_2():
    cnt = 0
    for line in open('./input-2.txt'):
        if all(int(elm)%2>0 for elm in line.split(' ')):
            cnt += 1
    print(cnt)
    

task_2()

# all any