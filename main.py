from tkinter import *
import random
import math
import mysql.connector


root = Tk()

root.title('Tourist Management System')
root.configure(bg = '#9BE2C4')
root.geometry("1255x944")
# p1 = PhotoImage(file = 'icon.png')
# root.iconphoto(False, p1)


mycon1 = mysql.connector.connect(host = "localhost", user = "root", passwd = "toor")

c1 = mycon1.cursor()

c1.execute("DROP DATABASE IF EXISTS touristmanagement")
c1.execute("CREATE DATABASE touristmanagement;")
c1.execute("USE touristmanagement")
c1.execute("create table TripInformation(Places varchar(30),Package integer,Hotels varchar(30),Numberofpeople integer,Tripduration varchar(30),Transportation varchar(30));")
c1.execute("insert into TripInformation values('Bangkok',90000,'5star',4,'FivenightsFourdays','flightspicejet');")
c1.execute("insert into TripInformation values('Hawaii',200000,'4star',4,'FivenightsFourdays','flightAirindia');")
c1.execute("insert into TripInformation values('Italy',150000,'3star',4,'FivenightsFourdays','flightAirindia');")
c1.execute("insert into TripInformation values('Goa',30000,'3star',4,'FivenightsFourdays','flightspicejet');")
c1.execute("insert into TripInformation values('bhutan',15000,'3star',4,'FivenightsFourdays','flightspicejet');")
c1.execute("insert into TripInformation values('SriLanka',85000,'3star',4,'FivenightsFourdays','flightspicejet');")
c1.execute("insert into TripInformation values('SouthAfrica',200000,'4star',4,'FivenightsFourdays','flightAirindia');")
c1.execute("insert into TripInformation values('Maldives',65000,'4star',4,'FivenightsFourdays','flightAirindia');")
c1.execute("insert into TripInformation values('Manali',20000,'3star',4,'FivenightsFourdays','flightAirindia');")
c1.execute("insert into TripInformation values('Kashmir',15000,'3star',4,'FivenightsFourdays','flightAirindia');")


mycon1.commit()



mycon = mysql.connector.connect(host = "localhost", user = "root", passwd = "toor", database = "touristmanagement")

c = mycon.cursor()



if mycon.is_connected():
    print("Connection successfully established!")
else:
    print("Not Connected!")

def show_less():
    query_label.destroy()
    btn.destroy()
    
def button():
    c.execute("SELECT * From TripInformation")
    records = c.fetchall()
    print(records)
    print_records = ''
    for record in records:
        print_records += str(record)+ "\n"
    global query_label
    query_label = Label(root, text = print_records, padx = 10, pady = 10, font = ('Bahnschrift SemiBold Condensed', 14),bg = '#9BE2C4')            
    query_label.grid(row = '2', column = '3')
    global btn
    btn = Button(root, text = 'Show Less',font = ('Bahnschrift SemiBold Condensed', 15), command = show_less, padx = 10, pady = 10, bg = '#181818', fg = 'white')
    btn.grid(row = '3', column = '3')
    
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

def clear():
    morebtn_lbl.destroy()
    morebtn_clear.destroy()

def morebtn():
    more_inpt = more_info.get()
    print(more_inpt)
    more_info.delete(0, END)
    query = "select * from tripinformation where Places = %s"
    value = (more_inpt,)
    c.execute(query, value)
    morebtn_data = c.fetchall()
    global morebtn_lbl
    morebtn_lbl = Label(root, text = morebtn_data,font = ('Bahnschrift SemiBold Condensed', 15), padx = 10, pady = 10, bg = '#9BE2C4', fg = 'black')
    morebtn_lbl.grid(row = '7', column = '3')
    global morebtn_clear
    morebtn_clear = Button(root, text = 'Clear', command = clear, font = ('Bahnschrift SemiBold Condensed', 15), padx = 5, pady = 5, bg = '#181818', fg = 'white')
    morebtn_clear.grid(row = '8', column = '3')


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
inpt_del.insert(0, 'Place that you want to remove')
inpt_del.grid(row = '10', column = '2', ipadx= 100, ipady = 8, padx = 5, pady = 5)
#inpt_del.insert(0, 'Enter the place that you want to delete ')

del_inp = inpt_del.get()
#empt_str = ''
#empt_str+=del_inp



btn_del = Button(root, text = "DONE!",font = ('Bahnschrift SemiBold Condensed', 15), command = delete, padx = 10, pady = 10, bg = '#181818', fg = 'white')
btn_del.grid(row = '11', column = '2', ipadx= 20, ipady = 6, padx = 5, pady = 5)

head_lbl = Label(root, text = 'Search Database!',font = ('Bahnschrift SemiBold Condensed', 24), bg = '#9BE2C4' )
head_lbl.grid(row = '4', column = '3')

more_info = Entry(root)
more_info.insert(0,'Enter what you want to search')
more_info.grid(row = '5', column = '3', ipadx= 100, ipady = 8, padx = 10, pady = 10)

more_btn = Button(root,text= "Search! ", command = morebtn,font = ('Bahnschrift SemiBold Condensed', 15), padx = 10, pady = 10, bg = '#181818', fg = 'white' )
more_btn.grid(row = '6', column = '3')

root.mainloop()
