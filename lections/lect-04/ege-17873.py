# https://kompege.ru/task

nums = [int(x) for x in open('./docs/17_17873.txt')]
mn = min(nums)

cnt = 0
for i in range(len(nums)-1):
    if nums[i]%16==mn or nums[i+1]%16==mn:
        cnt += 1
print(cnt)

"""
 Определите количество пар последовательности, 
 в которых остаток от деления на 16  
 хотя бы одного из элементов 
 равен минимальному элементу последовательности. 
"""