import time

sec = 15

while sec:
    # t = f'{sec:02d}'
    t = str(sec).zfill(2)
    print(t, end='\r')
    time.sleep(1)
    sec -= 1

print('00')
