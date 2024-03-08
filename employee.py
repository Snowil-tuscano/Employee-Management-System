from tkinter import *
class emplyee :
    def __init__(self,root) :
        self.root=root
        self.root.title("Employee Payroll Mnagement System")
        self.root.geometry("1350x750")
        self.root.config(bg="white")
        title= Label(self.root,text="Employee Payroll Mnagement System",font=("times new roman",30,"bold"),bg="#ADD8E6",fg="black").place(x=0,y=0,relwidth=1)
        Frame1 = Frame(self.root,bd=6,relief=RIDGE)
        Frame1.place(x=10,y=60,width=750,height=580)
        Frame2 = Frame(self.root,bd=6,relief=RIDGE)
        Frame2.place(x=770,y=60,width=490,height=300)
        
root = Tk()
obj = emplyee(root)
root.mainloop()
        