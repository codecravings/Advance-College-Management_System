from tkinter import*
import sqlite3

def connect():
       con = sqlite3.connect('College_Marks.db')
       cur = con.cursor()

       cur.execute('CREATE TABLE IF NOT EXISTS Marks (id INTEGER PRIMARY KEY, name text, roll integer, father_name text, mother_name \
                     text, date_of_birth integer, gender text, school text, email_address text, marks1 integer, marks2 integer, marks3 integer, marks4 integer, \
                     marks5 integer, grand_tot integer, percentage integer, cgpa integer, grade text, division text, result text)')

       con.commit()
       con.close()

def insert(name = ' ', roll = ' ', father_name =' ', mother_name =' ', date_of_birth =' ', gender =' ', school =' ', email_address =' ', marks1 =' ', marks2 =' ', \
           marks3 =' ', marks4 =' ', marks5 =' ', grand_tot =' ', percentage =' ', cgpa =' ', grade =' ', division =' ', result =' '):
       con = sqlite3.connect('College_Marks.db')
       cur = con.cursor()

       cur.execute('INSERT INTO Marks VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (name, roll, father_name, mother_name, date_of_birth, gender, \
                                                                                             school, email_address, marks1, marks2, marks3, marks4, marks5, grand_tot, percentage, \
                                                                                             cgpa, grade, division, result))

       con.commit()
       con.close()

'''def view():
       con = sqlite3.connect('College_Marks.db')
       cur = con.cursor()

       cur.execute('SELECT * FROM Marks')

       con.commit()
       con.close()

def delete(id):
       con = sqlite3.connect('College_Marks.db')
       cur = con.cursor()

       cur.execute('DELETE FROM Marks WHERE id = ?)',(id,))

       con.commit()
       con.close()'''

def update(id, name = ' ', roll = ' ', father_name =' ', mother_name =' ', date_of_birth =' ', gender =' ', school =' ', email_address =' ', marks1 =' ', marks2 =' ', \
           marks3 =' ', marks4 =' ', marks5 =' ', grand_tot =' ', percentage =' ', cgpa =' ', grade =' ', division =' ', result =' '):
       con = sqlite3.connect('College_Marks.db')
       cur = con.cursor()

       cur.execute('UPDATE Marks SET name = ? OR roll = ? OR father_name =  ? OR mother_name = ? OR date_of_birth = ? OR gender = ? OR \
                     school = ? OR email_address = ? OR marks1 = ? OR marks2 = ? OR  marks3 = ? OR marks4 = ? OR marks5 = ? OR grand_tot = ? OR percentage = ? OR \
                     cgpa = ? OR grade = ? OR division = ? OR result = ?', (name, roll, father_name, mother_name, date_of_birth, gender, school, email_address, marks1, marks2, marks3, \
                                                                       marks4, marks5, grand_tot, percentage, cgpa, grade))

       con.commit()
       con.close()

def search(roll):
       con = sqlite3.connect('College_Marks.db')
       cur = con.cursor()

       cur.execute('SELECT * FROM Marks WHERE roll = ?',(roll,))
       row = cur.fetchall()
       return row     

connect()

