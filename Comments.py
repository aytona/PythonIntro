#!/usr/bin/python3

def main():
    for n in Primes():                    # Generate a list of prime numbers
        if n > 100: break
        print(n)
        
def isPrime(n):
    if n == 1:                            # One is never prime
        return False
    for x in range(2, n):
        if n % x == 0:
            return False                 # Found a divisor, not prime
        else:
            return True
            
def Primes(n = 1):
    while(True):
        if isPrime(n): yield n           # Yield makes this a generator
        n += 1
        
if __name__ == "__main__": main()