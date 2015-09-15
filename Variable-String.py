#!/usr/bin/python3

def main():
    n = 42
    s = 'This is a {} \nstring!'.format(n)
    i = r'This is a {} \nstring!'.format(n)      # Raw string
    y = '''multiple line of strings
this is a string'''
    print(s) 
    print(i)
    print(y)
    
if __name__ == "__main__" : main()