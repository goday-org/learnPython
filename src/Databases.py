'''
Created on May 6, 2014

@author: andywaa
'''

import sqlite3
db = sqlite3.connect('../assets/data.db');
def main():
    db.execute('drop table if exists test')
    db.execute('create table test (t1 text, i1 int)')
    db.execute('insert into test (t1, i1) values (?,?)', ('one', 1))
    db.execute('insert into test (t1, i1) values (?,?)', ('two', 2))
    db.execute('insert into test (t1, i1) values (?,?)', ('three', 3))
    db.execute('insert into test (t1, i1) values (?,?)', ('four', 4))
    db.commit();
    
def readDB():
    cursor = db.execute('select * from test order by i1')    
    for i in cursor:
        print i
        
if __name__ == '__main__':
    main()
    readDB()
    pass