#!/usr/bin/python3

def isPrime(i):
    if i == 1:
        print("1 is special")
        return False
    for x in range (2, i):
        if i % x == 0:
            print ("{} equals {} x {}".format(i, x, i // x))
            return False
    else:
        print(i, "is a prime number")
        return True
        
for i in range(1, 20):
    isPrime(i)