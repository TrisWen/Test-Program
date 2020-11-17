# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:27:02 2020

@author: Tristan
"""

def function1(x,n):
    for i in range(n):
        x += 1
    return x

def function2(x,n):
    for i in range(n):
        x -= 1
    return x

def main():
    z = function1(3,10)
    a = function2(3,10)
    print(z)
    print(a)
    mean = (z+a)/2
    print("Mean is:", mean)       
    
if __name__ == "__main__":  
    main()