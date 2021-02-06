from tkinter import *
import sqlite3

root = Tk()
root.title("Database Connection")
root.geometry("360x400")

# Create submit function
def submit():
    # Create a database
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Insert into Table
    # The : represents dummy variables
    c.execute("INSERT INTO addresses VALUES(:f_name,:l_name,:address,:city,:state,:zipcode)",
        {
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        'zipcode':zipcode.get()
        })
    # Commit changes
    conn.commit()

    # Close the connection
    conn.close()

    # Clear the text boxes
    f_name.delete(0,END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

# Create the query function
def query():
    # Create a database
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Query the database
    # The oid is the primary key, SQLlite automatically creates this for you
    c.execute("SELECT *,oid FROM addresses")
    records = c.fetchall() # Fetch all records
    #print(records)

    print_records = ''
    for record in records:
        print_records += str(record[0]) +" "+str(record[1])+" "+str(record[6])+"\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=11,column=0,columnspan=2)

    # Commit changes
    conn.commit()

    # Close the connection
    conn.close()

## Create function to delete a record ##
def delete():
    # Create a database
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from addresses WHERE oid="+delete_box.get())


    # Commit changes
    conn.commit()

    # Close the connection
    conn.close()


# Create table
'''
c.execute("""
    CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text, 
    city text,
    state text,
    zipcode integer)
""")
'''

# Function to pdate a record #
def update():
    # Create a database
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    #Execute the command
    record_id = delete_box.get()
    c.execute("""UPDATE addresses SET 
    first_name=:f_name,
    last_name=:l_name,
    address=:address,
    city=:city,
    state=:state,
    zipcode=:zipcode
    WHERE oid = :oid""",
    {
        'f_name': f_name_editor.get(),
        'l_name': l_name_editor.get(),
        'address': address_editor.get(),
        'city': city_editor.get(),
        'state': state_editor.get(),
        'zipcode': zipcode_editor.get(),
        'oid': record_id
    }
              )

    #Commit changes
    conn.commit()

    # Close the connection
    conn.close()

    # Clear the text boxes
    editor.destroy()

## Function for editing a record ##
def edit():
    global editor
    editor = Tk()
    editor.title("Update a Record")
    editor.geometry("400x300")

    # Create a database
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    record_id =delete_box.get()

    # Query the database
    # The oid is the primary key, SQLlite automatically creates this for you
    c.execute("SELECT * FROM addresses WHERE oid="+record_id)

    records = c.fetchall()  # Fetch all records
    # print(records)

    #Create global variables as they are used in update function
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Creating text boxes for user interface
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20,pady=3)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20,pady=3)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20,pady=3)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20,pady=3)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20,pady=3)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20,pady=3)

    # Cretaing text box labels
    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=0,column=0)
    l_name_label_editor = Label(editor, text="Last Name")
    l_name_label_editor.grid(row=1,column=0)
    address_label_editor = Label(editor, text="Address")
    address_label_editor.grid(row=2,column=0)
    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3,column=0)
    state_label_editor = Label(editor, text="State")
    state_label_editor.grid(row=4,column=0)
    zip_label_editor = Label(editor, text="Zip Code")
    zip_label_editor.grid(row=5,column=0)

    # Create an Save Button
    edit_btn = Button(editor, text="Save Record", command = update)
    edit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=135)

    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        city_editor.insert(0,record[3])
        state_editor.insert(0,record[4])
        zipcode_editor.insert(0,record[5])

  # Commit changes
    conn.commit()

    # Close the connection
    conn.close()




# Creating text boxes for user interface
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20,pady=3)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20,pady=3)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20,pady=3)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20,pady=3)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20,pady=3)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20,pady=3)
delete_box = Entry(root, width=30)
delete_box.grid(row=8, column=1, padx=20,pady=3)

# Cretaing text box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0,column=0)
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1,column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2,column=0)
city_label = Label(root, text="City")
city_label.grid(row=3,column=0)
state_label = Label(root, text="State")
state_label.grid(row=4,column=0)
zip_label = Label(root, text="Zip Code")
zip_label.grid(row=5,column=0)
delete_label = Label(root, text="Select ID")
delete_label.grid(row=8,column=0)

# Create a submit Button
submit_btn = Button (root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

# Creating a query button
query_btn = Button(root, text="Show Records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=127)

# Creating a delete button
delete_btn = Button(root, text="Delete Record", command = delete)
delete_btn.grid(row=9,column=0,columnspan=2,pady=10,padx=10,ipadx=127)

# Create an Update Button
edit_btn = Button(root, text="Edit Record", command = edit)
edit_btn.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=135)


root.mainloop()