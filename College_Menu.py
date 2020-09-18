from tkinter import*
import random
import os

def __marksheet__():
       filename = 'College_Search_Page.py'
       os.system(filename)
       os.system('notepad'+filename)

def __Library__():
       filename = 'College_Library_Frontend.py'
       os.system(filename)
       os.system('notepad'+filename)

def __information__():
       filename = 'College_Std_info_FrontEnd.py'
       os.system(filename)
       os.system('notepad'+filename)

def __FeeReport__():
       filename = 'College_Fee_Frontend.py'
       os.system(filename)
       os.system('notepad'+filename)
       
       
def menu():
       root = Tk()
       root.title('Menu')
       root.geometry('1350x750')
       root.config(bg = 'sky blue')
       
       Menu_title_Frame = LabelFrame(root, font = ('arial',50,'bold'), width = 1000, height = 100, bg = 'sky blue', relief = 'raise', bd = 13)
       Menu_title_Frame.grid(row = 0, column = 0, pady = 50)
       
       Menu_title_Label = Label(Menu_title_Frame, text = 'MENU', font = ('arial',30,'bold'), bg = 'sky blue', foreground="white")
       Menu_title_Label.grid(row = 0, column = 0, padx = 150)


       #========================================================FRAMES===================================================================
       Menu_Frame_1 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'sky blue', relief = 'ridge', bd = 10)
       Menu_Frame_1.grid(row = 1, column = 0, padx = 280)
       Menu_Frame_2 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'sky blue', relief = 'ridge', bd = 10)
       Menu_Frame_2.grid(row = 2, column = 0, padx = 130, pady = 7)
       Menu_Frame_3 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'sky blue', relief = 'ridge', bd = 10)
       Menu_Frame_3.grid(row = 3, column = 0, pady = 7)
       Menu_Frame_4 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'sky blue', relief = 'ridge', bd = 10)
       Menu_Frame_4.grid(row = 4, column = 0, pady = 7)
       


       #========================================================LABELS===================================================================
       Label_1_STUDENTINFO = Label(Menu_Frame_1, text = 'STUDENT PROFILE', font = ('arial',25,'bold'), bg = 'sky blue', foreground="white")
       Label_1_STUDENTINFO.grid(row = 0, column = 0, padx = 50, pady = 5)
       Label_2_FEEREPORT = Label(Menu_Frame_2, text = 'FEE REPORT', font = ('arial',25,'bold'), bg = 'sky blue', foreground="white")
       Label_2_FEEREPORT.grid(row = 0, column = 0, padx = 100, pady = 5)
       Label_3_LIBRARYSYSTEM = Label(Menu_Frame_3, text = 'LIBRARY SYSTEM', font = ('arial',25,'bold'), bg = 'sky blue', foreground="white")
       Label_3_LIBRARYSYSTEM.grid(row = 0, column = 0, padx = 60, pady = 5)
       Label_4_MARKSHEET = Label(Menu_Frame_4, text = 'MARKSHEET', font = ('arial',25,'bold'), bg = 'sky blue', foreground="white")
       Label_4_MARKSHEET.grid(row = 0, column = 0, padx = 101, pady = 5)
       


       #========================================================BUTTONS===================================================================
       Button_1_VIEWINFO = Button(Menu_Frame_1, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __information__)
       Button_1_VIEWINFO.grid(row = 0, column = 3, padx = 50)
       Button_2_VIEWREPORT = Button(Menu_Frame_2, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __FeeReport__)
       Button_2_VIEWREPORT.grid(row = 0, column = 3, padx = 50)
       Button_3_VIEWLIBRARY = Button(Menu_Frame_3, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __Library__)
       Button_3_VIEWLIBRARY.grid(row = 0, column = 3, padx = 50)
       Button_4_VIEWMARKSHEET = Button(Menu_Frame_4, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __marksheet__)
       Button_4_VIEWMARKSHEET.grid(row = 0, column = 3, padx = 50)
       
       

       root.mainloop()


       
       
if __name__ == '__main__':
       menu()
