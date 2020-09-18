from tkinter import *  
import random
import College_Marksheet_Backend
import tkinter.messagebox
from tkinter import ttk

def marking_sheet():
       root = Tk()
       root.title('Marksheet')
       root.geometry('1350x750')
       root.config(bg = 'sky blue')


       name = StringVar()
       roll = StringVar()
       father_name = StringVar()
       mother_name = StringVar()
       date_of_birth = StringVar()
       gender = StringVar()
       school = StringVar()
       email_address = StringVar()
       marks1 = DoubleVar()
       marks2 = DoubleVar()
       marks3 = DoubleVar()
       marks4 = DoubleVar()
       marks5 = DoubleVar()
       grand_tot = DoubleVar()
       percentage = DoubleVar()
       cgpa = DoubleVar()
       grade = StringVar()
       division = StringVar()
       result = StringVar()



       def Add():
              if (len(roll.get()) != 0):
                     College_Marksheet_Backend.insert(name.get(), roll.get(), father_name.get(), mother_name.get(), date_of_birth.get(), gender.get(), \
                                                      school.get(), email_address.get(), marks1.get(), marks2.get(), marks3.get(), marks4.get(), marks5.get(), \
                                                      grand_tot.get(), percentage.get(), cgpa.get(), grade.get(), division.get(), result.get())

       def Update():
              if (len(roll.get()) != 0):
                     College_Marksheet_Backend.update(name.get(), roll.get(), father_name.get(), mother_name.get(), date_of_birth.get(), gender.get(), \
                                                      school.get(), email_address.get(), marks1.get(), marks2.get(), marks3.get(), marks4.get(), marks5.get(), \
                                                      grand_tot.get(), percentage.get(), cgpa.get(), grade.get(), division.get(), result.get())
                    
       def Exit():
              Exit = tkinter.messagebox.askyesno('Marksheet','Confirm if you want to Exit')
              if Exit > 0:
                     root.destroy()
                     return

       
       def Compute():
              num1 = (marks1.get());      num2 = (marks2.get());    num3 = (marks3.get());      num4 = (marks4.get());    num5 = (marks5.get())

              if num1 > 100:
                     tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
                     return
              if num2 > 100:
                     tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
                     return
              if num3 > 100:
                     tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
                     return
              if num4 > 100:
                     tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
                     return
              if num5 > 100:
                     tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
                     return
                     
       
              TOTAL = num1+num2+num3+num4+num5
              grand_tot.set(TOTAL)
              
              Percentage = ((num1 + num2 + num3 + num4 + num5) * 100) / 500
              percentage.set(Percentage)


              c_grades = (((num1+num2+num3+num4+num5) * 100)/500) / 9.5
              cgpa.set(round(c_grades,1))

              if c_grades > 10:
                     cgpa.set(10)


              if (((num1+num2+num3+num4+num5) * 100)/500) <= 40:
                     grades = 'G'
              elif (((num1+num2+num3+num4+num5) * 100)/500) <= 50:
                     grades = 'F'
              elif (((num1+num2+num3+num4+num5) * 100)/500) <= 60:
                     grades = 'E'
              elif (((num1+num2+num3+num4+num5) * 100)/500) <= 70:
                     grades = 'D'
              elif (((num1+num2+num3+num4+num5) * 100)/500) <= 80:
                     grades = 'C'
              elif (((num1+num2+num3+num4+num5) * 100)/500) <= 90:
                     grades = 'B'
              else:
                     grades = 'A'

              grade.set(grades)

              count = 0
              if num1 < 40:
                     count = count + 1
              if num2 < 40:
                     count = count + 1
              if num3 < 40:
                     count = count + 1
              if num4 < 40:
                     count = count + 1
              if num5 < 40:
                     count = count + 1

              if (count == 0):
                     result.set('PASS')
              elif (count == 1 or count == 2 ):
                     result.set('SUPPLY')
              else:
                     result.set('FAIL')

              if Percentage <= 45 and result != "FAIL":
                     division.set('THIRD')
              elif Percentage <= 60 and result != "FAIL":
                     division.set('SECOND')
              elif Percentage <= 100:
                     division.set('FIRST')     

       def Reset():
              name.set(' ')
              roll.set(' ')
              father_name.set(' ')
              mother_name.set(' ')
              date_of_birth.set(' ')
              gender.set(' ')
              school.set(' ')
              email_address.set(' ')
              marks1.set(' ')
              marks2.set(' ')
              marks3.set(' ')
              marks4.set(' ')
              marks5.set(' ')
              grand_tot.set(' ')
              percentage.set(' ')
              cgpa.set(' ')
              grade.set(' ')
              division.set(' ')
              result.set(' ')  
       

       #========================================================Marks_Frame_1===============================================================
       
       Marks_Frame_1 = LabelFrame(root, width = 1200, height = 400, font = ('arial',20,'bold'), bg = 'sky blue', foreground="white", bd = 10, \
                            text = 'Student Details', relief = 'ridge')
       Marks_Frame_1.grid(row = 1, column = 0, pady = 20, padx = 20)


       Name_lbl = Label(Marks_Frame_1, text = 'Name', font = ('arial',15,'bold'), bg = 'sky blue', foreground="white")
       Name_lbl.grid(row = 0, column = 0, padx = 80)
       Name_TxtEntry = Entry(Marks_Frame_1, font = ('arial',15), width = 25, textvariable = name)
       Name_TxtEntry.grid(row = 0, column = 1, padx = 5, pady = 5)

       RollNumber_lbl = Label(Marks_Frame_1, text = 'Roll Number', font = ('arial',15,'bold'), bg = 'sky blue', foreground="white")
       RollNumber_lbl.grid(row = 0, column = 3, padx = 80)
       RollNumber_TxtEntry = Entry(Marks_Frame_1, font = ('arial',15), width = 25, textvariable = roll)
       RollNumber_TxtEntry.grid(row = 0, column = 4, padx = 40)

       fname_lbl = Label(Marks_Frame_1, text = 'Father Name', font = ('arial',15,'bold'), bg = 'sky blue', foreground="white")
       fname_lbl.grid(row = 1, column = 0, padx = 80)
       fname_txtEntry = Entry(Marks_Frame_1, font = ('arial',15), width = 25, textvariable = father_name)
       fname_txtEntry.grid(row = 1, column = 1, padx = 5, pady = 10)

       mname_lbl = Label(Marks_Frame_1, text = 'Mother Name', font = ('arial',15,'bold'), bg = 'sky blue', foreground="white")
       mname_lbl.grid(row = 1, column = 3, padx = 80)
       mname_txtEntry = Entry(Marks_Frame_1, font = ('arial',15), width = 25, textvariable = mother_name)
       mname_txtEntry.grid(row = 1, column = 4, padx = 5)

       dateOFbirth_lbl = Label(Marks_Frame_1, text = 'Date of Birth', font = ('arial',15,'bold'), bg = 'sky blue', foreground="white")
       dateOFbirth_lbl.grid(row = 2, column = 0, padx = 80)
       dateOFbirth_txtEntry = Entry(Marks_Frame_1, font = ('arial',15), width = 25, textvariable = date_of_birth)
       dateOFbirth_txtEntry.grid(row = 2, column = 1, padx = 5, pady = 5)

       gender_lbl = Label(Marks_Frame_1, text = 'Gender', font = ('arial',15,'bold'), bg = 'sky blue', foreground="white")
       gender_lbl.grid(row = 2, column = 3, padx = 80)
       gender_txtEntry = ttk.Combobox(Marks_Frame_1, values = (' ','Male','Female','Others'), font = ('arial',15), width = 23, textvariable = gender)
       gender_txtEntry.grid(row = 2, column = 4, padx = 5, pady = 5)


       school_lbl = Label(Marks_Frame_1, text = 'School Name', font = ('arial',15,'bold'), bg = 'sky blue', foreground="white")
       school_lbl.grid(row = 3, column = 0, padx = 80)
       school_txtEntry = Entry(Marks_Frame_1, font = ('arial',15), width = 25, textvariable = school)
       school_txtEntry.grid(row = 3, column = 1, padx = 5, pady = 5)

       emailAddress_lbl = Label(Marks_Frame_1, text = 'Email ID', font = ('arial',15,'bold'), bg = 'sky blue', foreground="white")
       emailAddress_lbl.grid(row = 3, column = 3, padx = 80)
       emailAddress_txtEntry = Entry(Marks_Frame_1, font = ('arial',15), width = 25, textvariable = email_address)
       emailAddress_txtEntry.grid(row = 3, column = 4, padx = 5, pady = 5)



       Marks_Frame_2 = LabelFrame(root, width = 1200, height = 400, font = ('arial',20,'bold'), bg = 'sky blue', foreground="white", bd = 10 \
                            , text = 'Grades Point Obtained', relief = 'ridge')
       Marks_Frame_2.grid(row = 3, column = 0)





       subject_lbl = Label(Marks_Frame_2, text = 'SUBJECT', font = ('arial',16,'bold'), bg = 'sky blue', foreground="white")
       subject_lbl.grid(row = 3, column = 0, padx = 50, pady = 10)

       marks_obtained_lbl = Label(Marks_Frame_2, text = 'MARKS OBTAINED', font = ('arial',16,'bold'), bg = 'sky blue', foreground="white")
       marks_obtained_lbl.grid(row = 3, column = 1, padx = 20)

       subject_lbl = Label(Marks_Frame_2, text = 'PASSING MARKS', font = ('arial',16,'bold'), bg = 'sky blue', foreground="white")
       subject_lbl.grid(row = 3, column = 2, padx = 20)

       marks_obtained_lbl = Label(Marks_Frame_2, text = 'TOTAL MARKS', font = ('arial',16,'bold'), bg = 'sky blue', foreground="white")
       marks_obtained_lbl.grid(row = 3, column = 3, padx = 20)

       MATHEMATICS_lbl1 = Label(Marks_Frame_2, text = 'MATHEMATICS', font = ('arial',14), bg = 'sky blue', foreground="white")
       MATHEMATICS_lbl1.grid(row = 4, column = 0)
       PHYSICS_lbl2 = Label(Marks_Frame_2, text = 'PHYSICS', font = ('arial',14), bg = 'sky blue', foreground="white")
       PHYSICS_lbl2.grid(row = 5, column = 0)
       CHEMISTRY_lbl3 = Label(Marks_Frame_2, text = 'CHEMISTRY', font = ('arial',14), bg = 'sky blue', foreground="white")
       CHEMISTRY_lbl3.grid(row = 6, column = 0)
       PROGRAMMING_lbl4 = Label(Marks_Frame_2, text = 'PROGRAMMING', font = ('arial',14), bg = 'sky blue', foreground="white")
       PROGRAMMING_lbl4.grid(row = 7, column = 0)
       ENGLISH_lbl5 = Label(Marks_Frame_2, text = 'ENGLISH', font = ('arial',14), bg = 'sky blue', foreground="white")
       ENGLISH_lbl5.grid(row = 8, column = 0)
       GRAND_TOTAL_lbl6 = Label(Marks_Frame_2, text = 'GRAND TOTAL', font = ('arial',16), bg = 'sky blue', foreground="white")
       GRAND_TOTAL_lbl6.grid(row = 9, column = 0)
       PERCENTAGE_lbl7 = Label(Marks_Frame_2, text = 'PERCENTAGE', font = ('arial',16,'bold'), bg = 'sky blue', foreground="white")
       PERCENTAGE_lbl7.grid(row = 10, column = 0)
       CGPA_lbl8 = Label(Marks_Frame_2, text = 'CGPA', font = ('arial',16,'bold'), bg = 'sky blue', foreground="white")
       CGPA_lbl8.grid(row = 10, column = 2)
       GRADE_lbl9 = Label(Marks_Frame_2, text = 'GRADE', font = ('arial',16,'bold'), bg = 'sky blue', foreground="white")
       GRADE_lbl9.grid(row = 10, column = 4)
       DIVISION_lbl10 = Label(Marks_Frame_2, text = 'DIVISION', font = ('arial',16,'bold'), bg = 'sky blue', foreground="white")
       DIVISION_lbl10.grid(row = 11, column = 0)
       DIVISION_lbl10 = Label(Marks_Frame_2, text = 'RESULT', font = ('arial',16,'bold'), bg = 'sky blue', foreground="white")
       DIVISION_lbl10.grid(row = 11, column = 2)
       

       variables_1 = StringVar(Marks_Frame_2, value = '40')
       variables_2 = StringVar(Marks_Frame_2, value = '100')
       variables_3 = StringVar(Marks_Frame_2, value = '500')

       Text_Entry1 = Entry(Marks_Frame_2, font = ('arial',16), width = 5, textvariable = marks1)
       Text_Entry1.grid(row = 4, column = 1)
       Text_Entry2 = Entry(Marks_Frame_2, font = ('arial',16), width = 5, textvariable = marks2)
       Text_Entry2.grid(row = 5, column = 1)
       Text_Entry3 = Entry(Marks_Frame_2, font = ('arial',16), width = 5, textvariable = marks3)
       Text_Entry3.grid(row = 6, column = 1)
       Text_Entry4 = Entry(Marks_Frame_2, font = ('arial',16), width = 5, textvariable = marks4)
       Text_Entry4.grid(row = 7, column = 1)
       Text_Entry5 = Entry(Marks_Frame_2, font = ('arial',16), width = 5, textvariable = marks5)
       Text_Entry5.grid(row = 8, column = 1)
       Text_Entry6 = Entry(Marks_Frame_2, font = ('arial',14), width = 5, textvariable = grand_tot, state = 'readonly')
       Text_Entry6.grid(row = 9, column = 1, pady = 8)
       Text_Entry7 = Entry(Marks_Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = percentage, state = 'readonly')
       Text_Entry7.grid(row = 10, column = 1, pady = 8)
       Text_Entry8 = Entry(Marks_Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = cgpa, state = 'readonly')
       Text_Entry8.grid(row = 10, column = 3, pady = 8)
       Text_Entry9 = Entry(Marks_Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = grade, state = 'readonly')
       Text_Entry9.grid(row = 10, column = 5, padx = 20, pady = 8)
       Text_Entry10 = Entry(Marks_Frame_2, font = ('arial',14,'bold'), width = 8, textvariable = division, state = 'readonly')
       Text_Entry10.grid(row = 11, column = 1, padx = 20, pady = 8)
       Text_Entry11 = Entry(Marks_Frame_2, font = ('arial',14,'bold'), width = 7, textvariable = result, state = 'readonly')
       Text_Entry11.grid(row = 11, column = 3, padx = 20, pady = 8)
       
       Text_Entry_1_2 = Entry(Marks_Frame_2, textvariable = variables_1, font = ('arial',16), width = 5, state = 'readonly')
       Text_Entry_1_2.grid(row = 4, column = 2, pady = 5)
       Text_Entry_1_3 = Entry(Marks_Frame_2, textvariable = variables_2, font = ('arial',16), width = 5, state = 'readonly')
       Text_Entry_1_3.grid(row = 4, column = 3)
       Text_Entry_2_2 = Entry(Marks_Frame_2, textvariable = variables_1, font = ('arial',16), width = 5, state = 'readonly')
       Text_Entry_2_2.grid(row = 5, column = 2, pady = 5)
       Text_Entry_2_3 = Entry(Marks_Frame_2, textvariable = variables_2, font = ('arial',16), width = 5, state = 'readonly')
       Text_Entry_2_3.grid(row = 5, column = 3)
       Text_Entry_3_2 = Entry(Marks_Frame_2, textvariable = variables_1, font = ('arial',16), width = 5, state = 'readonly')
       Text_Entry_3_2.grid(row = 6, column = 2, pady = 5)
       Text_Entry_3_3 = Entry(Marks_Frame_2, textvariable = variables_2, font = ('arial',16), width = 5, state = 'readonly')
       Text_Entry_3_3.grid(row = 6, column = 3)
       Text_Entry_4_2 = Entry(Marks_Frame_2, textvariable = variables_1, font = ('arial',16), width = 5, state = 'readonly')
       Text_Entry_4_2.grid(row = 7, column = 2, pady = 5)
       Text_Entry_4_3 = Entry(Marks_Frame_2, textvariable = variables_2, font = ('arial',16), width = 5, state = 'readonly')
       Text_Entry_4_3.grid(row = 7, column = 3)
       Text_Entry_5_2 = Entry(Marks_Frame_2, textvariable = variables_1, font = ('arial',16), width = 5, state = 'readonly')
       Text_Entry_5_2.grid(row = 8, column = 2, pady = 5)
       Text_Entry_5_3 = Entry(Marks_Frame_2, textvariable = variables_2, font = ('arial',16), width = 5, state = 'readonly')
       Text_Entry_5_3.grid(row = 8, column = 3)
       Text_Entry_6_3 = Entry(Marks_Frame_2, textvariable = variables_3, font = ('arial',16), width = 5, state = 'readonly')
       Text_Entry_6_3.grid(row = 9, column = 3)
                



       Compute_button = Button(Marks_Frame_2, text = 'COMPUTE', font = ('arial',12,'bold'), width = 10, command = Compute)
       Compute_button.grid(row = 4, column = 4, padx = 50, pady = 6)
       Save_button = Button(Marks_Frame_2, text = 'SAVE', font = ('arial',12,'bold'), width = 10, command = Add)
       Save_button.grid(row = 5, column = 4, padx = 50, pady = 6)
       Update_button = Button(Marks_Frame_2, text = 'UPDATE', font = ('arial',12,'bold'), width = 10, command = Update)
       Update_button.grid(row = 6, column = 4, padx = 50, pady = 6)
       Cancel_button = Button(Marks_Frame_2, text = 'RESET', font = ('arial',12,'bold'), width = 10, command = Reset)
       Cancel_button.grid(row = 7, column = 4, padx = 50, pady = 6)
       Exit_button = Button(Marks_Frame_2, text = 'EXIT', font = ('arial',12,'bold'), width = 10, command = Exit)
       Exit_button.grid(row = 8, column = 4, padx = 50, pady = 6)


       root.mainloop()


def search_result_marksheet(row):
       root = Tk()
       root.title('Marksheet')
       root.geometry('1350x750')
       root.config(bg = 'sky blue', foreground="white")

       

       
       def Compute():
              num1 = (marks1.get());      num2 = (marks2.get());    num3 = (marks3.get());      num4 = (marks4.get());    num5 = (marks5.get())                                   
       
              TOTAL = num1+num2+num3+num4+num5
              grand_tot.set(TOTAL)
              
              Percentage = ((num1+num2+num3+num4+num5) * 100)/500
              percentage.set(Percentage)


              c_grades = (((num1+num2+num3+num4+num5) * 100)/500) / 9.5
              cgpa.set(round(c_grades,1))


              if (((num1+num2+num3+num4+num5) * 100)/500) <= 40:
                     grades = 'G'
              elif (((num1+num2+num3+num4+num5) * 100)/500) <= 50:
                     grades = 'F'
              elif (((num1+num2+num3+num4+num5) * 100)/500) <= 60:
                     grades = 'E'
              elif (((num1+num2+num3+num4+num5) * 100)/500) <= 70:
                     grades = 'D'
              elif (((num1+num2+num3+num4+num5) * 100)/500) <= 80:
                     grades = 'C'
              elif (((num1+num2+num3+num4+num5) * 100)/500) <= 90:
                     grades = 'B'
              else:
                     grades = 'A'

              grade.set(grades)

              count = 0
              if num1 < 40:
                     count = count + 1
              if num2 < 40:
                     count = count + 1
              if num3 < 40:
                     count = count + 1
              if num4 < 40:
                     count = count + 1
              if num5 < 40:
                     count = count + 1

              if (count == 0):
                     result.set('PASS')
              elif (count == 1 or count == 2 ):
                     result.set('SUPPLY')
              else:
                     result.set('FAIL')

              if Percentage <= 45 and result != "FAIL":
                     div.set('THIRD')
              elif Percentage <= 60 and result != "FAIL":
                     div.set('SECOND')
              elif Percentage <= 100:
                     div.set('FIRST')     

       
       


       
       Frame_1 = LabelFrame(root, width = 1200, height = 400, font = ('arial',20,'bold'), bg = 'sky blue', foreground="white", bd = 10, \
                            text = 'Student Details', relief = 'ridge')
       Frame_1.grid(row = 1, column = 0, pady = 20, padx = 20)

       name = StringVar(Frame_1,value=row[0][1])
       roll = StringVar(Frame_1,value=row[0][2])
       father_name = StringVar(Frame_1,value=row[0][3])
       mother_name = StringVar(Frame_1,value=row[0][4])
       date_of_birth = StringVar(Frame_1,value=row[0][5])
       gender = StringVar(Frame_1,value=row[0][6])
       school = StringVar(Frame_1,value=row[0][7])
       email_addres = StringVar(Frame_1,value=row[0][8])
       



       lbl_name = Label(Frame_1, text = 'Name', font = ('arial',15,'bold'), bg = 'sky blue', foreground="white")
       lbl_name.grid(row = 0, column = 0, padx = 80)
       Txt_Entry_Name = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = name)
       Txt_Entry_Name.grid(row = 0, column = 1, padx = 5, pady = 5)

       Lbl_Roll_no = Label(Frame_1, text = 'Roll Number', font = ('arial',15,'bold'), bg = 'sky blue', foreground="white")
       Lbl_Roll_no.grid(row = 0, column = 3, padx = 80)
       Txt_Entry_Roll_no = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = roll)
       Txt_Entry_Roll_no.grid(row = 0, column = 4, padx = 40)

       Llb_Father_Name = Label(Frame_1, text = 'Father Name', font = ('arial',15,'bold'), bg = 'sky blue', foreground="white")
       Llb_Father_Name.grid(row = 1, column = 0, padx = 80)
       Txt_Entry_Father_Name = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = father_name)
       Txt_Entry_Father_Name.grid(row = 1, column = 1, padx = 5, pady = 10)

       Lbl_Mother_Name = Label(Frame_1, text = 'Mother Name', font = ('arial',15,'bold'), bg = 'sky blue', foreground="white")
       Lbl_Mother_Name.grid(row = 1, column = 3, padx = 80)
       Txt_Entry_Mother_Name = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = mother_name)
       Txt_Entry_Mother_Name.grid(row = 1, column = 4, padx = 5)

       lbl_DateOFbirth = Label(Frame_1, text = 'Date of Birth', font = ('arial',15,'bold'), bg = 'sky blue', foreground="white")
       lbl_DateOFbirth.grid(row = 2, column = 0, padx = 80)
       Txt_Entry_DateOFbirth = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = date_of_birth)
       Txt_Entry_DateOFbirth.grid(row = 2, column = 1, padx = 5, pady = 5)

       Lbl_Gender = Label(Frame_1, text = 'Gender', font = ('arial',15,'bold'), bg = 'sky blue', foreground="white")
       Lbl_Gender.grid(row = 2, column = 3, padx = 80)
       TXt_Entry_Gender = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = gender)
       TXt_Entry_Gender.grid(row = 2, column = 4, padx = 5, pady = 5)


       Lbl_School = Label(Frame_1, text = 'School Name', font = ('arial',15,'bold'), bg = 'sky blue', foreground="white")
       Lbl_School.grid(row = 3, column = 0, padx = 80)
       Txt_Entry_School = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = school)
       Txt_Entry_School.grid(row = 3, column = 1, padx = 5, pady = 5)

       Lbl_EmailAddress = Label(Frame_1, text = 'Email Address', font = ('arial',15,'bold'), bg = 'sky blue', foreground="white")
       Lbl_EmailAddress.grid(row = 3, column = 3, padx = 80)
       Txt_Entry_EmailAddress = Entry(Frame_1, font = ('arial',15), width = 25, textvariable = email_addres)
       Txt_Entry_EmailAddress.grid(row = 3, column = 4, padx = 5, pady = 5)



       Frame_2 = LabelFrame(root, width = 1200, height = 400, font = ('arial',20,'bold'), bg = 'sky blue', foreground="white", bd = 10 \
                            , text = 'Grades Point Obtained', relief = 'ridge')
       Frame_2.grid(row = 3, column = 0)

       marks1 = DoubleVar(Frame_2,row[0][9])
       marks2 = DoubleVar(Frame_2,row[0][10])
       marks3 = DoubleVar(Frame_2,row[0][11])
       marks4 = DoubleVar(Frame_2,row[0][12])
       marks5 = DoubleVar(Frame_2,row[0][13])
       grand_tot = DoubleVar(Frame_2,row[0][14])
       percentage = DoubleVar(Frame_2,row[0][15])
       cgpa = DoubleVar(Frame_2,row[0][16])
       grade = StringVar(Frame_2,row[0][17])
       div = StringVar(Frame_2,row[0][18])
       result = StringVar(Frame_2,row[0][19])



       Lbl_Sub = Label(Frame_2, text = 'SUBJECT', font = ('arial',16,'bold'), bg = 'sky blue', foreground="white")
       Lbl_Sub.grid(row = 3, column = 0, padx = 50, pady = 10)

       Lbl_obtained_Marks = Label(Frame_2, text = 'MARKS OBTAINED', font = ('arial',16,'bold'), bg = 'sky blue', foreground="white")
       Lbl_obtained_Marks.grid(row = 3, column = 1, padx = 20)

       Lbl_Sub = Label(Frame_2, text = 'PASSING MARKS', font = ('arial',16,'bold'), bg = 'sky blue', foreground="white")
       Lbl_Sub.grid(row = 3, column = 2, padx = 20)

       Lbl_obtained_Marks = Label(Frame_2, text = 'TOTAL MARKS', font = ('arial',16,'bold'), bg = 'sky blue', foreground="white")
       Lbl_obtained_Marks.grid(row = 3, column = 3, padx = 20)

       MATHEMATICS_lbl1 = Label(Frame_2, text = 'MATHEMATICS', font = ('arial',14), bg = 'sky blue', foreground="white")
       MATHEMATICS_lbl1.grid(row = 4, column = 0)
       PHYSICS_lbl2 = Label(Frame_2, text = 'PHYSICS', font = ('arial',14), bg = 'sky blue', foreground="white")
       PHYSICS_lbl2.grid(row = 5, column = 0)
       CHEMISTRY_lbl3 = Label(Frame_2, text = 'CHEMISTRY', font = ('arial',14), bg = 'sky blue', foreground="white")
       CHEMISTRY_lbl3.grid(row = 6, column = 0)
       PROGRAMMING_lbl4 = Label(Frame_2, text = 'PROGRAMMING', font = ('arial',14), bg = 'sky blue', foreground="white")
       PROGRAMMING_lbl4.grid(row = 7, column = 0)
       ENGLISH_lbl5 = Label(Frame_2, text = 'ENGLISH', font = ('arial',14), bg = 'sky blue', foreground="white")
       ENGLISH_lbl5.grid(row = 8, column = 0)
       GRAND_TOTAL_lbl6 = Label(Frame_2, text = 'GRAND TOTAL', font = ('arial',16), bg = 'sky blue', foreground="white")
       GRAND_TOTAL_lbl6.grid(row = 9, column = 0)
       PERCENTAGE_lbl7 = Label(Frame_2, text = 'PERCENTAGE', font = ('arial',16,'bold'), bg = 'sky blue', foreground="white")
       PERCENTAGE_lbl7.grid(row = 10, column = 0)
       CGPA_lbl8 = Label(Frame_2, text = 'CGPA', font = ('arial',16,'bold'), bg = 'sky blue', foreground="white")
       CGPA_lbl8.grid(row = 10, column = 2)
       GRADE_lbbl9 = Label(Frame_2, text = 'GRADE', font = ('arial',16,'bold'), bg = 'sky blue', foreground="white")
       GRADE_lbbl9.grid(row = 10, column = 4)
       DIVISIONRESULT_lbl10 = Label(Frame_2, text = 'DIVISION', font = ('arial',16,'bold'), bg = 'sky blue', foreground="white")
       DIVISIONRESULT_lbl10.grid(row = 11, column = 0)
       DIVISIONRESULT_lbl10 = Label(Frame_2, text = 'RESULT', font = ('arial',16,'bold'), bg = 'sky blue', foreground="white")
       DIVISIONRESULT_lbl10.grid(row = 11, column = 2)
       

       variables_1 = StringVar(Frame_2, value = '40')
       variables_2 = StringVar(Frame_2, value = '100')
       variables_3 = StringVar(Frame_2, value = '500')

       Text_Entry1 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = marks1)
       Text_Entry1.grid(row = 4, column = 1)
       Text_Entry2 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = marks2)
       Text_Entry2.grid(row = 5, column = 1)
       Text_Entry3 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = marks3)
       Text_Entry3.grid(row = 6, column = 1)
       Text_Entry4 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = marks4)
       Text_Entry4.grid(row = 7, column = 1)
       Text_Entry5 = Entry(Frame_2, font = ('arial',16), width = 5, textvariable = marks5)
       Text_Entry5.grid(row = 8, column = 1)
       Text_Entry6 = Entry(Frame_2, font = ('arial',14), width = 5, textvariable = grand_tot)
       Text_Entry6.grid(row = 9, column = 1, pady = 8)
       Text_Entry7 = Entry(Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = percentage)
       Text_Entry7.grid(row = 10, column = 1, pady = 8)
       Text_Entry8 = Entry(Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = cgpa)
       Text_Entry8.grid(row = 10, column = 3, pady = 8)
       Text_Entry9 = Entry(Frame_2, font = ('arial',14,'bold'), width = 5, textvariable = grade)
       Text_Entry9.grid(row = 10, column = 5, padx = 20, pady = 8)
       Text_Entry10 = Entry(Frame_2, font = ('arial',14,'bold'), width = 8, textvariable = div)
       Text_Entry10.grid(row = 11, column = 1, padx = 20, pady = 8)
       Text_Entry11 = Entry(Frame_2, font = ('arial',14,'bold'), width = 7, textvariable = result)
       Text_Entry11.grid(row = 11, column = 3, padx = 20, pady = 8)
       
       Text_Entry_1_2 = Entry(Frame_2, textvariable = variables_1, font = ('arial',16), width = 5)
       Text_Entry_1_2.grid(row = 4, column = 2, pady = 5)
       Text_Entry_1_3 = Entry(Frame_2, textvariable = variables_2, font = ('arial',16), width = 5)
       Text_Entry_1_3.grid(row = 4, column = 3)
       Text_Entry_2_2 = Entry(Frame_2, textvariable = variables_1, font = ('arial',16), width = 5)
       Text_Entry_2_2.grid(row = 5, column = 2, pady = 5)
       Text_Entry_2_3 = Entry(Frame_2, textvariable = variables_2, font = ('arial',16), width = 5)
       Text_Entry_2_3.grid(row = 5, column = 3)
       Text_Entry_3_2 = Entry(Frame_2, textvariable = variables_1, font = ('arial',16), width = 5)
       Text_Entry_3_2.grid(row = 6, column = 2, pady = 5)
       Text_Entry_3_3 = Entry(Frame_2, textvariable = variables_2, font = ('arial',16), width = 5)
       Text_Entry_3_3.grid(row = 6, column = 3)
       Text_Entry_4_2 = Entry(Frame_2, textvariable = variables_1, font = ('arial',16), width = 5)
       Text_Entry_4_2.grid(row = 7, column = 2, pady = 5)
       Text_Entry_4_3 = Entry(Frame_2, textvariable = variables_2, font = ('arial',16), width = 5)
       Text_Entry_4_3.grid(row = 7, column = 3)
       Text_Entry_5_2 = Entry(Frame_2, textvariable = variables_1, font = ('arial',16), width = 5)
       Text_Entry_5_2.grid(row = 8, column = 2, pady = 5)
       Text_Entry_5_3 = Entry(Frame_2, textvariable = variables_2, font = ('arial',16), width = 5)
       Text_Entry_5_3.grid(row = 8, column = 3)
       Text_Entry_6_3 = Entry(Frame_2, textvariable = variables_3, font = ('arial',16), width = 5)
       Text_Entry_6_3.grid(row = 9, column = 3)
                


       
       
       Exit_button = Button(Frame_2, text = 'EXIT', font = ('arial',12,'bold'), width = 10, command = root.destroy)
       Exit_button.grid(row = 8, column = 4, padx = 50, pady = 6)

       
       root.mainloop()

if __name__ == '__main__':
       marking_sheet()
