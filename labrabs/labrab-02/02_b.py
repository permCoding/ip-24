def task_2_2():
    def get_sum(line):
        return sum(int(elm) for elm in line.split() if int(elm)%2!=0)
        
    lines = [line for line in open('./input-2.txt')]
    lst_sum = [get_sum(line) for line in lines]
    mx_sum = max(lst_sum)  # key

    for i in range(len(lst_sum)):
        if mx_sum == lst_sum[i]:
            print(i)
            break


task_2_2()
    