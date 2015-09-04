#!/usr/bin/python3

def isPrime(i):
    if i == 1:
        return False
    for x in range(2, i):
        if i % x == 0:
            return False
    else:
        return True
        
def Primes(i = 1):
    while(True):
        if isPrime(i): yield i
        i += 1
        
for i in Primes():
    if i > 100: break
    print(i)