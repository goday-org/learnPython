'''
Created on May 4, 2014

@author: andywaa
'''
def readFile(path):
    try:
        fobj = open(path, 'r')
        for eachline in fobj:
            print eachline,
        fobj.close()
    except IOError, e:
        print "file open error:", e
if __name__ == '__main__':
    readFile('../assets/note.txt')
    pass