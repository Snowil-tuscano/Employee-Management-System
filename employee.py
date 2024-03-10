from tkinter import *
class emplyee :
    def __init__(self,root) :
        self.root=root
        self.root.title("Employee Payroll Mnagement System")
        self.root.geometry("1350x750")
        self.root.config(bg="white")
        title= Label(self.root,text="Employee Payroll Mnagement System",font=("times new roman",30,"bold"),bg="#ADD8E6",fg="black").place(x=0,y=0,relwidth=1)
        
        # .....................frame1.................
        Frame1 = Frame(self.root,bd=4,relief=RIDGE)
        Frame1.place(x=10,y=60,width=750,height=580)
        Frame1.config(bg="white")
        title2= Label(Frame1,text="Employee Details",font=("times new roman",20,),bg="lightgray",fg="black").place(x=0,y=0,relwidth=1)
        
        
        # ................row1...........
        lbl_code = Label(Frame1,text="Employee code",font=("times new roman",18,),bg="white",fg="black").place(x=10,y=60)
        txt_code = Entry(Frame1,font=("times new roman",18,),bg="white",fg="black").place(x=200,y=60,width=200)
        lbl_code = Button(Frame1,text="Search",font=("times new roman",14),bg="white",fg="black",relief=RAISED).place(x=420,y=60)



        # ................row2...........
        lbl_Designation = Label(Frame1,text="Designation",font=("times new roman",18,),bg="white",fg="black").place(x=10,y=120)
        txt_Designation = Entry(Frame1,font=("times new roman",18,),bg="white",fg="black").place(x=200,y=120,width=200)
        
        lbl_dob = Label(Frame1,text="D.O.B",font=("times new roman",18,),bg="white",fg="black").place(x=420,y=120)
        txt_dob = Entry(Frame1,font=("times new roman",18,),bg="white",fg="black").place(x=510,y=120,width=200)
        
        # ................row3...........
        lbl_name = Label(Frame1, text="Name", font=("times new roman", 18), bg="white", fg="black").place(x=10, y=180)
        txt_name = Entry(Frame1, font=("times new roman", 18), bg="white", fg="black").place(x=200, y=180, width=200)   

        lbl_doj = Label(Frame1, text="D.O.J", font=("times new roman", 18), bg="white", fg="black").place(x=420, y=180)
        txt_doj = Entry(Frame1, font=("times new roman", 18), bg="white", fg="black").place(x=510, y=180, width=200)
        
        # ................row4...........
        lbl_Experience = Label(Frame1, text="Experience", font=("times new roman", 18), bg="white", fg="black").place(x=10, y=240)
        txt_Experience = Entry(Frame1, font=("times new roman", 18), bg="white", fg="black").place(x=200, y=240, width=200)   

        lbl_Age = Label(Frame1, text="Age", font=("times new roman", 18), bg="white", fg="black").place(x=420, y=240)
        txt_Age = Entry(Frame1, font=("times new roman", 18), bg="white", fg="black").place(x=510, y=240, width=200)
        
         # ................row5...........
        lbl_Proof = Label(Frame1, text="Proof  ID", font=("times new roman", 18), bg="white", fg="black").place(x=10, y=300)
        txt_Proof = Entry(Frame1, font=("times new roman", 18), bg="white", fg="black").place(x=200, y=300, width=200)   

        lbl_Gender = Label(Frame1, text="Gender", font=("times new roman", 18), bg="white", fg="black").place(x=420, y=300)
        radio_var = StringVar()
        radio_button1 = Radiobutton(Frame1, text="Male", variable=radio_var, value="Male", font=("times new roman", 16), bg="white", fg="black")
        radio_button1.place(x=510, y=300)

        
        radio_button2 = Radiobutton(Frame1, text="Female", variable=radio_var, value="Female"  ,font=("times new roman", 16), bg="white", fg="black")
        radio_button2.place(x=590, y=300)
        
        
          # ................row6...........
        lbl_Email = Label(Frame1, text="Email", font=("times new roman", 18), bg="white", fg="black").place(x=10, y=360)
        txt_Email = Entry(Frame1, font=("times new roman", 18), bg="white", fg="black").place(x=200, y=360, width=200)   

        lbl_con = Label(Frame1, text="Contact", font=("times new roman", 18), bg="white", fg="black").place(x=420, y=360)
        txt_con = Entry(Frame1, font=("times new roman", 18), bg="white", fg="black").place(x=510, y=360, width=200)
        # ................row7...........
        lbl_designation2 = Label(Frame1, text="Address", font=("times new roman", 18), bg="white", fg="black").place(x=10, y=420)
        txt_code3 = Text(Frame1, font=("times new roman", 18), bg="white", fg="black",height=4, width=42).place(x=200, y=420, )  


        
        # .....................frame2.................
        Frame2 = Frame(self.root,bd=4,relief=RIDGE)
        Frame2.place(x=770,y=60,width=490,height=300)
        
        
        # .....................Frame3.................
        Frame3 = Frame(self.root,bd=4,relief=RIDGE)
        Frame3.place(x=770,y=370,width=490,height=270)
        
root = Tk()
obj = emplyee(root)
root.mainloop()
        