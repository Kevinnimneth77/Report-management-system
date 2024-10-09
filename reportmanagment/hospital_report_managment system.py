from tkinter import*
from tkinter import ttk
from PIL import ImageTk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
import self

from PIL import Image as PILImage
from PIL import ImageTk
import tkinter as tk

window = Tk()

window.geometry('1920x1080+0+0')
window.title('Login Sytem hospital Maangement System')
window.resizable(False,False)

backgroundImage=ImageTk.PhotoImage(file='bg1 (3).jpg')

bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

def menu():
    #loginFrame = Frame(window, bg='#131313', bd=0)
    #loginFrame.place(x=1050,y=50, width=800, height=950)  # 1300x,550y

    borderFrame=Frame(window, width=800, height=950, highlightbackground='gold', highlightcolor='yellow', background='#131313',
          highlightthickness=3)
    borderFrame.place(x=1050,y=50)

    l1 = Label(window, text="M ", fg='blue', bg='#131313', font=('SimSun', 75, 'bold'))
    l1.place(x=1190, y=90)

    Label(window, text="edDoc", fg='white', bg='#131313', font=('SimSun', 65, 'bold')).place(x=1250,
                                                                                             y=100)
    Label(window, text="Care", fg='white', bg='#131313', font=('SimSun', 65, 'bold')).place(x=1530,
                                                                                                y=100)

    Label(window, text="Choose the right theme for medical ", fg='white', bg='#131313',
          font=('SimSun', 25, 'bold')).place(x=1110,
                                             y=290)#fg='#154360'

    Label(window, text="report.", fg='white', bg='#131313',
          font=('SimSun', 25, 'bold')).place(x=1670,
                                             y=330)

    Label(window, text="Any successful career starts with good medical. Together with ",
          fg='#5499C7', bg='#131313', font=('SimSun', 15, 'bold')).place(x=1110,
                                                                       y=450)
    Label(window, text="us you will have deeper knowledge of the subjects that will ",
          fg='#5499C7', bg='#131313', font=('SimSun', 15, 'bold')).place(x=1110,
                                                                       y=480)
    Label(window, text="be espectally useful for you when climbing thecareer ladder.", fg='#5499C7', bg='#131313',
          font=('SimSun', 15, 'bold')).place(x=1110,
                                             y=510)

    Label(window, text="joing with MCQ master.",
          fg='#5499C7', bg='#131313',
          font=('SimSun', 15, 'bold')).place(x=1110,
                                             y=540)

    Button(window, text="Doctor's Side", fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=1150, y=700, height=50, width=600)

    Button(window, command=logingpage,text="Patient's Side", fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=1150, y=800, height=50, width=600)


def logingpage():
    mainF = Frame(window, bg='#fff')
    mainF.place(width=1980, height=1200)

    img = ImageTk.PhotoImage(PILImage.open("WhatsApp Image 2024-08-01 at 12.32.09_5855e790.jpg").resize((500, 500)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=500, width=500, x=700, y=180)


    Label(mainF, text="M", fg='blue', bg='white', font=('SimSun', 75, 'bold')).place(x=700,
                                                                                     y=50)

    Label(mainF, text="edDoc", fg='black', bg='white', font=('SimSun', 65, 'bold')).place(x=760,
                                                                                          y=60)
    Label(mainF, text="Care", fg='black', bg='white', font=('SimSun', 65, 'bold')).place(x=1040,

                                                                                         y=60)

    Button(mainF, text='Sign in', command=signin, fg='white', bg='blue', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 18, 'bold')).place(x=700, y=750, height=50, width=550)

    Button(mainF, text='Register', command=register, fg='white', bg='blue', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 18, 'bold')).place(x=700, y=850, height=50, width=550)

def signin():

    global e_1,e_2

    mainF = Frame(window, bg='#fff')
    mainF.place(width=1980, height=1200)

    #img = ImageTk.PhotoImage(file='bg1.jpg')
    #bgLabel = Label(mainF, image=img)
    #bgLabel.place( x=1100, y=80)

    img = ImageTk.PhotoImage(PILImage.open("WhatsApp Image 2024-08-01 at 12.32.09_5855e790.jpg").resize((500, 500)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=500, width=500, x=1100, y=80)


    Frame(mainF, width=750, height=600, highlightbackground='blue', highlightcolor='yellow', background='white',
          highlightthickness=3).place(x=100,
                                      y=300)

    #Label(mainF, text="M C Q", fg='blue', bg='white', font=('SimSun', 65, 'bold')).place(x=100,y=100)

    Label(mainF, text="M", fg='blue', bg='white', font=('SimSun', 75, 'bold')).place(x=200,
                                                                                         y=70)

    Label(mainF, text="edDoc", fg='black',bg='white', font=('SimSun', 65, 'bold')).place(x=260,
                                                                                                                  y=80)
    Label(mainF, text="Care", fg='black', bg='white', font=('SimSun', 65, 'bold')).place(x=540,

                                                                                        y=80)
    #Label(mainF, text="Available Courses", fg='#EF930C', bg='white',
          #font=('SimSun', 20, 'bold')).place(x=300,
                                             #y=250)
    Label(mainF, text="Sign in", fg='blue',bg='white', border=0,
           font=('SimSun', 25, 'bold')).place(x=400, y=350)


    def on_enter(e):
        e_1.delete(0,'end')

    def on_leave(e):
        name=e_1.get()
        if name=='' :
            e_1.insert(0,'User Name')

    e_1 = Entry(mainF, border=0, bg='#dddddd', fg='#929292',font=('SimSun', 13))
    e_1.place(width=550, height=50, x=200, y=425)
    e_1.insert(0, 'User Name')
    e_1.bind('<FocusIn>',on_enter)
    e_1.bind('<FocusOut>',on_leave)


    def on_enter(e):
        e_2.delete(0,'end')

    def on_leave(e):
        password=e_2.get()
        if password=='' :
            e_2.insert(0,'Password')

    e_2 = Entry(mainF,  border=0, bg='#dddddd', fg='#929292',font=('SimSun', 13))
    e_2.place(width=550, height=50, x=200, y=500)
    e_2.insert(0, 'Password')
    e_2.bind('<FocusIn>', on_enter)
    e_2.bind('<FocusOut>', on_leave)

    Button(mainF, text='Sign in',command=login, fg='white', bg='blue', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 18, 'bold')).place(x=200, y=650, height=50, width=550)

    Checkbutton(mainF, text='Remember Password', fg='black', bg='white', border=0, activebackground='white',
           font=('SimSun', 15)).place(x=200, y=580, height=50, width=550)

    Label(mainF, text="Don't you have an account ?", fg='black', bg='white', border=0,
          font=('SimSun', 15)).place(x=280, y=750)
    Button(mainF, text='Sign up',command=register, fg='blue', bg='white', border=0,activebackground='white',
           activeforeground='#76448A', font=('SimSun', 15, 'bold')).place(x=550, y=750)

def login():

    if e_1.get() == '' or e_2.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif e_1.get() == 'kevin' and e_2.get() == '123456':
        messagebox.showinfo('Success', 'Welcome')
        #APP.destroy()
        hospital()

    else:
        messagebox.showerror('Error', 'Please enter correct credentials')

def register():
    mainF = Frame(window, bg='#fff')
    mainF.place(width=1920, height=1200)

    #img = ImageTk.PhotoImage(Image.open("login.png").resize((500, 500)))
    #l = Label(mainF, image=img)
    #l.img = img
    #l.place(height=500, width=500, x=1100, y=80)

    img = ImageTk.PhotoImage(PILImage.open("WhatsApp Image 2024-08-01 at 12.32.09_5855e790.jpg").resize((500, 500)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=500, width=500, x=1100, y=80)





    Frame(mainF,width=750,height=650,highlightbackground='blue',highlightcolor='yellow',background='white',highlightthickness=3).place(x=100,
                                                                                         y=250)

    #Label(mainF, text="M C Q", fg='blue', bg='white', font=('SimSun', 65, 'bold')).place(x=100,y=100)

    Label(mainF, text="M", fg='blue', bg='white', font=('SimSun', 75, 'bold')).place(x=200,
                                                                                     y=70)

    Label(mainF, text="edDoc", fg='black', bg='white', font=('SimSun', 65, 'bold')).place(x=260,
                                                                                          y=80)
    Label(mainF, text="Care", fg='black', bg='white', font=('SimSun', 65, 'bold')).place(x=540,

                                                                                         y=80)
    #Label(mainF, text="Available Courses", fg='#EF930C', bg='white',
          #font=('SimSun', 20, 'bold')).place(x=300,
                                             #y=250)
    Label(mainF, text="Register", fg='blue',bg='white', border=0,
           font=('SimSun', 25, 'bold')).place(x=400, y=275)


    def on_enter(e):
        e_1.delete(0,'end')

    def on_leave(e):
        name=e_1.get()
        if name=='' :
            e_1.insert(0,'User Name')

    e_1 = Entry(mainF, border=0, bg='#dddddd', fg='#929292',font=('SimSun', 13))
    e_1.place(width=550, height=50, x=200, y=350)
    e_1.insert(0, 'User Name')
    e_1.bind('<FocusIn>',on_enter)
    e_1.bind('<FocusOut>',on_leave)


    def on_enter(e):
        e_3.delete(0,'end')

    def on_leave(e):
        email=e_3.get()
        if email=='' :
            e_3.insert(0,'Email')

    e_3 = Entry(mainF, border=0, bg='#dddddd', fg='#929292',font=('SimSun', 13))
    e_3.place(width=550, height=50, x=200, y=425)
    e_3.insert(0, 'Email')
    e_3.bind('<FocusIn>',on_enter)
    e_3.bind('<FocusOut>',on_leave)


    def on_enter(e):
        e_2.delete(0,'end')

    def on_leave(e):
        password=e_2.get()
        if password=='' :
            e_2.insert(0,'Password')

    e_2 = Entry(mainF,  border=0, bg='#dddddd', fg='#929292',font=('SimSun', 13))
    e_2.place(width=550, height=50, x=200, y=500)
    e_2.insert(0, 'Password')
    e_2.bind('<FocusIn>', on_enter)
    e_2.bind('<FocusOut>', on_leave)


    def on_enter(e):
        e_4.delete(0,'end')

    def on_leave(e):
        cmps=e_4.get()
        if cmps=='' :
            e_4.insert(0,'Conform Password')

    e_4 = Entry(mainF, border=0, bg='#dddddd', fg='#929292',font=('SimSun', 13))
    e_4.place(width=550, height=50, x=200, y=575)
    e_4.insert(0, 'Conform Password')
    e_4.bind('<FocusIn>',on_enter)
    e_4.bind('<FocusOut>',on_leave)

    Button(mainF, text='Register',command=signin, fg='white', bg='blue', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 18, 'bold')).place(x=200, y=725, height=50, width=550)

    Checkbutton(mainF, text='Agree our term and conditions', fg='black', bg='white', border=0, activebackground='white',
           font=('SimSun', 15)).place(x=200, y=655, height=50, width=550)

    Label(mainF, text="Do you have an account ?", fg='black', bg='white', border=0,
          font=('SimSun', 15)).place(x=300, y=825)
    Button(mainF, text='Login Here',command=signin , fg='blue', bg='white', border=0,activebackground='white',
           activeforeground='#76448A', font=('SimSun', 15, 'bold')).place(x=550, y=825)




def hospital():
    root=Tk()
    root.title("Hospital Managment System")
    root.geometry("1980x1200+0+0")

    Lbltitle=Label(root,bd=20,relief=RIDGE,text="HOSPITAL REPORT MANAGMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
    Lbltitle.pack(side=TOP,fill=X)

        # ==============================Dataframe=========================

    Dataframe = Frame(root, bd=20, relief=RIDGE)
    Dataframe.place(x=0, y=130, width=1980, height=400)

    DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,font=("araial", 12, "bold"),text="Patient Information")
    DataframeLeft.place(x=0, y=5, width=980, height=350)

    DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("araial", 12, "bold"),text="Prescription")
    DataframeRight.place(x=990, y=5, width=980, height=350)


        # ====================button frame====================

    Buttonframe=Frame(root,bd=20,relief=RIDGE)
    Buttonframe.place(x=0,y=600,width=1990,height=70)

        # ============= Details frame==========================

    Buttonframe = Frame(root, bd=20, relief=RIDGE)
    Buttonframe.place(x=0, y=600, width=19000, height=1900)

        # ============== Data frameleft==========

    LblNameTablet=Label(DataframeLeft,text="Names of Tablet",  font=("times new roman", 12, "bold"),padx=2,pady=6)
    LblNameTablet.grid(row=0,column=0)

    comNametablet=ttk.Combobox(DataframeLeft,font=("times new roman", 12, "bold"),width=44)

    comNametablet["value"]=("Nice","Corona Vacacine","Accetaminophen","Adderall","Adderall","Amlodipine","Ativan")
    comNametablet.grid(row=0,column=1)

    lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Refence No:",padx=2)
    lblref.grid(row=1,column=0)
    txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
    txtref.grid(row=1,column=1)

    lblref = Label(DataframeLeft,font=("arial", 12, "bold"), text="Dose:", padx=2)
    lblref.grid(row=2, column=0)
    txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
    txtref.grid(row=2, column=1)

    lblref = Label(DataframeLeft,font=("arial", 12, "bold"), text="No of Tablets:", padx=2)
    lblref.grid(row=3, column=0)
    txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
    txtref.grid(row=3, column=1)

    lblref = Label(DataframeLeft,font=("arial", 12, "bold"), text="Lot:", padx=2)
    lblref.grid(row=4, column=0)
    txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
    txtref.grid(row=4, column=1)

    lblref = Label(DataframeLeft, font=("arial", 12, "bold"), text="issue Date:", padx=2)
    lblref.grid(row=5, column=0)
    txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
    txtref.grid(row=5, column=1)

    lblref = Label(DataframeLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2)
    lblref.grid(row=6, column=0)
    txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
    txtref.grid(row=6, column=1)

    lblref = Label(DataframeLeft, font=("arial", 12, "bold"), text="Daily Dose:", padx=2)
    lblref.grid(row=7, column=0)
    txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
    txtref.grid(row=7, column=1)

    lblref = Label(DataframeLeft, font=("arial", 12, "bold"), text="Side Effects:", padx=2)
    lblref.grid(row=8, column=0)
    txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
    txtref.grid(row=8, column=1)

    lblref = Label(DataframeLeft, font=("arial", 12, "bold"), text="Further Information:", padx=2)
    lblref.grid(row=9, column=0)
    txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
    txtref.grid(row=9, column=1)

    lblref = Label(DataframeLeft, font=("arial", 12, "bold"), text="Blood pressure:", padx=2)
    lblref.grid(row=10, column=0)
    txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
    txtref.grid(row=10, column=1)

    lblref = Label(DataframeLeft, font=("arial", 12, "bold"), text="Storage Advice:", padx=2)
    lblref.grid(row=11, column=0)
    txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
    txtref.grid(row=11, column=1)

    lblref = Label(DataframeLeft, font=("arial", 12, "bold"), text="Medication:", padx=2)
    lblref.grid(row=1, column=2)
    txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
    txtref.grid(row=1, column=3)

    lblref = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Id:", padx=2)
    lblref.grid(row=2, column=2)
    txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
    txtref.grid(row=2, column=3)

    lblref = Label(DataframeLeft, font=("arial", 12, "bold"), text="NHS Number:", padx=2)
    lblref.grid(row=3, column=2)
    txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
    txtref.grid(row=3, column=3)

    lblref = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Name:", padx=2)
    lblref.grid(row=4, column=2)
    txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
    txtref.grid(row=4, column=3)

    lblref = Label(DataframeLeft, font=("arial", 12, "bold"), text="Date of Birth:", padx=2)
    lblref.grid(row=5, column=0)
    txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
    txtref.grid(row=5, column=1)

    lblref = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Address:", padx=2)
    lblref.grid(row=6, column=0)
    txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
    txtref.grid(row=6, column=1)










        








#root=Tk()
#ob=Hospital(root)
#root.mainloop()

menu()
window.mainloop()