from tkinter import *#here we imported tkinter library
from PIL import Image,ImageTk #here we installed pillow(pip install pillow)
from subject import SubjectClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
from datetime import *
import time
import os
from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import *
from tkinter import messagebox
import pymysql
from tkinter import messagebox,ttk
import sqlite3
import os

class SRMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student result management system")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        
        #icons are here..........
        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")
        
        #this is the title.......
        title=Label(self.root,text="Student result management system",image=self.logo_dash,padx=10,compound=LEFT,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        
        #menu...................
        M_frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_frame.place(x=10,y=70,width=1340,height=80)


        btn_Subject=Button(M_frame,text="Subject",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_subject).place(x=20,y=5,width=200,height=40)
        btn_Student=Button(M_frame,text="Students",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_Result=Button(M_frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_view=Button(M_frame,text="view result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
        btn_Logout=Button(M_frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=900,y=5,width=200,height=40)
        btn_Exit=Button(M_frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_).place(x=1120,y=5,width=200,height=40)
        
        #content_window...........
        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)

        #update_details............
        self.lbl_subjects=Label(self.root,text="Total subjects\n[0]",font=("goudy old syle",20),bd=10,relief=RAISED,bg="#e43b06",fg="white")
        self.lbl_subjects.place(x=400,y=530,width=300,height=100)
        self.lbl_students=Label(self.root,text="Total students\n[0]",font=("goudy old syle",20),bd=10,relief=RAISED,bg="#0676ad",fg="white")
        self.lbl_students.place(x=710,y=530,width=300,height=100)
        self.lbl_result=Label(self.root,text="Total results\n[0]",font=("goudy old syle",20),bd=10,relief=RAISED,bg="#038074",fg="white")
        self.lbl_result.place(x=1020,y=530,width=300,height=100)

        #clock
        self.lbl=Label(self.root,text="CLOCK",font=("Book Antiqua","25","bold"),fg='white',compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=10,y=180,height=450,width=350)

        #self.clock_image()
        self.working()

        #this is the footer.........
        footer=Label(self.root,text="SRMS-Student result management system\nContact us for any issues:1234567",font=("goudy old style",12,),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        self.update_details()

#=============================================================
    def update_details(self):
        con=sqlite3.connect(database="SRMS.db")
        cur=con.cursor()
        try:
            cur.execute("select * from subject")
            cr=cur.fetchall()
            self.lbl_subjects.config(text=f"Total Subjects\n[{str(len(cr))}]")

            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_students.config(text=f"Total Students\n[{str(len(cr))}]")

            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")


            self.lbl_subjects.after(200,self.update_details)
        except Exception as ex:
            messagebox.showerror("ERROR",f"ERROR DUE TO {str(ex)}")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        #for clock image
        bg=Image.open("images/c.png")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        
        #hour line image
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
       
        #min line image
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)
       
        #sec line image
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)
        draw.ellipse((195,195,210,210),fill="#1AD5D5")
        clock.save("images/clock_new.png")

    def add_subject(self):
        self.new_win=Toplevel(self.root)   
        self.new_obj=SubjectClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)   
        self.new_obj=studentClass(self.new_win)
    
    def add_result(self):
        self.new_win=Toplevel(self.root)   
        self.new_obj=resultClass(self.new_win)
       
    def add_report(self):
        self.new_win=Toplevel(self.root)   
        self.new_obj=reportClass(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logOut ?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")

    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to Exit ?",parent=self.root)
        if op==True:
            self.root.destroy()
            
    
if __name__=="__main__":
    root=Tk()
    obj=SRMS(root)
    root.mainloop()