import sqlite3

def connect():
       conn = sqlite3.connect("College_student.db")
       cur = conn.cursor()

       cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, name text, father_name text, mother_name text, \
                     address text, mobileno integer,email_address text, date_of_birth integer, gender text)")

       conn.commit()
       conn.close()

def insert(name = " ", father_name =" ", mother_name =" ", address =" ", mobileno =" ", email_address =" ", date_of_birth =" ", gender =" "):
       conn = sqlite3.connect("College_student.db")
       cur = conn.cursor()

       cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?)", (name, father_name, mother_name, address , mobileno, email_address, date_of_birth, gender))

       conn.commit()
       conn.close()
                                                                        

def view():
       conn = sqlite3.connect("College_student.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM student")
       rows = cur.fetchall()
       return rows

       conn.close()

def delete(id):
       conn = sqlite3.connect("College_student.db")
       cur = conn.cursor()

       cur.execute("DELETE FROM student WHERE id = ?", (id,))

       conn.commit()
       conn.close()

def update(id, name = " ", father_name =" ", mother_name =" ", address =" ", mobileno =" ", email_address =" ", date_of_birth =" ", gender =" "):
       conn = sqlite3.connect("College_student.db")
       cur = conn.cursor()

       cur.execute("UPDATE student SET name = ? OR father_name = ? OR mother_name = ? OR address = ? OR mobileno = ? OR email_address = ? OR date_of_birth = ? OR gender = ?", \
                   (name, father_name, mother_name, address , mobileno, email_address, date_of_birth, gender))

       conn.commit()
       conn.close()

def search(name = " ", father_name =" ", mother_name =" ", address =" ", mobileno =" ", email_address =" ", date_of_birth =" ", gender =" "):
       conn = sqlite3.connect("College_student.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM student WHERE name = ? OR father_name = ? OR mother_name = ? OR address = ? OR mobileno = ? OR email_address = ? OR date_of_birth = ? \
                     OR gender = ?", (name, father_name, mother_name, address , mobileno, email_address, date_of_birth, gender))
       rows = cur.fetchall()
       return rows
       
       conn.close()

                                                               
connect()
       
