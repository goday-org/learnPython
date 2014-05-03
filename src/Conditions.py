# -*- coding: utf-8 -*-  
'''
Created on May 3, 2014

@author: andy
'''
#if elif else

def foo(n):
    if n>100:
        print "Number > 100"
    elif n>10:
        print "Number > 10"
    else: 
        print "Number < 10"        

if __name__ == '__main__':
    foo(90)
    pass