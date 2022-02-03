#app
import tkinter as tk




def sub_bt(rno,name,mark):
    print("works")
    print(rno)
    print(name)
    print(mark)
    sub_text.set("Loading...")



root = tk.Tk()

root.geometry("700x500")
root.resizable(False,False)
#root.iconbitmap("icon.png")
"""
#canvas
canvas = tk.Canvas(root, width=600, height = 300)
canvas.grid(columnspan=3, rowspan=3)
"""

#background image
#logo = Image.open('image.png')
#logo = ImageTk.PhotoImage(logo)
#logo_label = tk.Label(image=logo)
#logo_label.image = logo
#logo_label.grid(column=1, row=0)

canvas = tk.Canvas(width=400,height=375, bg="#def5ff")
canvas.place(x=150,y=60)

#title
title = tk.Label(text="DBMS", bg="#def5ff", font="Bold 30", fg="#20bebe")
title.place(x=300,y=80)

#reg_no label
reg_no = tk.Label(text="Reg No.: ", bg="#def5ff", font="10")
reg_no.place(x=200,y=150)

#name label
names = tk.Label(text="Name: ", bg="#def5ff", font="10")
names.place(x=200,y=200)

#total marks label
tot_mark = tk.Label(text="Total Marks: ", bg="#def5ff", font="10")
tot_mark.place(x=200,y=250)


#entry widgets
reg_no_in = tk.Text(borderwidth=0,highlightthickness=0,width=22,height=1)
reg_no_in.place(x=320,y=152,width=175,height=25)

name_in = tk.Text(borderwidth=0,highlightthickness=0,width=22,height=1)
name_in.place(x=320,y=202,width=175,height=25)

tot_marks_in = tk.Text(borderwidth=0,highlightthickness=0,width=22,height=1)
tot_marks_in.place(x=320,y=252,width=175,height=25)


#submit button
sub_text = tk.StringVar()
sub_btn = tk.Button(root,command=lambda:sub_bt(), textvariable= sub_text, font="Raleway", bg="#20bebe", fg="white", height=1, width=15)
sub_text.set("Submit")
sub_btn.place(x=270,y=380)

print(reg_no_in)

root.mainloop()