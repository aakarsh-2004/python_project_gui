from tkinter import *
import random
import math
import mysql.connector


root = Tk()

root.configure(bg = '#F4E5EE')

mycon = mysql.connector.connect(host = "localhost", user = "root", passwd = "toor", database = "touristmanagement",)
c = mycon.cursor()
if mycon.is_connected():
    print("Connection successfully established!")
else:
    print("Not Connected!")
def button():
    c.execute("SELECT * From TripInformation")
    data = c.fetchall()
    lbl = Label(root, text = data)
    lbl.grid(row = '0', column = '1')
    for row in data:
        print(row)
            

def test():
    inpt_pr = inpt.get()
    print(inpt_pr)
    inpt.delete(0, END)
inpt = Entry(root)
inpt_1 = Entry(root)
inpt_2 = Entry(root)
inpt_3 = Entry(root)
inpt_4 = Entry(root)
inpt_5 = Entry(root)

#lbl_t = Text(root)

#lbl_t.insert(INSERT, "WELCOME")

lbl_t = Label(root, text = 'WELCOME', font = ('Bahnschrift SemiBold Condensed', 35), bg = '#F4E5EE' )

lbl_t.grid(row = '0', column = '1', ipadx= 50, ipady = 12, padx = 20, pady = 20)

inpt.grid(row = '1', column = '2', ipadx= 100, ipady = 8, padx = 20, pady = 20)
inpt_1.grid(row = '2', column = '2', ipadx= 100, ipady = 8, padx = 20, pady = 20)
inpt_2.grid(row = '3', column = '2', ipadx= 100, ipady = 8, padx = 20, pady = 20)
inpt_3.grid(row = '4', column = '2', ipadx= 100, ipady = 8, padx = 20, pady = 20)
inpt_4.grid(row = '5', column = '2', ipadx= 100, ipady = 8, padx = 20, pady = 20)
inpt_5.grid(row = '5', column = '2', ipadx= 100, ipady = 8, padx = 20, pady = 20)

test_btn = Button(root, text = "Submit!", command = test, padx = 10, pady = 10, bg = 'black', fg = 'white')
test_btn.grid(row = '6', column = '2', ipadx = 100)

btn_show = Button(root, text= "Click here to get database! ", padx = 30, pady = 30, command= button, bg = 'black', fg = 'white')
btn_show.grid(row = '7', column = '2', ipadx= 100)


root.mainloop()
