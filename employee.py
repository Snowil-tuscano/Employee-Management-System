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
        lbl_code = Label(Frame1,text="Employee code",font=("times new roman",18,),bg="white",fg="black").place(x=10,y=40)
        lbl_desug = Label(Frame1,text="Designation",font=("times new roman",18,),bg="white",fg="black").place(x=10,y=90)

        
        # .....................frame2.................
        Frame2 = Frame(self.root,bd=4,relief=RIDGE)
        Frame2.place(x=770,y=60,width=490,height=300)
        
        
        # .....................Frame3.................
        Frame3 = Frame(self.root,bd=4,relief=RIDGE)
        Frame3.place(x=770,y=370,width=490,height=270)
        
root = Tk()
obj = emplyee(root)
root.mainloop()
        