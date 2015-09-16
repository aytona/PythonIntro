#!/usr/bin/python3

def main():
    choices = dict(
        one = 'first',
        two = 'second',
        three = 'third',
        four = 'fourth',
        five = 'fifth'
    )
    v = 'one'
    print(choices[v])
    print(choices.get(v, 'other'))
    # NOTE: This doesn't work
    
if __name__ == "__main__" : main()