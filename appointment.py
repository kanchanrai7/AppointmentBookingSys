import tkinter as tk
import smtplib
def automatic_email():
    date=date_menu.get()
    day=day_menu.get()
    month=month_menu.get()
    time_=times.get()
    user = e1.get()
    email =e2.get()
    message = (f"Dear {user}  Your appointment has been successfully booked on {day} {date}  {day} at {time_} \n See you there!\n For any query contact: 7651881382\n Thank you!!\n Please Do not reply it is an autogenerated email")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("your gmail", "your google app password")
    s.sendmail("&&&&&&&&&&&",email,message)
    print("Appointment Confirmed!!")
  
win=tk.Tk()
win.geometry("500x300")
win.title("Appointment Booking System")
win.configure(bg="azure")
l=tk.Label(win,text="Welcome")

l.grid(row=1,column=15)
l1=tk.Label(win,text="Enter your Name")
e1=tk.Entry(win)
l1.grid(row=3,column=5)
e1.grid(row=3,column=8)
l2=tk.Label(win,text="Enter Email")
e2=tk.Entry(win)
l2.grid(row=5,column=5)
e2.grid(row=5,column=8)

month_menu=tk.StringVar()
month_menu.set("Month")
drop1=tk.OptionMenu(win,month_menu,"Jan","Feb","March","April","May","June","July","Aug","Sep","Oct","Nov","Dec")
drop1.place(x=90,y=70)

l3=tk.Label(win,text="Select Date")
l3.place(x=5,y=70)
date_menu=tk.StringVar()
date_menu.set("Date")
drop2=tk.OptionMenu(win,date_menu,"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29")
drop2.place(x=180,y=70)
day_menu=tk.StringVar()
day_menu.set("Day")


times=tk.StringVar()
r1=tk.Radiobutton(win,text="10 AM",value="10 AM",variable=times)
r2=tk.Radiobutton(win,text="12 PM",value="12 PM",variable=times)
r3=tk.Radiobutton(win,text="3 PM",value="3 PM",variable=times)
r4=tk.Radiobutton(win,text="5 PM",value="5 PM",variable=times)

r1.place(x=80,y=130)
r2.place(x=140,y=130)
r3.place(x=200,y=130)
r4.place(x=260,y=130)
button=tk.Button(text="Submit",command=automatic_email,width="30")
button.place(x=90,y=170)

  
 
