from tkinter import *
import time
import ttkthemes
from tkinter import ttk

# FUNCTIONALITY PART
count = 0
text = ''

def slider():
    global text, count
    if count == len(s):
        count = 0
        text = ''
    text = text + s[count]
    sliderLabel.config(text=text)
    count += 1
    sliderLabel.after(300, slider)

def clock():
    date = time.strftime('%d/%m/%Y')  # Date with full year format
    currenttime = time.strftime('%I:%M:%S %p')  # 12-hour format with AM/PM
    datetimeLabel.config(text=f"DATE:{date}\n    TIME:{currenttime}")
    # Call the clock function again after 1000 milliseconds (1 second)
    datetimeLabel.after(1000, clock)

# GUI PART
root = ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

root.geometry('1370x700+0+0')
root.resizable(0, 0)
root.title('Student Management System')

# Label for date and time
datetimeLabel = Label(root, font=('times new roman', 18, 'bold'))
datetimeLabel.place(x=5, y=5)

# Call the clock function to initialize updating the label
clock()

# Text slider for title
s = 'Student Management System'
sliderLabel = Label(root, font=('arial', 28, 'italic bold'), width=30)
sliderLabel.place(x=400, y=0)
slider()

connectButton = ttk.Button(root,text='Connect Database')
connectButton.place(x=1100,y=0)

leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)

logo_image=PhotoImage(file='student (1).png')
logo_Label=Label(leftFrame, image=logo_image)
logo_Label.grid(row=0, column=0)

addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25, state=DISABLED)
addstudentButton.grid(row=1, column=0, pady=20)

searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25, state=DISABLED)
searchstudentButton.grid(row=2, column=0, pady=20)

deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25, state=DISABLED)
deletestudentButton.grid(row=3, column=0, pady=20)

updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25, state=DISABLED)
updatestudentButton.grid(row=4, column=0, pady=20)

showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25, state=DISABLED)
showstudentButton.grid(row=5, column=0, pady=20)

exportstudentButton=ttk.Button(leftFrame,text='Export Data',width=25, state=DISABLED)
exportstudentButton.grid(row=6, column=0, pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25)
exitButton.grid(row=7, column=0, pady=20)

rightFrame = Frame(root,bg='yellow')
rightFrame.place(x=350, y=80, width=1000, height=600)

scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile','Email', 'Address', 'Gender',
                                              'D.O.B', 'Added Date', 'Added Time'),
                          xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)

studentTable.pack(fill=BOTH, expand=1)

studentTable.heading('Id', text='Id')
studentTable.heading('Name', text='Name')
studentTable.heading('Mobile', text='Mobile')
studentTable.heading('Email', text='Email Address')
studentTable.heading('Address', text='Address')
studentTable.heading('Gender', text='Gender')
studentTable.heading('D.O.B', text='D.O.B')
studentTable.heading('Added Date', text='Added Date')
studentTable.heading('Added Time', text='Added Time')


studentTable.config(show='headings')

root.mainloop()
