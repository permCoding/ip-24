with open('./file_02.txt', 'a') as fw:
    s = ''
    s += '1234' + chr(48)
    s += chr(48)
    s += chr(32)
    s += chr(9)
    s += chr(65)
    s += chr(10)
    s += '1234'
    fw.write(s)
