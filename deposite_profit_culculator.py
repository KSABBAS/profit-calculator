from tkinter import * #importing the tkinter library 

deposite= Tk() #making the main window
deposite.geometry("350x300")
deposite.resizable(False,False)
deposite.config(background="#e7c27d") #the window color
deposite.iconbitmap(r"alphabet_96900.ico")
deposite.title("de-cl")
N=Entry(deposite,bg="#faf5ef",font=("family","15"),fg="#290916")
N.place(x=20,y=15,width=85)
p=Entry(deposite,bg="#faf5ef",font=("family","15"),fg="#290916")
p.place(x=20,y=50,width=85)
def store():
    benifit=0
    total=0
    num=0
    per= p.get()
    amount= N.get()
    mon=monthes.get()
    amount=float(amount)
    per=float(per)
    mon=float(mon)
    t=0
    while t != mon:
        benifit= amount * (per/100)
        total=num+benifit
        num= total
        t+=1
    
    l22=Label(deposite, text="                                          ",font=("family","14"))
    l22.place(x=145,y=257)
    l12=Label(deposite, text=total,font=("family","14"))
    l12.place(x=145,y=257)
    
def add():
    benifit=0
    
    per= p.get()
    amount= N.get()
    mon=monthes.get()
    amount=float(amount)
    per=float(per)
    mon=float(mon)
    t=1
    while t != mon:
        benifit= amount * (per/100)
        amount=amount+benifit
        t+=1
    l22=Label(deposite, text="                                            ",font=("family","14"))
    l22.place(x=145,y=257)
    l11=Label(deposite, text=amount,font=("family","14"))
    l11.place(x=145,y=257)
ln=Label(deposite,text="enter the amount of money",fg="#290916" ,font=("family","14"),bg="#e7c27d")
ln.place(x=110,y=15)
lp=Label(deposite,text="enter the persetage of the benifit",fg="#290916" ,font=("family","12"),bg="#e7c27d")
lp.place(x=110,y=53)
monthes=Entry(deposite,bg="#faf5ef",width=4,font=("family","10"),justify="center")
monthes.place(x=185,y=95)
lm=Label(deposite,text="monthes",fg="#290916" ,font=("family","12"),bg="#e7c27d")
lm.place(x=115,y=92)
culculation=Frame(deposite,bg="#faf5ef",width=310,height=100)
culculation.place(x=20,y=130)
l1=Label(culculation,text="what are you going to do with the benifit",fg="#290916" ,font=("family","13"),bg="#faf5ef")
l1.place(x=10,y=10)
b1=Button(culculation,text="store it",bg="#e7c27d",fg="#290916",command=store)
b1.place(x=85,y=55,width=60,height=30)
b2=Button(culculation,text="add  it",bg="#e7c27d",fg="#290916",command=add)
b2.place(x=160,y=55,width=60,height=30)
lo=Label(deposite,text="total = ",fg="#290916" ,font=("family","14"),bg="#e7c27d")
lo.place(x=90,y=256)
deposite.mainloop() 