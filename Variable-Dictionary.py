#!/usr/bin/python3

def main():
    d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    for k in sorted(d.keys()):      # Alphabetical order by keys
        print(k, d[k])
        
    i = dict(
        one = 1, two = 2, three = 3, four = 4, five = 5
    )
    for k in sorted(i.keys()):
        print(k, i[k])
    
if __name__ == "__main__" : main()