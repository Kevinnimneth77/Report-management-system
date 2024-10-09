from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
import self


class Hospital:
    def __init__(self, root, w=None):
        self.root=root
        self.root.title("Hospital Managment System")
        self.root.geometry("1980x1200+0+0")

        Lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL REPORT MANAGMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        Lbltitle.pack(side=TOP,fill=X)

        # ==============================Dataframe=========================

        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1980, height=400)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,font=("araial", 12, "bold"),text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("araial", 12, "bold"),text="Prescription")
        DataframeRight.place(x=990, y=5, width=980, height=350)


        # ====================button frame====================

        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=600,width=1990,height=70)

        # ============= Details frame==========================

        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=600, width=19000, height=1900)

        # ============== Data frameleft==========

        LblNameTablet=Label(DataframeLeft,text="Names of Tablet",  font=("times new roman", 12, "bold"),padx=2,pady=6)
        LblNameTablet.grid(row=0,column=0)

        comNametablet=ttk.Combobox(DataframeLeft,font=("times new roman", 12, "bold"),width=44)

        comNametablet["value"]=("Nice","Corona Vacacine","Accetaminophen","Adderall","Adderall","Amlodipine","Ativan")
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Refence No:",padx=2)
        lblref.grid(row=1,column=0,sticky=w)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtref.grid(row=1,column=1)

        lblref = Label(DataframeLeft,font=("arial", 12, "bold"), text="Dose:", padx=2)
        lblref.grid(row=2, column=0, sticky=w)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=2, column=1)

        lblref = Label(DataframeLeft,font=("arial", 12, "bold"), text="No of Tablets:", padx=2)
        lblref.grid(row=3, column=0, sticky=w)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=3, column=1)

        lblref = Label(DataframeLeft,font=("arial", 12, "bold"), text="Lot:", padx=2)
        lblref.grid(row=4, column=0, sticky=w)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=4, column=1)

        lblref = Label(DataframeLeft,font=("arial", 12, "bold"), text="issue Date:", padx=2)
        lblref.grid(row=5, column=0, sticky=w)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=5, column=1)

        lblref = Label(DataframeLeft,font=("arial", 12, "bold"), text="Exp Date:", padx=2)
        lblref.grid(row=6, column=0, sticky=w)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=6, column=1)

        lblref = Label(DataframeLeft,font=("arial", 12, "bold"), text="Daily Dose:", padx=2)
        lblref.grid(row=7, column=0, sticky=w)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=7, column=1)

        lblref = Label(DataframeLeft,font=("arial", 12, "bold"), text="Side Effects:", padx=2)
        lblref.grid(row=8, column=0, sticky=w)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=8, column=1)

        lblref = Label(DataframeLeft,font=("arial", 12, "bold"), text="Further Information:", padx=2)
        lblref.grid(row=9, column=0, sticky=w)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=9, column=1)

        lblref = Label(DataframeLeft,font=("arial", 12, "bold"), text="Blood pressure:", padx=2)
        lblref.grid(row=10, column=0, sticky=w)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=10, column=1)

        lblref = Label(DataframeLeft,font=("arial", 12, "bold"), text="Storage Advice:", padx=2)
        lblref.grid(row=11, column=0, sticky=w)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=11, column=1)

        lblref = Label(DataframeLeft,font=("arial", 12, "bold"), text="Medication:", padx=2)
        lblref.grid(row=1, column=2, sticky=w)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=1, column=3)

        lblref = Label(DataframeLeft,font=("arial", 12, "bold"), text="Patient Id:", padx=2)
        lblref.grid(row=2, column=2, sticky=w)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=2, column=3)

        lblref = Label(DataframeLeft,font=("arial", 12, "bold"), text="NHS Number:", padx=2)
        lblref.grid(row=3, column=2, sticky=w)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=3, column=3)

        lblref = Label(DataframeLeft,font=("arial", 12, "bold"), text="Patient Name:", padx=2)
        lblref.grid(row=4, column=2, sticky=w)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=4, column=3)

        lblref = Label(DataframeLeft,font=("arial", 12, "bold"), text="Date of Birth:", padx=2)
        lblref.grid(row=5, column=0, sticky=w)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=5, column=1)

        lblref = Label(DataframeLeft,font=("arial", 12, "bold"), text="Patient Address:", padx=2)
        lblref.grid(row=6, column=0, sticky=w)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=6, column=1)

        








root=Tk()
ob=Hospital(root)
root.mainloop()