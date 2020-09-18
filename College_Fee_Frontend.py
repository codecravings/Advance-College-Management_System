from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import datetime
import College_Fee_Backend


class college_fee():
    def __init__(self, master):
        self.master = master
        self.master.title('Fee Report')
        self.master.geometry('1350x750')
        self.master.config(bg='sky blue')


        self.receipts = StringVar()
        self.name = StringVar()
        self.admin = StringVar()
        self.date = StringVar()
        self.branch = StringVar()
        self.semister = StringVar()
        self.total = DoubleVar()
        self.paid = DoubleVar()
        self.due = DoubleVar()


        def Tuple(event):
            try:
                global studentInfo
                index = self.list.curselection()[0]
                studentInfo = self.list.get(index)

                self.receipts_entry.delete(0, END)
                self.receipts_entry.insert(END, studentInfo[1])
                self.studentname_entry.delete(0, END)
                self.studentname_entry.insert(END, studentInfo[2])
                self.collegeAdmin_entry.delete(0, END)
                self.collegeAdmin_entry.insert(END, studentInfo[3])
                self.Date_entry.delete(0, END)
                self.Date_entry.insert(END, studentInfo[4])
                self.collegeBranch_entry.delete(0, END)
                self.collegeBranch_entry.insert(END, studentInfo[5])
                self.semister_entry.delete(0, END)
                self.semister_entry.insert(END, studentInfo[6])
                self.tot_entry.delete(0, END)
                self.tot_entry.insert(END, studentInfo[7])
                self.moneyPaid_entry.delete(0, END)
                self.moneyPaid_entry.insert(END, studentInfo[8])
                self.studdenDdue_entry.delete(0, END)
                self.studdenDdue_entry.insert(END, studentInfo[9])
            except IndexError:
                pass

        def Insert():
            if (len(self.admin.get()) != 0):
                College_Fee_Backend.insert(self.receipts.get(), self.name.get(), self.admin.get(), self.date.get(),
                                           self.branch.get(), self.semister.get(), self.total.get(), self.paid.get(),
                                           self.due.get())
                self.list.delete(0, END)
                self.list.insert(END, (self.receipts.get(), self.name.get(), self.admin.get(), self.date.get(),
                                       self.branch.get(), self.semister.get(), self.total.get(), self.paid.get(),
                                       self.due.get()))

        def View():
            self.list.delete(0, END)
            for row in College_Fee_Backend.view():
                self.list.insert(END, row, str(' '))

        def Reset():
            self.receipts.set(' ')
            self.name.set(' ')
            self.admin.set(' ')
            #self.date.set(' ')
            self.branch.set(' ')
            self.semister.set(' ')
            self.paid.set(' ')
            self.due.set(' ')
            self.Display.delete('1.0', END)
            self.list.delete(0, END)

        def Delete():
            College_Fee_Backend.delete(studentInfo[0])
            Reset()
            View()

        def Receipt():
            self.Display.delete('1.0', END)
            self.Display.insert(END, '\t\tRECEIPT' + '\n\n')
            self.Display.insert(
                END, '\tReceipt No.\t     :' + self.receipts.get() + '\n')
            self.Display.insert(END, '\tStudent Name  :' +
                                self.name.get() + '\n')
            self.Display.insert(END, '\tAdmission No.\t:' +
                                self.admin.get() + '\n')
            self.Display.insert(
                END, '\tDate\t          :' + self.date.get() + '\n')
            self.Display.insert(
                END, '\tBranch\t          :' + self.branch.get() + '\n')
            self.Display.insert(
                END, '\tSemester \t        :' + self.semister.get() + '\n\n')

            x1 = (self.var_1.get())
            x2 = (self.paid.get())
            x3 = (x1 - x2)

            self.Display.insert(END, '\tTotal Amount  :' + str(x1) + '\n')
            self.Display.insert(END, '\tPaid Amount   :' + str(x2) + '\n')
            self.Display.insert(END, '\tBalance\t         :' + str(x3) + '\n')

            self.due.set(x3)

        def Search():
            self.list.delete(0, END)
            for row in College_Fee_Backend.search(self.receipts.get(), self.name.get(), self.admin.get(), self.date.get(),
                                                  self.branch.get(), self.semister.get(), self.total.get(), self.paid.get(),
                                                  self.due.get()):
                self.list.insert(END, row, str(' '))

        def Update():
            College_Fee_Backend.delete(studentInfo[0])
            Insert()

        def Exit():
            Exit = tkinter.messagebox.askyesno(
                'Attention', 'Confirm, if you want to Exit')
            if Exit > 0:
                root.destroy()
                return


        College_Main_Frame = Frame(self.master, bg='sky blue')
        College_Main_Frame.grid()

        College_Title_Frame = LabelFrame(
            College_Main_Frame, width=1350, height=100, bg='sky blue', relief='ridge', bd=15)
        College_Title_Frame.pack(side=TOP)

        self.lblTitle = Label(College_Title_Frame, font=('arial', 40, 'bold'), text='FEE REPORT',
                              bg='skyblue', padx=13, foreground="white")
        self.lblTitle.grid(padx=400)

        College_Data_Frame = Frame(College_Main_Frame, width=1350, height=350,
                           bg='sky blue', relief='ridge', bd=15)
        College_Data_Frame.pack(side=TOP, padx=15)

        College_Frame_1 = LabelFrame(College_Data_Frame, width=850, height=350, bg='sky blue', relief='ridge', bd=8,
                             text='Informations', font=('arial', 15, 'bold'), foreground="white")
        College_Frame_1.pack(side=LEFT, padx=10)

        College_Frame_2 = LabelFrame(College_Data_Frame, width=495, height=350, bg='sky blue', relief='ridge', bd=8,
                             text='Fee Receipt', foreground="white", font=('arial', 15, 'bold'))
        College_Frame_2.pack(side=RIGHT, padx=10)

        College_List_Frame = Frame(College_Main_Frame, width=1350, height=150,
                           bg='sky blue', relief='ridge', bd=15)
        College_List_Frame.pack(side=TOP, padx=15)

        Btn_Frame = Frame(College_Main_Frame, width=1350, height=80,
                          bg='sky blue', relief='ridge', bd=15)
        Btn_Frame.pack(side=TOP)


        self.receipts_lbl = Label(College_Frame_1, text='Receipt No. : ', font=(
            'arial', 14, 'bold'), bg='sky blue', foreground="white")
        self.receipts_lbl.grid(row=0, column=0, padx=15, sticky=W)

        self.studentName_lbl = Label(College_Frame_1, text='Student Name : ', font=(
            'arial', 14, 'bold'), bg='sky blue', foreground="white")
        self.studentName_lbl.grid(row=1, column=0, padx=15, sticky=W)

        self.collegeAdmin_lbl = Label(College_Frame_1, text='Admission No. : ', font=(
            'arial', 14, 'bold'), bg='sky blue', foreground="white")
        self.collegeAdmin_lbl.grid(row=2, column=0, padx=15, sticky=W)

        self.Date_lbl = Label(College_Frame_1, text='Date : ', font=(
            'arial', 14, 'bold'), bg='sky blue', foreground="white")
        self.Date_lbl.grid(row=3, column=0, padx=15, sticky=W)

        self.college_branch_lbl = Label(College_Frame_1, text='Branch : ', font=(
            'arial', 14, 'bold'), bg='sky blue', foreground="white")
        self.college_branch_lbl.grid(row=4, column=0, padx=15, sticky=W)

        self.semister_lbl = Label(College_Frame_1, text='Semester : ', font=(
            'arial', 14, 'bold'), bg='sky blue', foreground="white")
        self.semister_lbl.grid(row=5, column=0, padx=15, sticky=W)

        self.total_lbl = Label(College_Frame_1, text='TOTAL AMOUNT : ', font=(
            'arial', 14, 'bold'), bg='sky blue', foreground="white")
        self.total_lbl.grid(row=2, column=2, padx=5, sticky=W)

        self.paid_lbl = Label(College_Frame_1, text='PAID AMOUNT : ', font=(
            'arial', 14, 'bold'), bg='sky blue', foreground="white")
        self.paid_lbl.grid(row=3, column=2, padx=5, sticky=W)

        self.due_lbl = Label(College_Frame_1, text='BALANCE : ', font=(
            'arial', 14, 'bold'), bg='sky blue', foreground="white")
        self.due_lbl.grid(row=4, column=2, padx=5, sticky=W)


        self.var_1 = DoubleVar(College_Frame_1, value='36265')
        d1 = datetime.date.today()
        self.date.set(d1)

        self.receipts_entry = Entry(College_Frame_1, font=(
            'arial', 14), textvariable=self.receipts)
        self.receipts_entry.grid(row=0, column=1, padx=15, pady=5)

        self.studentname_entry = Entry(College_Frame_1, font=(
            'arial', 14), textvariable=self.name)
        self.studentname_entry.grid(row=1, column=1, padx=15, pady=5)

        self.collegeAdmin_entry = Entry(College_Frame_1, font=(
            'arial', 14), textvariable=self.admin)
        self.collegeAdmin_entry.grid(row=2, column=1, padx=15, pady=5)

        self.Date_entry = Entry(College_Frame_1, font=(
            'arial', 14), textvariable=self.date)
        self.Date_entry.grid(row=3, column=1, padx=15, pady=5)

        self.collegeBranch_entry = ttk.Combobox(College_Frame_1, values=(' ', 'CSE', 'IT', 'ETC/ET&T', 'Mechanical Engineer', 'Civil Engineer', 'IT/CT', 'Electrical Engineer'),
                                                font=('arial', 14), width=19, textvariable=self.branch)
        self.collegeBranch_entry.grid(row=4, column=1, padx=15, pady=5)

        self.semister_entry = ttk.Combobox(College_Frame_1, values=(' ', 'FIRST', 'SECOND', 'THIRD'), font=('arial', 14), width=19,
                                           textvariable=self.semister)
        self.semister_entry.grid(row=5, column=1, padx=15, pady=5)

        self.tot_entry = Entry(College_Frame_1, font=(
            'arial', 14), width=10, textvariable=self.var_1, state='readonly')
        self.tot_entry.grid(row=2, column=3, padx=8, pady=5)

        self.moneyPaid_entry = Entry(College_Frame_1, font=(
            'arial', 14), width=10, textvariable=self.paid)
        self.moneyPaid_entry.grid(row=3, column=3, pady=5)

        self.studdenDdue_entry = Entry(College_Frame_1, font=(
            'arial', 14), width=10, textvariable=self.due)
        self.studdenDdue_entry.grid(row=4, column=3, pady=7)


        self.Display = Text(College_Frame_2, width=42, height=12,
                            font=('arial', 14, 'bold'))
        self.Display.grid(row=0, column=0, padx=3)

        sb = Scrollbar(College_List_Frame)
        sb.grid(row=0, column=1, sticky='ns')

        self.list = Listbox(College_List_Frame, font=(
            'arial', 13, 'bold'), width=140, height=8)
        self.list.bind('<<ListboxSelect>>', Tuple)
        self.list.grid(row=0, column=0)
        sb.config(command=self.list.yview)


        button_Save = Button(Btn_Frame, text='SAVE', font=(
            'arial', 14, 'bold'), width=10, command=Insert)
        button_Save.grid(row=0, column=0, padx=5, pady=5)

        button_display = Button(Btn_Frame, text='DISPLAY', font=(
            'arial', 14, 'bold'), width=10, command=View)
        button_display.grid(row=0, column=1, padx=5, pady=5)

        button_Reset = Button(Btn_Frame, text='RESET', font=(
            'arial', 14, 'bold'), width=10, command=Reset)
        button_Reset.grid(row=0, column=2, padx=5, pady=5)

        button_Reset = Button(Btn_Frame, text='UPDATE', font=(
            'arial', 14, 'bold'), width=10, command=Update)
        button_Reset.grid(row=0, column=3, padx=5, pady=5)

        button_Search = Button(Btn_Frame, text='SEARCH', font=(
            'arial', 14, 'bold'), width=10, command=Search)
        button_Search.grid(row=0, column=4, padx=5, pady=5)

        button_Delete = Button(Btn_Frame, text='DELETE', font=(
            'arial', 14, 'bold'), width=10, command=Delete)
        button_Delete.grid(row=0, column=5, padx=5, pady=5)

        button_Receipt = Button(Btn_Frame, text='RECEIPT', font=(
            'arial', 14, 'bold'), width=10, command=Receipt)
        button_Receipt.grid(row=0, column=6, padx=5, pady=5)

        button_Exit = Button(Btn_Frame, text='EXIT', font=(
            'arial', 14, 'bold'), width=10, command=Exit)
        button_Exit.grid(row=0, column=7, padx=5, pady=5)


root = Tk()
obj = college_fee(root)
root.mainloop()
