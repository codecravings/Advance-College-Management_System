from tkinter import*
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox
import College_Library_Backend

class Library:
       
       def __init__(self, root):
              self.root = root
              self.root.title('Library Management System')
              self.root.geometry('1350x750')
              self.root.config(bg = 'sky blue')


              self.Mbtype = StringVar()
              self.referenceno = StringVar()
              self.firstname = StringVar()
              self.lastname = StringVar()
              self.address = StringVar()
              self.post = StringVar()
              self.mobileno = StringVar()
              self.ID = StringVar()
              self.title = StringVar()
              self.author = StringVar()
              self.borrow = StringVar()
              self.due = StringVar()
              self.loan = StringVar()
              self.yr_of_pub = StringVar()
              self.editions = StringVar()
              



              def BookRec(event):
                     try:
                            global selected_tuple
                            index = self.List_bx_2.curselection()[0]
                            selected_tuple = self.List_bx_2.get(index)

                            self.txt_Entry_0.delete(0, END)
                            self.txt_Entry_0.insert(END, selected_tuple[1])
                            self.txt_Entry_1.delete(0, END)
                            self.txt_Entry_1.insert(END, selected_tuple[2])
                            self.txt_Entry_2.delete(0, END)
                            self.txt_Entry_2.insert(END, selected_tuple[3])
                            self.txt_Entry_3.delete(0, END)
                            self.txt_Entry_3.insert(END, selected_tuple[4])
                            self.txt_Entry_4.delete(0, END)
                            self.txt_Entry_4.insert(END, selected_tuple[5])
                            self.txt_Entry_5.delete(0, END)
                            self.txt_Entry_5.insert(END, selected_tuple[6])
                            self.txt_Entry_6.delete(0, END)
                            self.txt_Entry_6.insert(END, selected_tuple[7])
                            self.txt_Entry_7.delete(0, END)
                            self.txt_Entry_7.insert(END, selected_tuple[8])
                            self.txt_Entry_8.delete(0, END)
                            self.txt_Entry_8.insert(END, selected_tuple[9])
                            self.txt_Entry_9.delete(0, END)
                            self.txt_Entry_9.insert(END, selected_tuple[10])
                            self.txt_Entry_10.delete(0, END)
                            self.txt_Entry_10.insert(END, selected_tuple[11])
                            self.txt_Entry_11.delete(0, END)
                            self.txt_Entry_11.insert(END, selected_tuple[12])
                            self.txt_Entry_12.delete(0, END)
                            self.txt_Entry_12.insert(END, selected_tuple[13])
                             

                     except IndexError:
                            pass
              def Insert():
                     if(len(self.referenceno.get()) != 0):
                            College_Library_Backend.insert(self.Mbtype.get(), self.referenceno.get(), self.firstname.get(), self.lastname.get() \
                                                           , self.address.get(), self.post.get(), self.mobileno.get(), self.ID.get() \
                                                           , self.title.get(), self.author.get(), self.borrow.get(), self.due.get() \
                                                           , self.loan.get())
                            self.List_bx_2.delete(0, END)
                            self.List_bx_2.insert(END, (self.Mbtype.get(), self.referenceno.get(), self.firstname.get(), self.lastname.get()\
                                                         , self.address.get(), self.post.get(), self.mobileno.get(), self.ID.get()\
                                                         , self.title.get(), self.author.get(), self.borrow.get(), self.due.get()\
                                                         , self.loan.get()))
                            

              def Display():
                     self.List_bx_2.delete(0, END)
                     for row in College_Library_Backend.view():
                            self.List_bx_2.insert(END, row, str(' '))
                                                       
              def Exit():
                     Exit = tkinter.messagebox.askyesno('Library Management System','Confirm if you want to Exit')
                     if Exit > 0:
                            root.destroy()
                            return
                                                                    
              def Reset():
                     self.Mbtype.set('')
                     self.referenceno.set('')
                     self.firstname.set('')
                     self.lastname.set('')
                     self.address.set('')
                     self.post.set('')
                     self.mobileno.set('')
                     self.ID.set('')
                     self.title.set('')
                     self.author.set('')
                     self.borrow.set('')
                     self.due.set('')
                     self.loan.set('')
                     self.Display_Layout.delete('1.0', END)
                     self.List_bx_2.delete(0, END)

              def Delete():
                     College_Library_Backend.delete(selected_tuple[0])
                     Reset()
                     Display()

              def Update():
                     College_Library_Backend.delete(selected_tuple[0])
                     College_Library_Backend.insert(self.Mbtype.get(), self.referenceno.get(), self.firstname.get(), self.lastname.get() \
                                                    , self.address.get(), self.post.get(), self.mobileno.get(), self.ID.get() \
                                                    , self.title.get(), self.author.get(), self.borrow.get(), self.due.get() \
                                                    , self.loan.get())
                     self.List_bx_2.delete(0, END)
                     self.List_bx_2.insert(END, (self.Mbtype.get(), self.referenceno.get(), self.firstname.get(), self.lastname.get()\
                                                  , self.address.get(), self.post.get(), self.mobileno.get(), self.ID.get()\
                                                  , self.title.get(), self.author.get(), self.borrow.get(), self.due.get()\
                                                  , self.loan.get()))

              def Search():
                     self.List_bx_2.delete(0, END)
                     for row in College_Library_Backend.search(self.Mbtype.get(), self.referenceno.get(), self.firstname.get(), self.lastname.get()\
                                                  , self.address.get(), self.post.get(), self.mobileno.get(), self.ID.get()\
                                                  , self.title.get(), self.author.get(), self.borrow.get(), self.due.get()\
                                                  , self.loan.get()):
                            self.List_bx_2.insert(END, row, str(' '))

              def Details():
                     self.Display_Layout.delete('1.0', END)
                     self.Display_Layout.insert(END, 'Book ID: ' + self.ID.get() + '\n')
                     self.Display_Layout.insert(END, 'Title: ' + self.title.get() + '\n')
                     self.Display_Layout.insert(END, 'Author:  ' + self.author.get() + '\n')
                     self.Display_Layout.insert(END, 'Edition: ' + self.editions.get() + '\n')
                     self.Display_Layout.insert(END, 'Year of Published: \t' + self.yr_of_pub.get() + '\n')
                     self.Display_Layout.insert(END, 'Date Borrowed: ' + self.borrow.get() + '\n')
                     self.Display_Layout.insert(END, 'Date Due:' + self.due.get() + '\n')
                     self.Display_Layout.insert(END, 'Days in Loan: ' + self.loan.get() + '\n')
                             

              Library_Main_Frame = Frame(self.root, bg = 'sky blue')
              Library_Main_Frame.grid()

              Library_Title_Frame_1 = Frame(Library_Main_Frame, width = 1350, bg = 'sky blue', relief = RIDGE, bd = 15, padx = 20)
              Library_Title_Frame_1.pack(side = TOP)

              self.Library_lblTitle = Label(Library_Title_Frame_1, font = ('arial', 40, 'bold'), text ='\tLibrary Management System\t', \
                                            bg = 'sky blue', padx = 13, foreground="white")
              self.Library_lblTitle.grid()

              btn_Frame = Frame(Library_Main_Frame, width = 1350, height = 50, relief = RIDGE, bd = 10, bg = 'sky blue')
              btn_Frame.pack(side = BOTTOM)

              Library_Detail_Frame = Frame(Library_Main_Frame, width = 1350, height = 100, relief = RIDGE, bd = 10, bg = 'sky blue')
              Library_Detail_Frame.pack(side = BOTTOM)

              Library_Data_Frame = Frame(Library_Main_Frame, width = 1350, height = 400, relief = RIDGE, bd = 15, bg = 'sky blue')
              Library_Data_Frame.pack(side = BOTTOM)

              Library_Frame_1 = LabelFrame(Library_Data_Frame, width = 800, height = 400, relief = RIDGE, bd = 10, bg = 'sky blue', \
                              text = "Library Membership Info:", foreground="white", padx = 20, font = ('arial',15,'bold'))
              Library_Frame_1.pack(side = LEFT, padx = 3)

              Library_Frame_2 = LabelFrame(Library_Data_Frame, width = 550, height = 400, relief = RIDGE, bd = 10, bg = 'sky blue', \
                              text = "Book Details:", foreground="white", padx = 20, font = ('arial',15,'bold'))
              Library_Frame_2.pack(side = RIGHT)



              self.memLabel_1 = Label(Library_Frame_1, text ='Member type', font = ('arial', 13, 'bold'), pady = 2, \
                                      bg = 'sky blue', foreground="white")
              self.memLabel_1.grid(row = 0, column = 0, sticky = W)
              self.refLabel_2 = Label(Library_Frame_1, text ='Reference No.', font = ('arial', 13, 'bold'), pady = 2, \
                                      bg = 'sky blue', foreground="white")
              self.refLabel_2.grid(row = 1, column = 0, sticky = W)
              self.firstnameLabel_3 = Label(Library_Frame_1, text ='First Name', font = ('arial', 13, 'bold'), pady = 2, \
                                            bg = 'sky blue', foreground="white")
              self.firstnameLabel_3.grid(row = 2, column = 0, sticky = W)
              self.lastnameLabel_4 = Label(Library_Frame_1, text ='Last Name', font = ('arial', 13, 'bold'), pady = 2, \
                                           bg = 'sky blue', foreground="white")
              self.lastnameLabel_4.grid(row = 3, column = 0, sticky = W)
              self.addressLabel_5 = Label(Library_Frame_1, text ='Address', font = ('arial', 13, 'bold'), pady = 2, \
                                          bg = 'sky blue', foreground="white")
              self.addressLabel_5.grid(row = 4, column = 0, sticky = W)
              self.postcodeLabel_6 = Label(Library_Frame_1, text ='Post Code', font = ('arial', 13, 'bold'), pady = 2, \
                                           bg = 'sky blue', foreground="white")
              self.postcodeLabel_6.grid(row = 5, column = 0, sticky = W)
              self.mobilenoLabel_7 = Label(Library_Frame_1, text ='Mobile No.', font = ('arial', 13, 'bold'), pady = 2, \
                                           bg = 'sky blue', foreground="white")
              self.mobilenoLabel_7.grid(row = 6, column = 0, sticky = W)
              self.bookidLabel_8 = Label(Library_Frame_1, text ='Book ID', font = ('arial', 13, 'bold'), pady = 2, \
                                         bg = 'sky blue', foreground="white")
              self.bookidLabel_8.grid(row = 0, column = 2, sticky = W)
              self.booktitleLabel_9 = Label(Library_Frame_1, text ='Book Title', font = ('arial', 13, 'bold'), pady = 2, \
                                            bg = 'sky blue', foreground="white")
              self.booktitleLabel_9.grid(row = 1, column = 2, sticky = W)
              self.authorLabel_10 = Label(Library_Frame_1, text ='Author', font = ('arial', 13, 'bold'), pady = 2, \
                                          bg = 'sky blue', foreground="white")
              self.authorLabel_10.grid(row = 2, column = 2, sticky = W)
              self.dateborrowedLabel_11 = Label(Library_Frame_1, text ='Date Borrowed', font = ('arial', 13, 'bold'), pady = 2, \
                                                bg = 'sky blue', foreground="white")
              self.dateborrowedLabel_11.grid(row = 3, column = 2, sticky = W)
              self.dateLabel_13 = Label(Library_Frame_1, text ='Date Due', font = ('arial', 13, 'bold'), pady = 2, \
                                        bg = 'sky blue', foreground="white")
              self.dateLabel_13.grid(row = 4, column = 2, sticky = W)
              self.dateLabel_13 = Label(Library_Frame_1, text ='Days in Loan', font = ('arial', 13, 'bold'), pady = 2, \
                                        bg = 'sky blue', foreground="white")
              self.dateLabel_13.grid(row = 5, column = 2, sticky = W)
              


              self.txt_Entry_0 = ttk.Combobox(Library_Frame_1, values = (' ', 'Student', 'Faculty', 'Staff Member'), \
                                              font = ('arial',13,'bold'), width = 23, textvariable = self.Mbtype)
              self.txt_Entry_0.grid(row = 0, column = 1)
              self.txt_Entry_1 = Entry(Library_Frame_1, font = ('arial', 13, 'bold'), width = 25, textvariable = self.referenceno)
              self.txt_Entry_1.grid(row = 1, column = 1, padx = 15)
              self.txt_Entry_2 = Entry(Library_Frame_1, font = ('arial', 13, 'bold'), width = 25, textvariable = self.firstname)
              self.txt_Entry_2.grid(row = 2, column = 1, padx = 15)
              self.txt_Entry_3 = Entry(Library_Frame_1, font = ('arial', 13, 'bold'), width = 25, textvariable = self.lastname)
              self.txt_Entry_3.grid(row = 3, column = 1, padx = 15)
              self.txt_Entry_4 = Entry(Library_Frame_1, font = ('arial', 13, 'bold'), width = 25, textvariable = self.address)
              self.txt_Entry_4.grid(row = 4, column = 1, padx = 15)
              self.txt_Entry_5 = Entry(Library_Frame_1, font = ('arial', 13, 'bold'), width = 25, textvariable = self.post)
              self.txt_Entry_5.grid(row = 5, column = 1, padx = 15)
              self.txt_Entry_6 = Entry(Library_Frame_1, font = ('arial', 13, 'bold'), width = 25, textvariable = self.mobileno)
              self.txt_Entry_6.grid(row = 6, column = 1, padx = 15)
              self.txt_Entry_7 = Entry(Library_Frame_1, font = ('arial', 13, 'bold'), width = 25, textvariable = self.ID)
              self.txt_Entry_7.grid(row = 0, column = 4, padx = 15)
              self.txt_Entry_8 = Entry(Library_Frame_1, font = ('arial', 13, 'bold'), width = 25, textvariable = self.title)
              self.txt_Entry_8.grid(row = 1, column = 4, padx = 15)
              self.txt_Entry_9 = Entry(Library_Frame_1, font = ('arial', 13, 'bold'), width = 25, textvariable = self.author)
              self.txt_Entry_9.grid(row = 2, column = 4, padx = 15)
              self.txt_Entry_10 = Entry(Library_Frame_1, font = ('arial', 13, 'bold'), width = 25, textvariable = self.borrow)
              self.txt_Entry_10.grid(row = 3, column = 4, padx = 15)
              self.txt_Entry_11 = Entry(Library_Frame_1, font = ('arial', 13, 'bold'), width = 25, textvariable = self.due)
              self.txt_Entry_11.grid(row = 4, column = 4, padx = 15)
              self.txt_Entry_12 = Entry(Library_Frame_1, font = ('arial', 13, 'bold'), width = 25, textvariable = self.loan)
              self.txt_Entry_12.grid(row = 5, column = 4, padx = 15)



              self.Display_Layout = Text(Library_Frame_2, font = ('arial', 13, 'bold'), width = 28, height = 11)
              self.Display_Layout.grid(row = 0, column = 2)


              List_of_Books = [' C',' C++',' Java',' Python',' PHP',' Java Script',' My SQL',' Data Structure',' Linux',\
                               ' Operating System',' Web Developement',' Data Science',' Algorithms',' Android', \
                               ' VB.net']


              def SelectedBook(event):
                     value_List = str(self.List_bx_1.get(self.List_bx_1.curselection()))
                     val = value_List

                     if (val == ' C'):
                            self.ID.set('ISBN 525341')
                            self.title.set('Programming using C')
                            self.author.set('Denish ritche')
                            self.yr_of_pub.set('2019')
                            self.editions.set('5th')

                            import datetime

                            days1 = datetime.date.today()
                            days2 = datetime.timedelta(days = 14)
                            days3 = (days1 + days2)
                            self.borrow.set(days1)
                            self.loan.set('14')
                            self.due.set(days3)
                            Details()
                     elif (val == ' C++'):
                            self.ID.set('ISBN 345687')
                            self.title.set('Programming using C++')
                            self.author.set('Denis Ritche 2.0')
                            self.yr_of_pub.set('2019')
                            self.editions.set('4th')

                            import datetime

                            days1 = datetime.date.today()
                            days2 = datetime.timedelta(days = 10)
                            days3 = (days1 + days2)
                            self.borrow.set(days1)
                            self.loan.set('10')
                            self.due.set(days3)
                            Details()
                     elif (val == ' Java'):
                            self.ID.set('ISBN 643842')
                            self.title.set('Java Programming')
                            self.author.set('James Gosling')
                            self.yr_of_pub.set('2019')
                            self.editions.set('7th')

                            import datetime

                            days1 = datetime.date.today()
                            days2 = datetime.timedelta(days = 13)
                            days3 = (days1 + days2)
                            self.borrow.set(days1)
                            self.loan.set('13')
                            self.due.set(days3)
                            Details()
                     elif (val == ' Python'):
                            self.ID.set('ISBN 564524')
                            self.title.set('Python Programming')
                            self.author.set('Guido van Rossum')
                            self.yr_of_pub.set('2019')
                            self.editions.set('3rd')

                            import datetime

                            days1 = datetime.date.today()
                            days2 = datetime.timedelta(days = 13)
                            days3 = (days1 + days2)
                            self.borrow.set(days1)
                            self.loan.set('13')
                            self.due.set(days3)
                            Details()
                     elif (val == ' PHP'):
                            self.ID.set('ISBN 735893')
                            self.title.set('PHP Programming')
                            self.author.set('Rasmus Lerdorf')
                            self.yr_of_pub.set('2019')
                            self.editions.set('5th')

                            import datetime

                            days1 = datetime.date.today()
                            days2 = datetime.timedelta(days = 15)
                            days3 = (days1 + days2)
                            self.borrow.set(days1)
                            self.loan.set('15')
                            self.due.set(days3)
                            Details()
                     elif (val == ' Java Script'):
                            self.ID.set('ISBN 643842')
                            self.title.set('Java Script Programming')
                            self.author.set('Brendan Eich')
                            self.yr_of_pub.set('2019')
                            self.editions.set('4th')

                            import datetime

                            days1 = datetime.date.today()
                            days2 = datetime.timedelta(days = 13)
                            days3 = (days1 + days2)
                            self.borrow.set(days1)
                            self.loan.set('13')
                            self.due.set(days3)
                            Details()
                     elif (val == ' My SQL'):
                            self.ID.set('ISBN 649635')
                            self.title.set('My SQL Programming')
                            self.author.set('Allan Larsson ')
                            self.yr_of_pub.set('2019')
                            self.editions.set('3rd')

                            import datetime

                            days1 = datetime.date.today()
                            days2 = datetime.timedelta(days = 20)
                            days3 = (days1 + days2)
                            self.borrow.set(days1)
                            self.loan.set('20')
                            self.due.set(days3)
                            Details()
                     elif (val == ' Data Structure'):
                            self.ID.set('ISBN 531588')
                            self.title.set('Data Structure')
                            self.author.set('Data boi')
                            self.yr_of_pub.set('2019')
                            self.editions.set('5th')

                            import datetime

                            days1 = datetime.date.today()
                            days2 = datetime.timedelta(days = 11)
                            days3 = (days1 + days2)
                            self.borrow.set(days1)
                            self.loan.set('11')
                            self.due.set(days3)
                            Details()
                     elif (val == ' Linux'):
                            self.ID.set('ISBN 356853')
                            self.title.set('Linux Administration')
                            self.author.set('Code Cravings')
                            self.yr_of_pub.set('2019')
                            self.editions.set('1st')

                            import datetime

                            days1 = datetime.date.today()
                            days2 = datetime.timedelta(days = 6)
                            days3 = (days1 + days2)
                            self.borrow.set(days1)
                            self.loan.set('6')
                            self.due.set(days3)
                            Details()
                     elif (val == ' Operating System'):
                            self.ID.set('ISBN 536453')
                            self.title.set('OS Concepts ')
                            self.author.set('Bill Gates')
                            self.yr_of_pub.set('2019')
                            self.editions.set('4th')

                            import datetime

                            days1 = datetime.date.today()
                            days2 = datetime.timedelta(days = 12)
                            days3 = (days1 + days2)
                            self.borrow.set(days1)
                            self.loan.set('12')
                            self.due.set(days3)
                            Details()
                     elif (val == ' Web Developement'):
                            self.ID.set('ISBN 543548')
                            self.title.set('Web Developement ')
                            self.author.set('An web developer')
                            self.yr_of_pub.set('2019')
                            self.editions.set('3rd')

                            import datetime

                            days1 = datetime.date.today()
                            days2 = datetime.timedelta(days = 15)
                            days3 = (days1 + days2)
                            self.borrow.set(days1)
                            self.loan.set('15')
                            self.due.set(days3)
                            Details()
                     elif (val == ' Data Science'):
                            self.ID.set('ISBN 835764')
                            self.title.set('Data Science Concept ')
                            self.author.set('Ryan Manaay')
                            self.yr_of_pub.set('2019')
                            self.editions.set('3rd')

                            import datetime

                            days1 = datetime.date.today()
                            days2 = datetime.timedelta(days = 15)
                            days3 = (days1 + days2)
                            self.borrow.set(days1)
                            self.loan.set('15')
                            self.due.set(days3)
                            Details()
                     elif (val == ' Algorithms'):
                            self.ID.set('ISBN 535674')
                            self.title.set('Basics of Algorithm ')
                            self.author.set('Paul Angelo Niar')
                            self.yr_of_pub.set('2019')
                            self.editions.set('7th')

                            import datetime

                            days1 = datetime.date.today()
                            days2 = datetime.timedelta(days = 10)
                            days3 = (days1 + days2)
                            self.borrow.set(days1)
                            self.loan.set('10')
                            self.due.set(days3)
                            Details()
                     elif (val == ' Android'):
                            self.ID.set('ISBN 356452')
                            self.title.set('Android Programming')
                            self.author.set('Sundar Pichal')
                            self.yr_of_pub.set('2019')
                            self.editions.set('4th')

                            import datetime

                            days1 = datetime.date.today()
                            days2 = datetime.timedelta(days = 9)
                            days3 = (days1 + days2)
                            self.borrow.set(days1)
                            self.loan.set('9')
                            self.due.set(days3)
                            Details()
                            
              sroll_b_1 = Scrollbar(Library_Frame_2)
              sroll_b_1.grid(row =0, column = 1, sticky = 'ns')

              self.List_bx_1 = Listbox(Library_Frame_2, font = ('arial', 13, 'bold'), width = 20, height = 10)
              self.List_bx_1.bind('<<ListboxSelect>>', SelectedBook)
              self.List_bx_1.grid(row = 0, column = 0)
              sroll_b_1.config(command = self.List_bx_1.yview)

              
              scroll_b_2 = Scrollbar(Library_Detail_Frame)
              scroll_b_2.grid(row = 1, column = 1, sticky = 'ns')

              self.List_bx_2 = Listbox(Library_Detail_Frame, font = ('arial', 13, 'bold'), width = 144, height = 11)
              self.List_bx_2.bind('<<ListboxSelect>>', BookRec)
              self.List_bx_2.grid(row = 1, column = 0)
              scroll_b_2.config(command = self.List_bx_2.yview)

              for items in List_of_Books:
                     self.List_bx_1.insert(END, items)



              btnsave_1 = Button(btn_Frame, text = 'SAVE', font = ('arial',15,'bold'), width = 10, command = Insert)
              btnsave_1.grid(row = 0, column = 0, padx = 8, pady = 5)
              btndisplay_2 = Button(btn_Frame, text = 'DISPLAY', font = ('arial',15,'bold'), width = 10, command = Display)
              btndisplay_2.grid(row = 0, column = 1, padx = 8)
              btnreset_3 = Button(btn_Frame, text = 'RESET', font = ('arial',15,'bold'), width = 10, command = Reset)
              btnreset_3.grid(row = 0, column = 2, padx = 8)
              btnupdate_4 = Button(btn_Frame, text = 'UPDATE', font = ('arial',15,'bold'), width = 10, command = Update)
              btnupdate_4.grid(row = 0, column = 3, padx = 8)
              btnsearch_5 = Button(btn_Frame, text = 'SEARCH', font = ('arial',15,'bold'), width = 10, command = Search)
              btnsearch_5.grid(row = 0, column = 4, padx = 8)
              btndelete_6 = Button(btn_Frame, text = 'DELETE', font = ('arial',15,'bold'), width = 10, command = Delete)
              btndelete_6.grid(row = 0, column = 5, padx = 8)
              btnexit_7 = Button(btn_Frame, text = 'EXIT', font = ('arial',15,'bold'), width = 10, command = Exit)
              btnexit_7.grid(row = 0, column = 6, padx = 8)

              

if __name__ == '__main__':
       root = Tk()
       applicaton = Library(root)
       root.mainloop()
