# -*- coding: utf-8 -*-  
'''
Created on May 14, 2014

@author: andywaa
'''
import os

def main():
    print 'start main'
    ls = os.linesep
    text = 'this is for test'
    fobj = open('../assets/test.txt', 'w')
    fobj.write(text)
    textArr = ['line1', 'line2', 'line3']
    fobj.writelines(['%s%s' %(ls, x) for x in textArr])
    fobj.close()

if __name__ == '__main__':
    main()
    pass