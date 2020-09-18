from tkinter import*
import tkinter.messagebox
import os


def main():
    root = Tk()
    app = Screen_Window_1(root)


class Screen_Window_1:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Window")
        self.master.geometry('1350x750')
        self.master.config(bg = 'lightskyblue')
        self.Frame = Frame(self.master, bg = 'lightskyblue')
        self.Frame.pack()


        self.u_name = StringVar()                             # x = StringVar()  Holds a string; default value is " "
        self.u_password = StringVar()

        self.Lbl_Title_Login = Label(self.Frame, text ='Login Menu', font = ('arial', 55, 'bold'), bg ='lightskyblue', foreground="white")
        self.Lbl_Title_Login.grid(row = 0, column = 0, columnspan =3, pady = 40)
        
        self.Log_Frame_1 = LabelFrame(self.Frame, width = 1350, height = 600, relief ='ridge', foreground="white", bg ='lightskyblue', bd = 15,
                                      font = ('arial',20,'bold'))
        self.Log_Frame_1.grid(row = 1, column =0)
        self.Log_Frame_2 = LabelFrame(self.Frame, width = 1000, height = 600, relief ='ridge', foreground="white", bg ='lightskyblue', bd = 15,
                                      font = ('arial',20,'bold'))
        self.Log_Frame_2.grid(row = 2, column = 0)


        #===================================================LABEL and ENTRIES=======================================================================
        self.lbl_uname = Label(self.Log_Frame_1, text ='Username', foreground="white", font = ('arial', 20, 'bold'), bg ='lightskyblue', bd = 20)
        self.lbl_uname.grid(row = 0, column = 0)
        self.txt_uname = Entry(self.Log_Frame_1, font = ('arial', 20, 'bold'), textvariable = self.u_name)
        self.txt_uname.grid(row = 0, column = 1, padx = 50)
        
        self.lbl_pass = Label(self.Log_Frame_1, text ='Password', foreground="white", font = ('arial', 20, 'bold'), bg ='lightskyblue', bd = 20)
        self.lbl_pass.grid(row = 1, column = 0)
        self.txt_pass = Entry(self.Log_Frame_1, font = ('arial', 20, 'bold'), show ='*', textvariable = self.u_password)
        self.txt_pass.grid(row = 1, column = 1)
        
        
        #=============================================================BUTTONS=======================================================================
        self.login_button = Button(self.Log_Frame_2, text ='Login', width = 10, font = ('airia', 15, 'bold'), command = self.Login)
        self.login_button.grid(row = 3, column = 0, padx = 8, pady = 20)

        self.reset_button = Button(self.Log_Frame_2, text ='Reset', width = 10, font = ('airia', 15, 'bold'), command = self.Reset)
        self.reset_button.grid(row = 3, column = 1, padx = 8, pady = 20)

        self.exit_button = Button(self.Log_Frame_2, text ='Exit', width = 10, font = ('airia', 15, 'bold'), command = self.Exit)
        self.exit_button.grid(row = 3, column = 2, padx = 8, pady = 20)


        #======================================================Code for Login Button==================================================================
    def Login(self):
        u = (self.u_name.get())
        p = (self.u_password.get())

        if (u == str('adones') and p == str(1)):
            self.__menu__()
        else:
            tkinter.messagebox.askyesno("Login","Error : Wrong Password")
            self.u_name.set("")
            self.u_password.set("")
            #self.text_Username.focus()

        
        #======================================================Code for Reset Button==================================================================
    def Reset(self):
         self.u_name.set("")
         self.u_password.set("")
         self.txt_uname.focus()


        #======================================================Code for Exit Button==================================================================

    def Exit(self):
        self.Exit = tkinter.messagebox.askokcancel("Login System", "Confirm if you want to Exit")
        if self.Exit > 0:
            self.master.destroy()
            return

    def __menu__(self):
        filename = 'College_Menu.py'
        os.system(filename)
        os.system('notepad'+filename)

    '''def new_window(self):
        self.new_Window = Toplevel(self.master)
        self.app = Window_2(self.new_Window)'''

class Screen_Window_2:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Main Menu")
        self.master.geometry('1350x750')
        self.master.config(bg = 'sky blue')
        self.Frame = Frame(self.master, bg = 'lightskyblue')
        self.Frame.pack()

    

if __name__ == '__main__':
    main()                                              


