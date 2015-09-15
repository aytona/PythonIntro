#!/usr/bin/python3

def main():
    x = (1, 2, 3)
    i = [1, 3, 3]
    n = 'string'
    print(type(x),x)
    print(type(i),i)
    print(type(n),n[2])
    print(type(n),n[2:4])
    # tuple: immutable object that once its created
    # its created and cannot be edited (insert/append/etc..)
    i.insert(2, 7)
    print(type(i),i)
    s = 'string'
    for p in s:
        print(s)
    
if __name__ == "__main__" : main()