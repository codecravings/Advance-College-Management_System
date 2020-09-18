from tkinter import *  
import random
import College_Marksheet_Backend
import College_Marksheet_Frontend
import tkinter.messagebox
import os

class Window_1():
       def __init__(self, master):
              self.master = master
              self.master.title('Search Page')
              self.master.geometry('1360x750')
              self.master.config(bg = 'skyblue')

              self.roll = StringVar()
              search_frame = LabelFrame(self.master, width = 1000, height = 100, font = ('arial',30,'bold'), relief = 'ridge', bd = 15, bg = 'sky blue', fg = 'white')
              search_frame.grid(row = 1, column = 0, padx = 200, pady = 200)

              lbl_enterrollnumber = Label(search_frame, text = 'Enter Roll Number', font = ('arial',25,'bold'), bg = 'sky blue', fg = 'white')
              lbl_enterrollnumber.grid(row = 0, column = 0, padx = 100, pady = 10)

              txtsearch_entry = Entry(search_frame, font = ('arial',25,'bold'), textvariable = self.roll)
              txtsearch_entry.grid(row = 0, column = 1, padx = 30, pady = 20)

              def Search():
                     if(len(self.roll.get()) != 0):
                           row = College_Marksheet_Backend.search(int(self.roll.get()))
                           print(row)
                           College_Marksheet_Frontend.search_result_marksheet(row)
                     else:
                            tkinter.messagebox.askokcancel('Attention','Please enter valid Roll No.')
                            return

              def new():
                     filename = 'College_Marksheet_Frontend.py'
                     os.system(filename)
                     os.system('notepad'+filename)
                           

              button_search = Button(search_frame, text = 'SEARCH', width = 15, font = ('arial',15,'bold'), command=Search)
              button_search.grid(row = 1, column = 0, padx = 50)
              buttone_new = Button(search_frame, text = 'CREATE NEW', width = 15, font = ('arial',15,'bold'), command=new)
              buttone_new.grid(row = 1, column = 1, padx = 50, pady = 20 )




root = Tk()
root.title("Login Form")
Window_1(root)
root.mainloop()
