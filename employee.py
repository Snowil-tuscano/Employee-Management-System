from tkinter import *
class emplyee :
    def __init__(self,root) :
        self.root=root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1350x750")
        self.root.config(bg="white")
        title= Label(self.root,text="Employee Payroll Mnagement System",font=("times new roman",30,"bold"),bg="#ADD8E6",fg="black").place(x=0,y=0,relwidth=1)
        
        # .....................frame1.................
        
        #...........variables....................
        self.var_code= StringVar()
        self.var_desig= StringVar()
        self.var_dob= StringVar()
        self.var_name= StringVar()
        self.var_doj= StringVar()
        self.var_exp= StringVar()
        self.var_age= StringVar()
        self.var_proof= StringVar()
        self.var_gender = StringVar()
        self.var_contact= StringVar()
        self.var_address= StringVar()
        self.var_email= StringVar()
        Frame1 = Frame(self.root,bd=4,relief=RIDGE)
        Frame1.place(x=10,y=60,width=750,height=580)
        Frame1.config(bg="white")
        title2= Label(Frame1,text="Employee Details",font=("times new roman",20,),bg="lightgray",fg="black").place(x=0,y=0,relwidth=1)
        
        
        # ................row1...........
        lbl_code = Label(Frame1,text="Employee code",font=("times new roman",18,),bg="white",fg="black").place(x=10,y=60)
        txt_code = Entry(Frame1,font=("times new roman",18,),textvariable= self.var_code ,bg="white",fg="black").place(x=200,y=60,width=200)
        lbl_code = Button(Frame1,text="Search",font=("times new roman",14),bg="#f0f0f0",fg="black",relief=SOLID).place(x=420,y=60)



        # ................row2...........
        lbl_Designation = Label(Frame1,text="Designation",font=("times new roman",18,),bg="white",fg="black").place(x=10,y=120)
        txt_Designation = Entry(Frame1,font=("times new roman",18,),textvariable= self.var_desig ,bg="white",fg="black").place(x=200,y=120,width=200)
        
        lbl_dob = Label(Frame1,text="D.O.B",font=("times new roman",18,),bg="white",fg="black").place(x=420,y=120)
        txt_dob = Entry(Frame1,font=("times new roman",18,),textvariable= self.var_dob ,bg="white",fg="black").place(x=510,y=120,width=200)
        
        # ................row3...........
        lbl_name = Label(Frame1, text="Name", font=("times new roman", 18), bg="white", fg="black").place(x=10, y=180)
        txt_name = Entry(Frame1, font=("times new roman", 18), textvariable= self.var_name  , bg="white", fg="black").place(x=200, y=180, width=200)   

        lbl_doj = Label(Frame1, text="D.O.J", font=("times new roman", 18), bg="white", fg="black").place(x=420, y=180)
        txt_doj = Entry(Frame1, font=("times new roman", 18),textvariable= self.var_doj , bg="white", fg="black").place(x=510, y=180, width=200)
        
        # ................row4...........
        lbl_Experience = Label(Frame1, text="Experience", font=("times new roman", 18), bg="white", fg="black").place(x=10, y=240)
        txt_Experience = Entry(Frame1, font=("times new roman", 18), bg="white",textvariable= self.var_exp , fg="black").place(x=200, y=240, width=200)   

        lbl_Age = Label(Frame1, text="Age", font=("times new roman", 18), bg="white", fg="black").place(x=420, y=240)
        txt_Age = Entry(Frame1, font=("times new roman", 18), textvariable= self.var_age ,bg="white", fg="black").place(x=510, y=240, width=200)
        
         # ................row5...........
        lbl_Proof = Label(Frame1, text="Proof  ID", font=("times new roman", 18), bg="white", fg="black").place(x=10, y=300)
        txt_Proof = Entry(Frame1, font=("times new roman", 18),textvariable= self.var_proof , bg="white", fg="black").place(x=200, y=300, width=200)   

        lbl_Gender = Label(Frame1, text="Gender", font=("times new roman", 18), bg="white", fg="black").place(x=420, y=300)
        radio_button1 = Radiobutton(Frame1, text="Male", variable=self.var_gender, value="male", font=("times new roman", 16), bg="white", fg="black")
        radio_button1.place(x=510, y=300)

        
        radio_button2 = Radiobutton(Frame1, text="Female", variable=self.var_gender, value="female", font=("times new roman", 16), bg="white", fg="black")
        radio_button2.place(x=590, y=300)
        
        
          # ................row6...........
        lbl_Email = Label(Frame1, text="Email", font=("times new roman", 18), bg="white", fg="black").place(x=10, y=360)
        txt_Email = Entry(Frame1, font=("times new roman", 18),textvariable= self.var_email , bg="white", fg="black").place(x=200, y=360, width=200)   

        lbl_con = Label(Frame1, text="Contact", font=("times new roman", 18), bg="white", fg="black").place(x=420, y=360)
        txt_con = Entry(Frame1, font=("times new roman", 18),textvariable= self.var_contact, bg="white", fg="black").place(x=510, y=360, width=200)
        # ................row7...........
        lbl_Address = Label(Frame1, text="Address", font=("times new roman", 18), bg="white", fg="black").place(x=10, y=420)
        self.txt_Address = Text(Frame1, font=("times new roman", 18),bg="white", fg="black",height=4, width=42)
        self.txt_Address.place(x=200, y=420 )  


        
        # .....................frame2.................
        #......................variables
        
        self.var_base_pay = StringVar()
        self.var_present = StringVar()
        self.var_medical = StringVar()
        self.var_conv = StringVar()
        self.var_p_f = StringVar()
        self.var_net_sal = StringVar()
        Frame2 = Frame(self.root,bd=4,relief=RIDGE)
        Frame2.place(x=770,y=60,width=490,height=300)
        Frame2.config(bg="white")
        title2= Label(Frame2,text="Employee Salary Details",font=("times new roman",20,),bg="lightgray",fg="black").place(x=0,y=0,relwidth=1)
        
        # .............row1...........
        lbl_Base = Label(Frame2,text="Base Pay",font=("times new roman",18,),bg="white",fg="black").place(x=5,y=60)
        txt_Base = Entry(Frame2,font=("times new roman",18), textvariable=self.var_base_pay   ,bg="white",fg="black").place(x=120,y=60,width=90)
        
        lbl_Present = Label(Frame2,text="Present Days",font=("times new roman",18,),bg="white",fg="black").place(x=230,y=60)
        txt_Present = Entry(Frame2,font=("times new roman",18), textvariable=self.var_present ,bg="white",fg="black").place(x=370,y=60,width=90)
        
       # .............row2...........
        lbl_Medical = Label(Frame2,text="Medical",font=("times new roman",18,),bg="white",fg="black").place(x=5,y=120)
        txt_Medical = Entry(Frame2,font=("times new roman",18), textvariable=self.var_medical ,bg="white",fg="black").place(x=120,y=120,width=90)
        
        lbl_Convinence = Label(Frame2,text="Convinence",font=("times new roman",18,),bg="white",fg="black").place(x=230,y=120)
        txt_Convinence = Entry(Frame2,font=("times new roman",18), textvariable=self.var_conv ,bg="white",fg="black").place(x=370,y=120,width=90)
       
        # .............row3...........
        lbl_PF = Label(Frame2,text="P.F",font=("times new roman",18,),bg="white",fg="black").place(x=5,y=180)
        txt_PF = Entry(Frame2,font=("times new roman",18), textvariable=self.var_p_f ,bg="white",fg="black").place(x=120,y=180,width=90)

        lbl_net = Label(Frame2,text="Net Salary",font=("times new roman",18,),bg="white",fg="black").place(x=230,y=180)
        txt_net = Entry(Frame2,font=("times new roman",18), textvariable=self.var_net_sal,bg="white",fg="black").place(x=370,y=180,width=90)
        
        # ..............adding buttons ..............
   
        btn_Calculate = Button(Frame2,text="Calculate",font=("times new roman",14),command= self.calculate, bg="#f0f0f0",fg="black",relief=SOLID).place(x=180,y=240)
        btn_Save = Button(Frame2,text="Save",font=("times new roman",14),bg="#f0f0f0",fg="black",relief=SOLID,).place(x=280,y=240)
        btn_clear = Button(Frame2,text="Clear",font=("times new roman",14),bg="#f0f0f0",fg="black",relief=SOLID).place(x=350,y=240)
         # lbl_code = Button(Frame2,text="Print",font=("times new roman",14),bg="#f0f0f0",fg="black",relief=SOLID).place(x=360,y=240)

       


        
        
        # .....................Frame3.................
        Frame3 = Frame(self.root,bd=4,relief=RIDGE)
        Frame3.place(x=770,y=370,width=490,height=270)
        Frame3.config(bg="white")
        
        
        #.....calculator frame 
        cal_frame =Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        cal_frame.place(x=5,y=5,width=216,height=255)
        
        self.var_txt=StringVar()
        self.var_operator=''
        def btn_click(num):
          self.var_operator+=str(num)
          self.var_txt.set(self.var_operator)
          
          
        def result():
          res=str(eval(self.var_operator))
          self.var_txt.set(res)
          self.var_operator=''
          
        def clr():
          self.var_operator=''
          self.var_txt.set(self.var_operator)

        title4= Entry(cal_frame,text="Calculator",textvariable=self.var_txt,font=("times new roman",20,),bg="lightgray",fg="black").place(x=0,y=0,relwidth=1)

          
        # .................calculator row 1 ...............
        btn7= Button(cal_frame,text="7",command=lambda:btn_click(7) ,font=("times new roman ",15,"bold")).place(x=2,y=42,width=50,height=40)
        btn8= Button(cal_frame,text="8",command=lambda:btn_click(8),font=("times new roman ",15,"bold")).place(x=55,y=42,width=50,height=40)
        btn9= Button(cal_frame,text="9",command=lambda:btn_click(9),font=("times new roman ",15,"bold")).place(x=108,y=42,width=50,height=40)
        btn_div= Button(cal_frame,text="/",command=lambda:btn_click('/'),font=("times new roman ",15,"bold")).place(x=160,y=42,width=50,height=40)
        
        
        # .................calculator row 2 ...............
        btn4= Button(cal_frame,text="4",command=lambda:btn_click(4),font=("times new roman ",15,"bold")).place(x=2,y=86,width=50,height=40)
        btn5= Button(cal_frame,text="5",command=lambda:btn_click(5), font=("times new roman ",15,"bold")).place(x=55,y=86,width=50,height=40)
        btn6= Button(cal_frame,text="6", command=lambda:btn_click(6), font=("times new roman ",15,"bold")).place(x=108,y=86,width=50,height=40)
        btn_mul= Button(cal_frame,text="*",command=lambda:btn_click('*'), font=("times new roman ",15,"bold")).place(x=160,y=86,width=50,height=40)
        
        
        # # .................calculator row 3 ...............
        btn1= Button(cal_frame,text="1",command=lambda:btn_click(1),font=("times new roman ",15,"bold")).place(x=2,y=130,width=50,height=40)
        btn2= Button(cal_frame,text="2",command=lambda:btn_click(2),font=("times new roman ",15,"bold")).place(x=55,y=130,width=50,height=40)
        btn3= Button(cal_frame,text="3",command=lambda:btn_click(3),font=("times new roman ",15,"bold")).place(x=108,y=130,width=50,height=40)
        btn_plus= Button(cal_frame,text="+",command=lambda:btn_click('+'),font=("times new roman ",15,"bold")).place(x=160,y=130,width=50,height=40)
 
        # # .................calculator row 4 ...............
        btn0= Button(cal_frame,text="0",command=lambda:btn_click(0),font=("times new roman ",15,"bold")).place(x=2,y=174,width=50,height=40)
        btn_neg= Button(cal_frame,text="-",command=lambda:btn_click('-'),font=("times new roman ",15,"bold")).place(x=55,y=174,width=50,height=40)
        btn_dot= Button(cal_frame,text=".",command=lambda:btn_click('.'),font=("times new roman ",15,"bold")).place(x=108,y=174,width=50,height=40)
        btn_equal= Button(cal_frame,text="=",command=lambda:result(),font=("times new roman ",15,"bold")).place(x=160,y=174,width=50,height=40)
        
        
        btn_clr = Button(cal_frame,text="Clear",command=lambda:clr(),font=("times new roman ",15,"bold")).place(x=80,y=215,width=60,height=35)

        sal_frame =Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        sal_frame.place(x=225,y=5,width=253,height=255)   
        title5= Label(sal_frame,text="Salary Slip",font=("times new roman",20,),bg="lightgray",fg="black").place(x=0,y=0,relwidth=1)
 
        sal_frame2 =Frame(sal_frame,bg="white",bd=2,relief=RIDGE)
        sal_frame2.place(x=0,y=32,relwidth=1,height=180)   
        lbl_print = Button(sal_frame,text="Print",font=("times new roman",14),bg="#f0f0f0",fg="black",relief=SOLID,).place(x=100,y=215,width=60,height=35)

        
        scroll_y= Scrollbar(sal_frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)
       
    def calculate(self):
      print( self.var_code.get(),
       self.var_desig.get(),
       self.var_dob.get(),
       self.var_name.get(),
       self.var_doj.get(),
       self.var_exp.get(),
       self.var_age.get(),
       self.var_proof.get(),
       self.var_gender.get(),
        self.var_contact.get(),
        self.var_address.get(),
        self.var_email.get(),
        self.var_base_pay.get(),
        self.var_present.get(),
        self.var_medical.get(),
        self.var_conv.get(),
        self.var_p_f.get(),
        self.var_net_sal.get())    

        
        

        
        
root = Tk()
obj = emplyee(root)
root.mainloop()
        