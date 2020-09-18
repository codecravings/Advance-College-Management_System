import sqlite3

def connect():
       con = sqlite3.connect('College_library.db')
       cur = con.cursor()

       cur.execute('CREATE TABLE IF NOT EXISTS library(x INTEGER PRIMARY KEY, Mbtype text, referenceno integer, firstname text, \
                     lastname text, address text, post integer, mobileno integer, ID text, title text, author text, \
                     borrow integer, due integer, loan integer)')


       con.commit()
       con.close()

def insert(Mbtype =' ', referenceno =' ', firstname =' ', lastname =' ', address =' ', post =' ', mobileno =' ', ID =' ', \
           title = ' ', author = ' ', borrow = ' ', due = ' ', loan = ' '):
       con = sqlite3.connect('College_library.db')
       cur = con.cursor()

       cur.execute('INSERT INTO library VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)', (Mbtype, referenceno, firstname, lastname, address, post, \
                                                                                   mobileno, ID, title, author, borrow, due, loan))

       con.commit()
       con.close()

def view():
       con = sqlite3.connect('College_library.db')
       cur = con.cursor()

       cur.execute('SELECT * FROM library')
       row = cur.fetchall()
       return row

       con.close()
def delete(x):
       con = sqlite3.connect('College_library.db')
       cur = con.cursor()

       cur.execute('DELETE FROM library WHERE x = ?',(x,))
       
       con.commit()
       con.close()
       
def update(x, Mbtype =' ', referenceno =' ', firstname =' ', lastname =' ', address =' ', post =' ', mobileno =' ', ID =' ', \
           title = ' ', author = ' ', borrow = ' ', due = ' ', loan = ' '):
       con = sqlite3.connect('College_library.db')
       cur = con.cursor()

       cur.execute('UPDATE library SET Mbtype = ? OR referenceno = ? OR firstname = ? OR lastname = ? OR address = ? OR post = ? OR \
       mobileno = ? OR ID = ? OR title = ? OR author = ? OR borrow = ? OR due = ? OR loan = ?', (Mbtype, referenceno, firstname, lastname, address, \
                                                                                                 post, mobileno, ID, title, author, borrow, due, loan))
       con.commit()
       con.close()

def search(Mbtype =' ', referenceno =' ', firstname =' ', lastname =' ', address =' ', post =' ', mobileno =' ', ID =' ', \
           title = ' ', author = ' ', borrow = ' ', due = ' ', loan = ' '):
       con = sqlite3.connect('College_library.db')
       cur = con.cursor()

       cur.execute('SELECT * FROM library WHERE Mbtype = ? OR referenceno = ? OR firstname = ? OR lastname = ? OR address = ? OR \
       post = ? OR mobileno = ? OR ID = ? OR title = ? OR author = ? OR borrow = ? OR due = ? OR loan = ?',(Mbtype, referenceno, \
                                                                                                            firstname, lastname, \
                                                                                                            address, post, mobileno, \
                                                                                                            ID, title, author, \
                                                                                                            borrow, due, loan))
       row = cur.fetchall()
       return row
       con.close()


connect()
       
       
       
                   
       
