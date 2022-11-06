from tkinter import *
import random
import math
import mysql.connector


root = Tk()

root.configure(bg = '#9BE2C4')
root.geometry("1255x944")

mycon = mysql.connector.connect(host = "localhost", user = "root", passwd = "toor", database = "touristmanagement",)
c = mycon.cursor()
if mycon.is_connected():
    print("Connection successfully established!")
else:
    print("Not Connected!")
def button():
    c.execute("SELECT * From TripInformation")
    records = c.fetchall()
    print(records)
    print_records = ''
    for record in records:
        print_records += str(record)+ "\n"
    query_label = Label(root, text = print_records, padx = 10, pady = 10, font = ('Bahnschrift SemiBold Condensed', 14),bg = '#9BE2C4')            
    query_label.grid(row = '2', column = '3')
def test():
    inpt_pr = str(inpt.get())
    inpt_pr_1 = inpt_1.get()
    inpt_pr_2 = str(inpt_2.get())
    inpt_pr_3 = inpt_3.get()
    inpt_pr_4 = str(inpt_4.get())
    inpt_pr_5 = str(inpt_5.get())
    print(inpt_pr)
    print(inpt_pr_1)
    print(inpt_pr_2)
    print(inpt_pr_3)
    print(inpt_pr_4)
    print(inpt_pr_5)
    inpt.delete(0, END)
    inpt_1.delete(0, END)
    inpt_2.delete(0, END)
    inpt_3.delete(0, END)
    inpt_4.delete(0, END)
    inpt_5.delete(0, END)
    st = "INSERT INTO tripinformation(Places, Package, Hotels, Numberofpeople, Tripduration, Transportation) VALUES('{}', {}, '{}', {}, '{}', '{}')".format(inpt_pr, inpt_pr_1, inpt_pr_2, inpt_pr_3, inpt_pr_4, inpt_pr_5)
    c.execute(st)
    mycon.commit()

def delete():
    del_inp = inpt_del.get()
    print(del_inp)
    inpt_del.delete(0, END)
    query = "DELETE FROM tripinformation WHERE Places = %s" 
    value = (del_inp,)
    c.execute(query, value)
    mycon.commit()


inpt = Entry(root)
inpt.insert(0, "Enter name of Place ")
inpt_1 = Entry(root)
inpt_1.insert(0, "Enter Package ")
inpt_2 = Entry(root)
inpt_2.insert(0, "Enter hotel's star ")
inpt_3 = Entry(root)
inpt_3.insert(0, "Enter number of people ")
inpt_4 = Entry(root)
inpt_4.insert(0, "Enter Trip duration ")
inpt_5 = Entry(root)
inpt_5.insert(0, "Enter Flight name ")


#lbl_t = Text(root)

#lbl_t.insert(INSERT, "WELCOME")

#lbl_t = Label(root, text = 'WELCOME', font = ('Bahnschrift SemiBold Condensed', 35), bg = '#F4E5EE' )

#lbl_t.grid(row = '0', column = '1', ipadx= 50, ipady = 12, padx = 10, pady = 10)

lbl_h = Label(root, text = 'Add onto the database:', font = ('Bahnschrift SemiBold Condensed', 24), bg = '#9BE2C4' )

lbl_h.grid(row = '0', column = '2')

inpt.grid(row = '1', column = '2', ipadx= 100, ipady = 8, padx = 10, pady = 10)
inpt_1.grid(row = '2', column = '2', ipadx= 100, ipady = 8, padx = 10, pady = 10)
inpt_2.grid(row = '3', column = '2', ipadx= 100, ipady = 8, padx = 10, pady = 10)
inpt_3.grid(row = '4', column = '2', ipadx= 100, ipady = 8, padx = 10, pady = 10)
inpt_4.grid(row = '5', column = '2', ipadx= 100, ipady = 8, padx = 10, pady = 10)
inpt_5.grid(row = '6', column = '2', ipadx= 100, ipady = 8, padx = 10, pady = 10)

test_btn = Button(root, text = "Submit!",font = ('Bahnschrift SemiBold Condensed', 15), command = test, padx = 10, pady = 10, bg = '#181818', fg = 'white')
test_btn.grid(row = '7', column = '2', ipadx = 100)

btn_show = Button(root, text= "Click here to get database! ",font = ('Bahnschrift SemiBold Condensed', 15), padx = 30, pady = 30, command= button, bg = '#181818', fg = 'white')
btn_show.grid(row = '1', column = '3', ipadx= 40)



lbl_d = Label(root, text = 'Delete the data of a Place:', font = ('Bahnschrift SemiBold Condensed', 25), bg = '#9BE2C4',padx = 30, pady = 30)
lbl_d.grid(row = '9', column = '2')

inpt_del = Entry(root)

inpt_del.grid(row = '10', column = '2', ipadx= 100, ipady = 8, padx = 5, pady = 5)
#inpt_del.insert(0, 'Enter the place that you want to delete ')

del_inp = inpt_del.get()
#empt_str = ''
#empt_str+=del_inp



btn_del = Button(root, text = "DONE!",font = ('Bahnschrift SemiBold Condensed', 15), command = delete, padx = 10, pady = 10, bg = '#181818', fg = 'white')
btn_del.grid(row = '11', column = '2', ipadx= 20, ipady = 6, padx = 5, pady = 5)

root.mainloop()
