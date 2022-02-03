import tkinter as tk


root = tk.Tk()
root.geometry("600x700")
canvas = tk.Canvas(width=600,height=700, bg="#def5ff")
canvas.grid(columnspan=3, rowspan=8)
title=root.title("LOGIN PAGE")
Title=tk.Label(text='SELECT LOGIN',font="BOLD 30",bg="red").grid(row=1,column=1)
did = tk.IntVar()
password1 = tk.StringVar()
hid = tk.IntVar()
password2 = tk.StringVar()
#variables for donor page
name=tk.StringVar()




#Variables for hospital page






#Variables for 
#Submit page
def submit():
    x = did.get()
    y = password1.get()
    root5=tk.Tk()
    root5.geometry('600x700')
    canvas = tk.Canvas(root5,width=600,height=700, bg="#def5ff")
    canvas.place(x=0,y=0)

def submit2():
    x=hid.get()
    y=password2.get()


#DONOR LOGIN PAGE

def donor():
    root2=tk.Tk()
    root2.geometry('600x700')
    canvas = tk.Canvas(root2,width=600,height=700, bg="#def5ff")
    canvas.place(x=0,y=0)
 

    password1.set("")
    did.set("")

    label1 = tk.Label(root2, text="Donor id ",  font= "10",bg="#def5ff").grid(row=2, column=0)
    entry1 = tk.Entry(root2,textvariable= did, width=20,font= "10")
    entry1.grid(row=2,column=1)


    label1 = tk.Label(root2, text="Password ",  font= "10",bg="#def5ff").grid(row=3,column=0)
    entry2 = tk.Entry(root2,textvariable = password1,width=10,font= "10")
    entry2.grid(row=3,column=1)
   
    sub=tk.Button(root2,text="Submit",font="50",command=lambda:[submit()]).grid(row=4,column=0)

    root2.mainloop()

#HOSPITAL LOGIN PAGE 
def hospital():
    root3=tk.Tk()
    root3.geometry('600x700')
    canvas = tk.Canvas(root3,width=600,height=700, bg="#def5ff")
    canvas.place(x=0,y=0)
    did = tk.IntVar()
    password = tk.StringVar()

    password1.set("")
    hid.set("")

    label1 = tk.Label(root3, text="ID ",  font= "10",bg="#def5ff").grid(row=2, column=0)
    entry1 = tk.Entry(root3,textvariable= hid, width=20,font= "10")
    entry1.grid(row=2,column=1)


    label1 = tk.Label(root3, text="Password ",  font= "10",bg="#def5ff").grid(row=3,column=0)
    entry2 = tk.Entry(root3,textvariable = password2,width=10,font= "10")
    entry2.grid(row=3,column=1)
   
    sub=tk.Button(root3,text="Submit",font="50",command=lambda:[submit()]).grid(row=4,column=0)

    root3.mainloop()
#NEW Donor registration details
def new():
    root4=tk.Tk()
    root4.geometry('600x700')
    canvas = tk.Canvas(root4,width=600,height=700, bg="#def5ff")
    canvas.place(x=0,y=0)

    label1 = tk.Label(root4, text="Name ",  font= "10",bg="#def5ff").grid(row=3,column=0)
    entry2 = tk.Entry(root4,textvariable = name,width=10,font= "10")
    

    label1 = tk.Label(root4, text="Password ",  font= "10",bg="#def5ff").grid(row=3,column=0)
    entry2 = tk.Entry(root4,textvariable = password2,width=10,font= "10")
    
#New hospital details

hos= tk.Button(root,text = "Hospital login",font= "50",bg="#def5ff",fg='orange',command= lambda:[hospital()]).grid(row=2,column=1)
don = tk.Button(root, text="Donor login",font= "50", bg="#def5ff",fg='orange',command= lambda:[donor()]).grid(row=3,column=1)

root.mainloop()