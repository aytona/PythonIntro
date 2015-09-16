#!/usr/bin/python3

def main():
    a, b = 0, 1
    if a < b:
        print('this is true')
    else:
        print('it is false')
        
    v = 'one'
    if v == 'one':
        print('v is equal to one')
    elif v == 'two':
        print('v is equal to two')
    else:
        print('v is some other thing')
    
    i = 'this is true' if a < b else 'this is not true'
    print(i)
    
if __name__ == "__main__" : main()