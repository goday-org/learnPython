'''
Created on May 22, 2014

@author: andywaa
'''
def main():
    print '''Choose Write or Read:
            <1>: Write
            <2>: Read'''
    action = raw_input('>')
    
    if action == '1':
        writeHandler()
    elif action == '2':
        readHandler()
    else:
        print 'Please choose correct action.'
        main()

def writeHandler():
    print "Let's write something."
    print 'Input a file name:'
    fileName = raw_input('>')
    print 'Input the Content:'
    content = raw_input('>')
    save('../assets/%s.txt' %(fileName), content)

def readHandler():
    print "Let's read something."
    print 'Input a file name:'
    fileName = raw_input('>')
    read('../assets/%s.txt' %(fileName))

def save(path, content):
    fobj = open(path, 'w')
    fobj.write(content)
    fobj.close()
    main()

def read(path):
    try:
        fobj = open(path, 'r')
        for eachline in fobj:
            print eachline,
        fobj.close()
    except IOError, e:
        print "file open error:", e
    main()       
                             
if __name__ == '__main__':
    main()
    pass