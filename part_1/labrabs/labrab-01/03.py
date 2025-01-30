def isPrime(n):
    for div in range(2, n):  # 2 3 4 n-1
        if n % div == 0:
            return False
    return True
         

for n in range(2, 50):
    print(n, isPrime(n))
