import sqlite3

def connect():
       con = sqlite3.connect('College_fee.db')
       cur = con.cursor()

       cur.execute('CREATE TABLE IF NOT EXISTS fee(id INTEGER PRIMARY KEY, receipts integer, name text, admin text, date integer, \
                    branch text, semister text, total integer, paid integer, due integer)')

       con.commit()
       con.close()

def insert(receipts =' ', name =' ', admin =' ', date =' ', branch =' ', semister =' ', total =' ', paid =' ', due =' '):
       con = sqlite3.connect('College_fee.db')
       cur = con.cursor()

       cur.execute('INSERT INTO fee VALUES (NULL,?,?,?,?,?,?,?,?,?)', (receipts, name, admin, date, branch, semister, total, paid, due))

       con.commit()
       con.close()

def view():
       con = sqlite3.connect('College_fee.db')
       cur = con.cursor()

       cur.execute('SELECT * FROM fee')
       row = cur.fetchall()
       return row

       con.commit()
       

def delete(id):
       con = sqlite3.connect('College_fee.db')
       cur = con.cursor()

       cur.execute('DELETE FROM fee WHERE id = ?',(id,))

       con.commit()
       con.close()

def update(id, receipts =' ', name =' ', admin =' ', date =' ', branch =' ', semister =' ', total =' ', paid =' ', due =' '):
       con = sqlite3.connect('College_fee.db')
       cur = con.cursor()

       cur.execute('UPDATE fee SET receipts = ? OR name = ? OR admin = ? OR date = ? OR branch = ? OR semister = ? OR total = ? OR \
                    paid = ? OR due = ?', (receipts, name, admin, date, branch, semister, total, paid, due))


       con.commit()
       con.close()

def search(receipts =' ', name =' ', admin =' ', date =' ', branch =' ', semister =' ', total =' ', paid =' ', due =' '):
       con = sqlite3.connect('College_fee.db')
       cur = con.cursor()

       cur.execute('SELECT * FROM fee WHERE  receipts = ? OR name = ? OR admin = ? OR date = ? OR branch = ? OR semister = ? OR \
                    total = ? OR paid = ? OR due = ?', (receipts, name, admin, date, branch, semister, total, paid, due))
       row = cur.fetchall()
       return row

       con.commit()
       
connect()


