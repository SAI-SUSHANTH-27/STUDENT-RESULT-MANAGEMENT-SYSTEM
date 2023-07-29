from tkinter import *#here we imported tkinter library
from PIL import Image,ImageTk #here we installed pillow(pip install pillow)
from tkinter import ttk,messagebox
import sqlite3
class SubjectClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student result management system")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #this is the title.......

        title=Label(self.root,text="Manage Subject Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=35)
        
        #variables.......

        self.var_subject=StringVar()
        self.var_duration=StringVar()
        self.var_faculty=StringVar()
        
        #widgets..............

        lbl_subject_name=Label(self.root,text="Subject Name",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=60)
        lbl_subject_duration=Label(self.root,text="Duration",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=100)
        lbl_subject_faculty=Label(self.root,text="Faculty",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=140)
        lbl_subject_description=Label(self.root,text="Description",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=180)
       
        #entry fields............

        self.txt_subject_name=Entry(self.root,textvariable=self.var_subject,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_subject_name.place(x=150,y=60,width=200)
        txt_subject_duration=Entry(self.root,textvariable=self.var_duration,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=150,y=100,width=200)
        txt_subject_faculty=Entry(self.root,textvariable=self.var_faculty,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=150,y=140,width=200)
        self.txt_subject_description=Text(self.root,font=("goudy old style",15,'bold'),bg='lightyellow')
        self.txt_subject_description.place(x=150,y=180,width=500,height=130)

        #buttons.............

        self.btn_add=Button(self.root,text='Save',font=("goudy old style",15,'bold'),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_add=Button(self.root,text='Update',font=("goudy old style",15,'bold'),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_add.place(x=270,y=400,width=110,height=40)
        self.btn_add=Button(self.root,text='Delete',font=("goudy old style",15,'bold'),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_add.place(x=390,y=400,width=110,height=40)
        self.btn_add=Button(self.root,text='Clear',font=("goudy old style",15,'bold'),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_add.place(x=510,y=400,width=110,height=40)

        #search panel...................

        self.var_search=StringVar()
        lbl_search_subjectName=Label(self.root,text="Subject Name",font=("goudy old style",15,'bold'),bg='white').place(x=720,y=60)
        txt_Search_subjectName=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=870,y=60,width=180)
        btn_search=Button(self.root,text='Search',font=("goudy old style",15,'bold'),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height=28)
        
        #content....................

        self.S_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.S_Frame.place(x=720,y=100,width=470,height=340)


        scrolly=Scrollbar(self.S_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.S_Frame,orient=HORIZONTAL)
        self.SubjectTable=ttk.Treeview(self.S_Frame,columns=("sid","name","duration","faculty","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.SubjectTable.xview)
        scrolly.config(command=self.SubjectTable.yview)

        self.SubjectTable.heading("sid",text="Subject ID")
        self.SubjectTable.heading("name",text="Name")
        self.SubjectTable.heading("duration",text="Duration")
        self.SubjectTable.heading("faculty",text="Faculty")
        self.SubjectTable.heading("description",text="Description")
        self.SubjectTable["show"]='headings'
        self.SubjectTable.column("sid",width=100)
        self.SubjectTable.column("name",width=100)
        self.SubjectTable.column("duration",width=100)
        self.SubjectTable.column("faculty",width=100)
        self.SubjectTable.column("description",width=150)
        self.SubjectTable.pack(fill=BOTH,expand=1)
        self.SubjectTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

#=======================================================================================================

    def clear(self):
        self.show()
        self.var_subject.set("")
        self.var_duration.set("")
        self.var_faculty.set("")
        self.var_search.set("")
        self.txt_subject_description.delete("1.0",END)
        self.txt_subject_name.config(state=NORMAL)
        

    def delete(self):
        con=sqlite3.connect(database="SRMS.db")
        cur=con.cursor()
        try:
            if self.var_subject.get()=="":
                messagebox.showerror("ERROR","SUBJECT NAME SHOULD BE REQUIRED",parent=self.root)
            else:
                cur.execute("select * from subject where name =?",(self.var_subject.get(),))
                row=cur.fetchone()
                if row ==None:
                    messagebox.showerror("ERROR","PLEASE SELECT SUBJECT FROM THE LIST FIRST",parent=self.root)
                else:
                    op=messagebox.askyesno("CONFIRM","DO YOU REALLY WANT TO DELETE?",parent=self.root)
                    if op==True:
                        cur.execute("delete from subject where name=?",(self.var_subject.get(),))
                        con.commit()
                        messagebox.showinfo("DELETE","SUBJECT DELETED SUCCESSFULLY",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("ERROR",f"ERROR DUE TO {str(ex)}")


    def get_data(self,ev):
        self.txt_subject_name.config(state='readonly')
        self.txt_subject_name
        r=self.SubjectTable.focus()
        content=self.SubjectTable.item(r)
        row=content["values"]
        #print(row)
        self.var_subject.set(row[1])
        self.var_duration.set(row[2])
        self.var_faculty.set(row[3])
        #self.var_subject.set(row[4])
        self.txt_subject_description.delete("1.0",END)
        self.txt_subject_description.insert(END,row[4])


    def add(self):
        con=sqlite3.connect(database="SRMS.db")
        cur=con.cursor()
        try:
            if self.var_subject.get()=="":
                messagebox.showerror("ERROR","SUBJECT NAME SHOULD BE REQUIRED",parent=self.root)
            else:
                cur.execute("select * from subject where name =?",(self.var_subject.get(),))
                row=cur.fetchone()
                if row !=None:
                    messagebox.showerror("ERROR","SUBJECT NAME ALREADY PRESENT",parent=self.root)
                else:
                    cur.execute("insert into subject (name,duration,faculty,description) values(?,?,?,?)",(
                        self.var_subject.get(),
                        self.var_duration.get(),
                        self.var_faculty.get(),
                        self.txt_subject_description.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("SUCCESS","SUBJECT ADDED SUCCESSFULLY",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("ERROR",f"ERROR DUE TO {str(ex)}")


    def update(self):
        con=sqlite3.connect(database="SRMS.db")
        cur=con.cursor()
        try:
            if self.var_subject.get()=="":
                messagebox.showerror("ERROR","SUBJECT NAME SHOULD BE REQUIRED",parent=self.root)
            else:
                cur.execute("select * from subject where name =?",(self.var_subject.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("ERROR","SELECT SUBJECT FROM LIST",parent=self.root)
                else:
                    cur.execute("update subject set duration=?,faculty=?,description=? where name=?",(
                        self.var_duration.get(),
                        self.var_faculty.get(),
                        self.txt_subject_description.get("1.0",END),
                        self.var_subject.get()
                    ))
                    con.commit()
                    messagebox.showinfo("SUCCESS","SUBJECT UPDATED SUCCESSFULLY",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("ERROR",f"ERROR DUE TO {str(ex)}")
    

    def show(self):
        con=sqlite3.connect(database="SRMS.db")
        cur=con.cursor()
        try:
            cur.execute("select * from subject ")
            rows=cur.fetchall()
            self.SubjectTable.delete(*self.SubjectTable.get_children())
            for row in rows:
                self.SubjectTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("ERROR",f"ERROR DUE TO {str(ex)}")


    def search(self):
        con=sqlite3.connect(database="SRMS.db")
        cur=con.cursor()
        try:
            cur.execute(f"select * from subject where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.SubjectTable.delete(*self.SubjectTable.get_children())
            for row in rows:
                self.SubjectTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("ERROR",f"ERROR DUE TO {str(ex)}")
    

if __name__=="__main__":
    root=Tk()
    obj=SubjectClass(root)
    root.mainloop()