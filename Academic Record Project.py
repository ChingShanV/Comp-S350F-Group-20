from tkinter import *
import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "2002531vex",
    database = "comp350F_project"
    )

# Create a cursor
mycursor = mydb.cursor()


def change_info():
    # Implement your logic for changing student information here
    pass

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()
    user_type = var.get()

    if user_type == 1:  # Student Login
        # Check if student login exists in student_info table
        mycursor.execute("SELECT * FROM student_info WHERE login_id = %s", (username,))
        result = mycursor.fetchone()

        if result is None:
            messagebox.showerror("Error", "Invalid login ID")
        elif result[5] != password:
            messagebox.showerror("Error", "Invalid password")
        else:
            # Create a new window for student information display
            student_window = tk.Toplevel(window)
            student_window.title("Student Information")

            student_window.geometry("1000x760") 
            student_window.configure(bg="#8BC34A")

            # Add image file 
            bg2 = PhotoImage( file = "my ioh_banner 1 (1).png") 

            logo2 = PhotoImage( file = "HKMU-logo-mb (1).png")

            label4 = Label( student_window, image = bg2) 
            label4.place(x = 0,y = 0) 

            frametop2 = Frame( student_window, bg = "#FFFFFF") 
            frametop2.pack(pady = 0, padx = 0) 

            # Add text 
            label5 = Label( frametop2, text = "HKMU Academic Record System", bg = "#FFFFFF", fg="#8BC34A", font=("lucida", 40, "bold")) 

            label5.grid(row = 1,column = 2,padx = 70,pady = 0) 

            label6 = Label( frametop2, image = logo2, bg =  "#FFFFFF") 
            label6.grid(row = 1,column = 1,padx = 30,pady = 0) 


            # Create a label frame for student information
            info_frame = ttk.LabelFrame(student_window, text="Personal Information")
            info_frame.pack(padx=10, pady=(70,10))

            # Create labels and entry fields for student information
            labels = ["Student ID:", "Name:", "Gender:", "Telephone Number:", "Major:", "Year of Study:"]
            entries = []
            for i, label in enumerate(labels):
                ttk.Label(info_frame, text=label).grid(row=i, column=0, padx=5, pady=5)
                entry = ttk.Entry(info_frame)
                entry.grid(row=i, column=1, padx=5, pady=5)
                entries.append(entry)

            # Create a button to change student information
            change_btn = ttk.Button(student_window, text="Change Information", command=change_info)
            change_btn.pack(pady=(10,30))

            v=Scrollbar(student_window, orient='vertical')
            v.pack(side=RIGHT, fill='y')
            v2=Scrollbar(student_window, orient='horizontal')
            v2.pack(side=BOTTOM, fill='x')

            # Create a table frame for academic record
            record_frame = ttk.LabelFrame(student_window, text="Academic Record")
            record_frame.pack(padx=0, pady=(10,0))

            # Create a Treeview widget to display student information
            tree = ttk.Treeview(record_frame, yscrollcommand=v.set, xscrollcommand=v2.set)
            tree["columns"] = ("Student ID", "Student Name", "Gender", "Tel", "Major", "Year")

            # Configure column headings
            tree.heading("Student ID", text="Student ID")
            tree.heading("Student Name", text="Student Name")
            tree.heading("Gender", text="Gender")
            tree.heading("Tel", text="Telephone Number")
            tree.heading("Major", text="Major")
            tree.heading("Year", text="Year Of Studying")

            # Insert student information into the Treeview
            tree.insert("", tk.END, values=(result[0], result[1], result[2],result[3],result[6],result[7]))

            v.config(command=tree.yview)
            v2.config(command=tree.xview)

            # Pack the Treeview
            tree.pack()

    elif user_type == 2:  # Instructor Login
        # Check if instructor login exists in instructor_info table
        mycursor.execute("SELECT * FROM instructor_info WHERE login_id = %s", (username,))
        result = mycursor.fetchone()

        if result is None:
            messagebox.showerror("Error", "Invalid login ID")
        elif result[4] != password:
            messagebox.showerror("Error", "Invalid password")
        else:
            # Create a new window for instructor information display
            instructor_window = tk.Toplevel(window)
            instructor_window.title("Instructor Information")

            instructor_window.geometry("1000x760") 
            instructor_window.configure(bg="#8BC34A")

            # Add image file 
            bg3 = PhotoImage( file = "my ioh_banner 1 (1).png") 

            logo3 = PhotoImage( file = "HKMU-logo-mb (1).png")

            label7 = Label(instructor_window, image = bg3) 
            label7.place(x = 0,y = 0) 

            frametop3 = Frame(instructor_window, bg = "#FFFFFF") 
            frametop3.pack(pady = 0, padx = 0) 

            # Add text 
            label8 = Label( frametop3, text = "HKMU Academic Record System", bg = "#FFFFFF", fg="#8BC34A", font=("lucida", 40, "bold")) 

            label8.grid(row = 1,column = 2,padx = 70,pady = 0) 

            label9 = Label( frametop3, image = logo3, bg =  "#FFFFFF") 
            label9.grid(row = 1,column = 1,padx = 30,pady = 0) 

            v=Scrollbar(student_window, orient='vertical')
            v.pack(side=RIGHT, fill='y')
            v2=Scrollbar(student_window, orient='horizontal')
            v2.pack(side=BOTTOM, fill='x')

            # Create a table frame for academic record
            record_frame2 = ttk.LabelFrame(instructor_window, text="Student Information")
            record_frame2.pack(padx=0, pady=(10.0))

            # Create a Treeview widget to display instructor information
            tree = ttk.Treeview(record_frame2, yscrollcommand=v.set, xscrollcommand=v2.set)
            tree["columns"] = ("Name", "Gender", "Tel", "Major", "Year")

            # Configure column headings
            tree.heading("Name", text="Name")
            tree.heading("Gender", text="Gender")
            tree.heading("Tel", text="Telephone Number")

            # Insert instructor information into the Treeview
            tree.insert("", tk.END, values=(result[0], result[1], result[2]))

            v.config(command=tree.yview)
            v2.config(command=tree.xview)

            # Pack the Treeview
            tree.pack()

# Create the main Tkinter window
window = tk.Tk()
window.title("Login Page")
 # Adjust size 
window.geometry("1000x580") 

# Add image file 
bg = PhotoImage( file = "HKMU_homepage.png") 

logo = PhotoImage( file = "HKMU-logo-mb (1).png")

# Show image using label 
label1 = Label( window, image = bg) 
label1.place(x = 0,y = 0) 

frametop = Frame( window, bg = "#FFFFFF") 
frametop.pack(pady = 0, padx = 0) 

# Add text 
label2 = Label( frametop, text = "HKMU Academic Record System", 
			bg = "#FFFFFF", fg="#8BC34A", font=("lucida", 40, "bold")) 

label2.grid(row = 1,column = 2,padx = 70,pady = 0) 

label3 = Label( frametop, image = logo, bg =  "#FFFFFF") 
label3.grid(row = 1,column = 1,padx = 30,pady = 0) 

# Create Frame 
frame1 = Frame( window, bg = "#FFFFFF") 
frame1.pack(pady = 60, padx = 100)  

# Create username label and entry
username_label = Label(frame1,text = "Username:",font=("lucida",25,'bold'),fg = "#000000",bg = "#FFFFFF")
username_label.grid(row = 1,column = 1,padx = 40,pady = 40)
username_entry = Entry(frame1, fg = "#000000", bg = "#ECEFF1")
username_entry.grid(row = 1,column = 2,ipady = 7,ipadx = 20,padx = 40)

# Create password label and entry
password_label = Label(frame1,text="Password:",font=("lucida",25,"bold"),fg = "#000000",bg = "#FFFFFF")
password_label.grid(row = 2,column = 1,pady = 40)
password_entry = Entry(frame1,fg = "#000000", bg = "#ECEFF1", show="*")
password_entry.grid(row = 2,column = 2,ipady = 1,ipadx = 20,padx = 40)

# Create radio buttons for user type
var = tk.IntVar()
student_radio = tk.Radiobutton(frame1, text="Student",font=("lucida",25,"bold"),bg = "#FFFFFF",fg = "#000000",bd = 7, variable=var, value=1)
student_radio.grid(row = 3,column = 1,ipady = 7,ipadx = 20,padx = 40)
instructor_radio = tk.Radiobutton(frame1, text="Instructor",font=("lucida",25,"bold"),bg = "#FFFFFF",fg = "#000000",bd = 7, variable=var, value=2)
instructor_radio.grid(row = 3,column = 2,ipady = 1,ipadx = 20,padx = 40)

# Create login button
login_button = Button(frame1,text = "Login",font=("lucida",25,"bold"),bg = "#8E44AD",fg = "#000000",bd = 7, command=login)
login_button.grid(row = 4,column = 2, pady = 40,padx = 40)
# Start the Tkinter event loop
window.mainloop()