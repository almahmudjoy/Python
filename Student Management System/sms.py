from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox
import mysql.connector
import re


# FUNCTIONALITY PART

def delete_student():
    indexing = studentTable.focus()

    if not indexing:
        messagebox.showwarning("Delete", "No student selected for deletion")
        return

    content = studentTable.item(indexing)
    content_id = content['values'][0]

    # Confirm deletion with the user
    confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete student with ID {content_id}?")
    if not confirm:
        return

    # Execute delete query with content_id as a tuple
    query = 'DELETE FROM student WHERE id=%s'
    mycursor.execute(query, (content_id,))
    con.commit()

    messagebox.showinfo('Delete', f'ID {content_id} has been deleted successfully.')

    # Refresh studentTable after deletion
    query = 'SELECT * FROM student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)


def search_student():
    def search_data():
        query='select * from student where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s'
        mycursor.execute(query,(idEntry.get(), nameEntry.get(), emailEntry.get(), phoneEntry.get(), addressEntry.get(), genderEntry.get(), dobEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('',END,values=data)

    search_window = Toplevel()
    search_window.title('Search Student')
    search_window.grab_set()
    search_window.resizable(False, False)
    idLabel = Label(search_window, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(search_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(search_window, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(search_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(search_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    genderLabel = Label(search_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel = Label(search_window, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, pady=15, padx=10)

    search_student_button = ttk.Button(search_window, text='SEARCH', command=search_data)
    search_student_button.grid(row=7, columnspan=2, pady=15)

def add_student():

    def add_data():
        # Retrieve entries
        student_id = idEntry.get()
        name = nameEntry.get()
        phone = phoneEntry.get()
        email = emailEntry.get()
        address = addressEntry.get()
        gender = genderEntry.get()
        dob = dobEntry.get()

        # Validation checks
        if not (student_id.isdigit() and len(student_id) == 3):
            messagebox.showerror('Error', 'ID must be exactly 3 digits.', parent=add_window)
            return
        if not name.isalpha():
            messagebox.showerror('Error', 'Name should only contain alphabetic characters.', parent=add_window)
            return
        if not (phone.isdigit() and len(phone) == 11):
            messagebox.showerror('Error', 'Phone number must be exactly 11 digits.', parent=add_window)
            return
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror('Error', 'Invalid email format. Must contain "@" and a domain.', parent=add_window)
            return
        if gender.lower() not in ['male', 'female']:
            messagebox.showerror('Error', 'Gender must be "male" or "female".', parent=add_window)
            return
        if not re.match(r"\d{2}/\d{2}/\d{4}", dob):
            messagebox.showerror('Error', 'DOB format should be "dd/mm/yyyy".', parent=add_window)
            return

        # Additional check to ensure no fields are empty
        if student_id == '' or name == '' or phone == '' or email == '' or address == '' or gender == '' or dob == '':
            messagebox.showerror('Error', 'All fields are required', parent=add_window)
            return

        # Check if ID already exists
        mycursor.execute("SELECT * FROM student WHERE id = %s", (student_id,))
        existing_record = mycursor.fetchone()
        if existing_record:
            messagebox.showerror('Error', 'ID already exists. Please use a unique ID.', parent=add_window)
            return

        # Insert data if all validations pass
        currentdate = time.strftime('%d/%m/%Y')
        currenttime = time.strftime('%I:%M:%S %p')
        query = 'INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        try:
            mycursor.execute(query, (student_id, name, phone, email, address, gender, dob, currentdate, currenttime))
            con.commit()
            result = messagebox.askyesno('Confirm', 'Data added successfully. Do you want to clean the form?',
                                         parent=add_window)
            if result:
                idEntry.delete(0, END)
                nameEntry.delete(0, END)
                phoneEntry.delete(0, END)
                emailEntry.delete(0, END)
                addressEntry.delete(0, END)
                genderEntry.delete(0, END)
                dobEntry.delete(0, END)
        except mysql.connector.IntegrityError as e:
            messagebox.showerror('Error', f'Failed to add data: {e}', parent=add_window)
        query = 'select *from student'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('', END, values=data)

    add_window=Toplevel()
    add_window.grab_set()
    add_window.resizable(False,False)
    idLabel=Label(add_window, text='Id',font=('times new roman', 20,'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15,sticky=W)
    idEntry=Entry(add_window, font=('roman', 15,'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel=Label(add_window, text='Name',font=('times new roman', 20,'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15,sticky=W)
    nameEntry=Entry(add_window, font=('roman', 15,'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel=Label(add_window, text='Phone',font=('times new roman', 20,'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15,sticky=W)
    phoneEntry=Entry(add_window, font=('roman', 15,'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel=Label(add_window, text='Email',font=('times new roman', 20,'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15,sticky=W)
    emailEntry=Entry(add_window, font=('roman', 15,'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel=Label(add_window, text='Address',font=('times new roman', 20,'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15,sticky=W)
    addressEntry=Entry(add_window, font=('roman', 15,'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    genderLabel=Label(add_window, text='Gender',font=('times new roman', 20,'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15,sticky=W)
    genderEntry=Entry(add_window, font=('roman', 15,'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel=Label(add_window, text='D.O.B',font=('times new roman', 20,'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15,sticky=W)
    dobEntry=Entry(add_window, font=('roman', 15,'bold'), width=24)
    dobEntry.grid(row=6, column=1, pady=15, padx=10)

    add_student_button=ttk.Button(add_window,text='ADD STUDENT', command=add_data)
    add_student_button.grid(row=7, columnspan=2, pady=15)


def connect_database():
    def connect():
        global mycursor, con
        try:
            # Establish connection to the MySQL database
            con = mysql.connector.connect(
                host='localhost',         #hostEntry.get()
                user='root',              #userEntry.get(),
                password=''               #passwordEntry.get()
            )
            mycursor = con.cursor()
            mycursor.execute("SHOW DATABASES")  # Sample command to check connection

            # Fetch all results to avoid "Unread result found" error
            mycursor.fetchall()

            messagebox.showinfo('Success', 'Database Connection is Successful', parent=connectWindow)

            try:
                # Create database and table if they don't exist
                query = 'CREATE DATABASE IF NOT EXISTS studentmanagementsystem'
                mycursor.execute(query)

                # Use the database
                mycursor.execute('USE studentmanagementsystem')

                # Create the student table if it doesn't exist
                query = ('CREATE TABLE IF NOT EXISTS student ('
                         'id INT NOT NULL PRIMARY KEY, '
                         'name VARCHAR(30), '
                         'mobile VARCHAR(11), '
                         'email VARCHAR(30), '
                         'address VARCHAR(100), '
                         'gender VARCHAR(20), '
                         'dob VARCHAR(50), ' 
                         'date VARCHAR(50), '
                         'time VARCHAR(50))')
                mycursor.execute(query)

                # Enable buttons after successful connection and table creation
                addstudentButton.config(state=NORMAL)
                searchstudentButton.config(state=NORMAL)
                updatestudentButton.config(state=NORMAL)
                showstudentButton.config(state=NORMAL)
                exportstudentButton.config(state=NORMAL)
                deletestudentButton.config(state=NORMAL)

                # Close the connection window after successful connection
                connectWindow.destroy()

            except mysql.connector.Error as err:
                messagebox.showerror('Error', f"Failed to create database/table: {err}", parent=connectWindow)

        except mysql.connector.Error as err:
            messagebox.showerror('Error', f"Connection failed: {err}", parent=connectWindow)

            # Close the connection window here as well if the connection fails
            connectWindow.destroy()

    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0, 0)

    hostnameLabel = Label(connectWindow, text='Host Name', font=('arial', 20, 'bold'))
    hostnameLabel.grid(row=0, column=0, padx=20)

    hostEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    hostEntry.grid(row=0, column=1, padx=40, pady=20)

    usernameLabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    userEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    userEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordnameLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordnameLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton = ttk.Button(connectWindow, text='Connect', command=connect)
    connectButton.grid(row=3, columnspan=2)


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

connectButton = ttk.Button(root,text='Connect Database', command=connect_database)
connectButton.place(x=1100,y=0)

leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)

logo_image=PhotoImage(file='student (1).png')
logo_Label=Label(leftFrame, image=logo_image)
logo_Label.grid(row=0, column=0)

addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25, state=DISABLED, command=add_student)
addstudentButton.grid(row=1, column=0, pady=20)

searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25, state=DISABLED, command=search_student)
searchstudentButton.grid(row=2, column=0, pady=20)

deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25, state=DISABLED, command=delete_student)
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

studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile','Email', 'Address', 'Gender', 'D.O.B', 'Added Date', 'Added Time'),
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
