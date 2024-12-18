from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox,filedialog
import mysql.connector
import re
import pandas as pd

'''
def toggle_cgpa_fields():
    """Toggle CGPA fields between single and range input."""
    if toggle_var.get() == "Search":
        # Hide single CGPA input and show minCGPA/maxCGPA inputs
        CGPAEntry.grid_forget()
        minCGPALabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
        minCGPAEntry.grid(row=6, column=1, pady=15, padx=10)
        maxCGPALabel.grid(row=7, column=0, padx=30, pady=15, sticky=W)
        maxCGPAEntry.grid(row=7, column=1, pady=15, padx=10)
    else:
        # Hide minCGPA/maxCGPA inputs and show single CGPA input
        minCGPALabel.grid_forget()
        minCGPAEntry.grid_forget()
        maxCGPALabel.grid_forget()
        maxCGPAEntry.grid_forget()
        CGPALabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
        CGPAEntry.grid(row=6, column=1, pady=15, padx=10)'''

# FUNCTIONALITY PART
def toplevel_data(title, button_text, command):
    global idEntry, nameEntry, phoneEntry, emailEntry, addressEntry, gender_combobox, CGPAEntry, dobEntry, screen
    #global minCGPAEntry, maxCGPAEntry, minCGPALabel, maxCGPALabel, CGPALabel, toggle_var

    screen = Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(False, False)
    idLabel = Label(screen, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(screen, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(screen, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(screen, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(screen, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    '''genderLabel = Label(screen, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)'''

    gender_label = Label(screen, text="Gender", font=('times new roman', 20, 'bold'))
    gender_label.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    gender_options = ['Male', 'Female']
    gender_combobox = ttk.Combobox(screen, values=gender_options, font=('roman', 15, 'bold'), width=24)
    gender_combobox.grid(row=5, column=1, pady=15, padx=10)

    CGPALabel = Label(screen, text='CGPA', font=('times new roman', 20, 'bold'))
    CGPALabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    CGPAEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    CGPAEntry.grid(row=6, column=1, pady=15, padx=10)

    ''' # CGPA Fields
    CGPALabel = Label(screen, text='CGPA', font=('times new roman', 20, 'bold'))
    CGPAEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)

    # Min and Max CGPA Fields (hidden initially)
    minCGPALabel = Label(screen, text='Min CGPA', font=('times new roman', 20, 'bold'))
    minCGPAEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    maxCGPALabel = Label(screen, text='Max CGPA', font=('times new roman', 20, 'bold'))
    maxCGPAEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)

    dobLabel = Label(screen, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=8, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=8, column=1, pady=15, padx=10)

    # Initial Layout for CGPA field
    CGPALabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    CGPAEntry.grid(row=6, column=1, pady=15, padx=10)

    # Toggle button to switch between "Add" and "Search" modes
    toggle_button = ttk.Button(
        screen,
        textvariable=toggle_var,
        command=lambda: toggle_var.set("Search" if toggle_var.get() == "Add" else "Add") or toggle_cgpa_fields()
    )
    toggle_button.grid(row=9, column=0, columnspan=2, pady=15)

    student_button = ttk.Button(screen, text=button_text, command=command)
    student_button.grid(row=10, columnspan=2, pady=15)

    # You can remove the command_function from here if you want to handle the logic elsewhere.
    def command_function():
        if toggle_var.get() == "Search":
            print(f"Searching for students with CGPA between {minCGPAEntry.get()} and {maxCGPAEntry.get()}")
        else:
            print(f"Adding student with CGPA: {CGPAEntry.get()}")

    # Avoid recursive calls; only call toplevel_data once
    # Example of how to call toplevel_data
    if title != 'Update Student':
        screen.mainloop()

# Call the function with a title and button text
toplevel_data("Student Form", "Submit", lambda: print("Submitted"))'''

    dobLabel = Label(screen, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=7, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=7, column=1, pady=15, padx=10)

    student_button = ttk.Button(screen, text=button_text, command=command)
    student_button.grid(row=8, columnspan=2, pady=15)


    if title=='Update Student':
        indexing = studentTable.focus()
        content = studentTable.item(indexing)
        listdata = content['values']
        idEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        phoneEntry.insert(0, listdata[2])
        emailEntry.insert(0, listdata[3])
        addressEntry.insert(0, listdata[4])
        gender_combobox.insert(0, listdata[5])
        CGPAEntry.insert(0, listdata[6])
        dobEntry.insert(0, listdata[7])

def iexit():
    result=messagebox.askyesno('Confirm', 'Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass


def export_data():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = studentTable.get_children()
    newlist = []

    for index in indexing:
        content = studentTable.item(index)
        datalist = content['values']
        newlist.append(datalist)

    table = pd.DataFrame(newlist, columns=['Id', 'Name', 'Mobile', 'Email', 'Address', 'Gender', 'CGPA', 'DOB', 'Added Time', 'Added Date'])
    table.to_csv(url, index=False)
    messagebox.showinfo('Success', 'Data is saved successfully')


def update_data():
    currentdate = time.strftime('%d/%m/%Y')
    currenttime = time.strftime('%I:%M:%S %p')

    # Ensure phone number is treated as a string, preserving leading zeros
    phone_number = phoneEntry.get().strip()  # Remove any extra spaces if present
    phone_number = str(phone_number).zfill(11)  # Ensure the number is exactly 11 digits, including leading zero

    if len(phone_number) != 11:
        messagebox.showerror('Error', 'Phone number must be exactly 11 digits.', parent=screen)
        return

    # Correct order: name, mobile, email, address, gender, dob, date, time, id
    query = '''
        UPDATE student SET
            name = %s,
            mobile = %s,
            email = %s,
            address = %s,
            gender = %s, 
            CGPA = %s,
            dob = %s,
            date = %s,
            time = %s
        WHERE id = %s'''

    # Ensure the parameters are in the correct order
    parameters = (
        nameEntry.get(),
        #phoneEntry.get(),
        phone_number,
        emailEntry.get(),
        addressEntry.get(),
        gender_combobox.get(),
        CGPAEntry.get(),
        dobEntry.get(),
        currentdate,
        currenttime,
        idEntry.get()  # This is for the WHERE clause
    )

    try:
        mycursor.execute(query, parameters)
        con.commit()
        messagebox.showinfo('Success', f'ID {idEntry.get()} has been modified successfully.', parent=screen)
        screen.destroy()
        show_student()
    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Failed to update data: {err}', parent=screen)

def show_student():
    query = 'SELECT * FROM student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)

'''def show_student():
    mycursor.execute("SELECT * FROM student")
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())  # Clear existing table rows
    for row in fetched_data:
        studentTable.insert('', 'end', values=row)  # Insert updated rows into the table
'''

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


'''def search_data():
    query='select * from student where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or CGPA=%s or dob=%s'
    mycursor.execute(query,(idEntry.get(), nameEntry.get(), emailEntry.get(), phoneEntry.get(), addressEntry.get(), gender_combobox.get(), CGPAEntry.get(), dobEntry.get()))
    studentTable.delete(*studentTable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('',END,values=data)'''


'''def search_data():
    # Retrieve user input
    student_id = idEntry.get()
    name = nameEntry.get()
    email = emailEntry.get()
    phone = phoneEntry.get()
    address = addressEntry.get()
    gender = gender_combobox.get()
    CGPA = CGPAEntry.get()
    dob = dobEntry.get()

    # Check if CGPA is a valid float
    if CGPA and not CGPA.replace('.', '', 1).isdigit():
        messagebox.showerror('Error', 'CGPA must be a valid number', parent=screen)
        return
    else:
        CGPA = float(CGPA) if CGPA else None  # Convert CGPA to float if valid

    # Adjust the query to handle the CGPA field as a float with a tolerance for comparison
    query = 
    SELECT * FROM student
    WHERE id=%s OR name=%s OR email=%s OR mobile=%s OR address=%s OR gender=%s OR
    (%s IS NULL OR ROUND(CGPA, 2)=%s) OR dob=%s
    

    # Execute the query, using 'None' for CGPA if not provided
    mycursor.execute(query, (student_id, name, email, phone, address, gender, CGPA, CGPA, dob))
    studentTable.delete(*studentTable.get_children())
    fetched_data = mycursor.fetchall()

    # Check if the query returned data and insert it into the table
    for data in fetched_data:
        studentTable.insert('', END, values=data)'''


def search_data():
    # Retrieve user inputs
    student_id = idEntry.get().strip()
    name = nameEntry.get().strip()
    email = emailEntry.get().strip()
    phone = phoneEntry.get().strip()
    address = addressEntry.get().strip()
    gender = gender_combobox.get().strip()
    CGPA = CGPAEntry.get().strip()
    dob = dobEntry.get().strip()

    # Validate CGPA if provided
    if CGPA:
        try:
            CGPA = float(CGPA)  # Convert to float
        except ValueError:
            messagebox.showerror('Error', 'CGPA must be a valid number', parent=screen)
            return
    else:
        CGPA = None  # Set to None if not provided

    # Base query and dynamic conditions
    query = 'SELECT * FROM student WHERE 1=1'  # "1=1" allows appending conditions dynamically
    params = []  # To store query parameters dynamically

    # Append conditions for each field
    if student_id:
        query += ' AND id = %s'
        params.append(student_id)
    if name:
        query += ' AND name = %s'
        params.append(name)
    if email:
        query += ' AND email = %s'
        params.append(email)
    if phone:
        query += ' AND mobile = %s'
        params.append(phone)
    if address:
        query += ' AND address = %s'
        params.append(address)
    if gender:
        query += ' AND gender = %s'
        params.append(gender)
    if CGPA is not None:
        query += ' AND ROUND(CGPA, 2) = ROUND(%s, 2)'
        params.append(CGPA)
    if dob:
        query += ' AND dob = %s'
        params.append(dob)

    # Execute the query
    mycursor.execute(query, tuple(params))

    # Clear the current table entries
    studentTable.delete(*studentTable.get_children())

    # Fetch and display the results
    fetched_data = mycursor.fetchall()
    if fetched_data:
        for data in fetched_data:
            studentTable.insert('', END, values=data)
    else:
        messagebox.showinfo('Info', 'No matching records found.', parent=screen)




def add_data():
    # Retrieve entries
    student_id = idEntry.get()
    name = nameEntry.get()
    phone = phoneEntry.get()
    email = emailEntry.get()
    address = addressEntry.get()
    gender = gender_combobox.get()
    CGPA = CGPAEntry.get()
    dob = dobEntry.get()

    # Validation for student_id
    if not (student_id.isdigit() and len(student_id) == 3):
        messagebox.showerror('Error', 'ID must be exactly 3 digits.', parent=screen)
        return
    if not re.match(r"^[A-Za-z\s\-]+$", name):
        messagebox.showerror('Error', 'Name should only contain alphabetic characters.', parent=screen)
        return
    if not (phone.isdigit() and len(phone) == 11):
        messagebox.showerror('Error', 'Phone number must be exactly 11 digits.', parent=screen)
        return
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror('Error', 'Invalid email format. Must contain "@" and a domain.', parent=screen)
        return
    if gender.lower() not in ['male', 'female']:
        messagebox.showerror('Error', 'Gender must be "male" or "female".', parent=screen)
        return
    if not re.match(r"\d{2}/\d{2}/\d{4}", dob):
        messagebox.showerror('Error', 'DOB format should be "dd/mm/yyyy".', parent=screen)
        return

    # Additional check to ensure no fields are empty
    if student_id == '' or name == '' or phone == '' or email == '' or address == '' or gender == '' or CGPA == '' or dob == '':
        messagebox.showerror('Error', 'All fields are required', parent=screen)
        return

    # Check if ID already exists
    mycursor.execute("SELECT * FROM student WHERE id = %s", (student_id,))
    existing_record = mycursor.fetchone()
    if existing_record:
        messagebox.showerror('Error', 'ID already exists. Please use a unique ID.', parent=screen)
        return

    # Insert data if all validations pass
    currentdate = time.strftime('%d/%m/%Y')
    currenttime = time.strftime('%I:%M:%S %p')
    query = 'INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    try:
        mycursor.execute(query, (student_id, name, phone, email, address, gender, CGPA, dob, currentdate, currenttime))
        con.commit()
        result = messagebox.askyesno('Confirm', 'Data added successfully. Do you want to clean the form?',
                                     parent=screen)

        # Refresh the student table immediately after inserting new data
        show_student()

        # Ask user if they want to clear the form
        result = messagebox.askyesno('Confirm', 'Do you want to clean the form?', parent=screen)

        if result:
            idEntry.delete(0, END)
            nameEntry.delete(0, END)
            phoneEntry.delete(0, END)
            emailEntry.delete(0, END)
            addressEntry.delete(0, END)
            gender_combobox.set('')
            CGPAEntry.delete(0, END)
            dobEntry.delete(0, END)

    except mysql.connector.IntegrityError as e:
        messagebox.showerror('Error', f'Failed to add data: {e}', parent=screen)
        '''query = 'select *from student'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('', END, values=data)'''

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
                         'CGPA VARCHAR(20), '
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
    date = time.strftime('%d/%m/%Y')  # Current date
    currenttime = time.strftime('%I:%M:%S %p')  # Current time
    datetimeLabel.config(text=f'Date: {date}\nTime: {currenttime}')
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

addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25, state=DISABLED, command=lambda :toplevel_data('Add Student','Add', add_data))
addstudentButton.grid(row=1, column=0, pady=20)

searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25, state=DISABLED, command=lambda :toplevel_data('Search Student','Search', search_data))
searchstudentButton.grid(row=2, column=0, pady=20)

deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25, state=DISABLED, command=delete_student)
deletestudentButton.grid(row=3, column=0, pady=20)

updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25, state=DISABLED, command=lambda :toplevel_data('Update Student','Update', update_data))
updatestudentButton.grid(row=4, column=0, pady=20)

showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25, state=DISABLED, command=show_student)
showstudentButton.grid(row=5, column=0, pady=20)

exportstudentButton=ttk.Button(leftFrame,text='Export Data',width=25, state=DISABLED, command=export_data)
exportstudentButton.grid(row=6, column=0, pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25, command=iexit)
exitButton.grid(row=7, column=0, pady=20)

rightFrame = Frame(root,bg='yellow')
rightFrame.place(x=350, y=80, width=1000, height=600)

scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile','Email', 'Address', 'Gender','CGPA', 'D.O.B', 'Added Date', 'Added Time'),
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
studentTable.heading('CGPA', text='CGPA')
studentTable.heading('D.O.B', text='D.O.B')
studentTable.heading('Added Date', text='Added Date')
studentTable.heading('Added Time', text='Added Time')


studentTable.column('Id', width=50, anchor=CENTER)
studentTable.column('Name', width=300, anchor=CENTER)
studentTable.column('Email', width=300, anchor=CENTER)
studentTable.column('Mobile', width=200, anchor=CENTER)
studentTable.column('Address', width=300, anchor=CENTER)
studentTable.column('Gender', width=100, anchor=CENTER)
studentTable.column('CGPA', width=100, anchor=CENTER)
studentTable.column('D.O.B', width=100, anchor=CENTER)
studentTable.column('Added Date', width=200, anchor=CENTER)
studentTable.column('Added Time', width=200, anchor=CENTER)

style=ttk.Style()

style.configure('Treeview', rowheight=40, font=('arial',12,'bold'),foreground='red4', background='white', fieldbackground='white')
style.configure('Treeview.Heading', font=('arial',14,'bold'), foreground='blue')



studentTable.config(show='headings')

root.mainloop()
