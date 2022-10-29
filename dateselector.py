from tkinter import *
from tkcalendar import Calendar

# creating an object of tkinter

tkobj = Tk()

# setting up the geomentry

tkobj.geometry("400x400")
tkobj.title("Calendar picker")
#creating a calender object

tkc = Calendar(tkobj,selectmode = "day",year=2022,month=10,date=1)

#display on main window
tkc.pack(pady=40)
print(type(tkc.get_date()))

# getting date from the calendar 

def fetch_date():
    date.config(text = "Selected Date is: " + tkc.get_date())

#add button to load the date clicked on calendar

but = Button(tkobj,text="Select Date",command=fetch_date, bg="black", fg='white')
#displaying button on the main display
but.pack()
#Label for showing date on main display
date = Label(tkobj,text="",bg='black',fg='white')
date.pack(pady=20)
#starting the object
tkobj.mainloop()