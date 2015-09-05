#!/usr/bin/python3

class Egg:
    # Constructor
    def __init__(self, kind = "Fried"):
        self.kind = kind
        
    def WhatKind(self):
        return self.kind
        
def main():
    # Instances/Objects of the class Egg()
    fried = Egg()
    scrambled = Egg('Scrambled')
    
    print(fried.WhatKind())
    print(scrambled.WhatKind())
    
if __name__ == "__main__": main()