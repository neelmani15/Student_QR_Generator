from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
class QR_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+300+100")
        self.root.title('QR Generator | By Neelmani')
        self.root.resizable(False,False)

        title=Label(self.root,text="UIT Student QRCode Generator",font=("times new roman",40),bg="#3A3B3C",fg='white').place(x=0,y=0,relwidth=1)

        #=========Variable to fetch detials of Student======
        self.var_student_name=StringVar()
        self.var_student_roll=StringVar()
        self.var_student_dept=StringVar()
        self.var_student_year=StringVar()

        #=================Details of UIT Students window======================
        stud_frame=Frame(self.root,bd=2,relief=GROOVE,bg='white')
        stud_frame.place(x=50,y=100,width=500,height=380)

        #===========Adding title to UIT Student Window======
        stud_title=Label(stud_frame,text="UIT Student Details",font=("times new roman",20),bg="#3A3B3C",fg='white').place(x=0,y=0,relwidth=1)

        #============Adding Label in UIT Student Window=====
        label_student_name=Label(stud_frame,text="Student Name",font=("Arial",15,'bold')).place(x=20,y=60)
        label_student_roll=Label(stud_frame,text="Roll Number",font=("Arial",15,'bold')).place(x=20,y=100)
        label_student_dept=Label(stud_frame,text="Department",font=("Arial",15,'bold')).place(x=20,y=140)
        label_student_year=Label(stud_frame,text="Academic Year",font=("Arial",15,'bold')).place(x=20,y=180)

        #==========Adding Entry in UIT Students Window======
        text_student_name=Entry(stud_frame,font=("Arial",15),textvariable=self.var_student_name,bg="#AFEEEE").place(x=220,y=60)
        text_student_roll=Entry(stud_frame,font=("Arial",15),textvariable=self.var_student_roll,bg="#AFEEEE").place(x=220,y=100)
        text_student_dept=Entry(stud_frame,font=("Arial",15),textvariable=self.var_student_dept,bg="#AFEEEE").place(x=220,y=140)
        text_student_year=Entry(stud_frame,font=("Arial",15),textvariable=self.var_student_year,bg="#AFEEEE").place(x=220,y=180)

        #==========Add Button to Generate QR and clear it====
        submit=Button(stud_frame,text="QR Generate",command=self.generate,font=("times now roman",18,'bold'),bg="#0000A0",fg='white').place(x=40,y=240,width=180,height=30)
        clear=Button(stud_frame,text="Clear",command=self.clear,font=("times now roman",18,'bold'),bg="#838996",fg='white').place(x=260,y=240,width=180,height=30)

        self.msg=""
        self.label_msg=Label(stud_frame,text=self.msg,font=("times now roman",20,'bold'),bg='white',fg='green')
        self.label_msg.place(x=0,y=300,relwidth=1)

        #===================Student QR code Window=============================
        qr_Frame=Frame(self.root,bd=2,relief=GROOVE,bg='#F8F8FF')
        qr_Frame.place(x=600,y=100,width=250,height=380)

        #==========Adding title to Student QR code Window======
        qr_title=Label(qr_Frame,text="Student QR Code",font=("times new roman",20),bg="#3A3B3C",fg="white").place(x=0,y=0,relwidth=1)

        self.qr_code=Label(qr_Frame,text="No Qr \nAvailable",font=("times new roman",15),bg='#3A3B3C',fg='white',bd=1,relief=GROOVE)
        self.qr_code.place(x=35,y=100,width=180,height=180)
    def clear(self):
        self.var_student_name.set("")
        self.var_student_roll.set("")
        self.var_student_dept.set("")
        self.var_student_year.set("")
        self.msg = ''
        self.label_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate(self):
        if self.var_student_name.get()=='' or self.var_student_roll.get()=='' or self.var_student_dept.get()=='' or self.var_student_year.get()=='':
            self.msg='All Fields are Required!!!'
            self.label_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Student Name: {self.var_student_name.get()}\nRoll number: {self.var_student_roll.get()}\nDepartment: {self.var_student_dept.get()}\nAcademic Year: {self.var_student_year.get()}")
            qr_code=qrcode.make(qr_data)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("Student_QR/"+str(self.var_student_roll.get())+'.png')
            #========QR Code Image Update========
            self.img=ImageTk.PhotoImage(file="Student_QR/"+str(self.var_student_roll.get())+'.png')
            self.qr_code.config(image=self.img)
            #========Upading Notification========
            self.msg='QR Generated Successfully!!!'
            self.label_msg.config(text=self.msg,fg='green')

root = Tk()
ob = QR_Generator(root)
root.mainloop()