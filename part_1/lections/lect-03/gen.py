e = '012.09-2 7 1'
q = ''.join(str(i) for i in range(0, 10))

s = ''.join(smb for smb in e if smb in q)

print(s)
        