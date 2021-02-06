# SHows how to open directory and files from within Tkinter
from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("Database Connection")

# Create a database
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Create table
c.execute("""
    CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text, 
    city text,
    state text,
    zipcode integer)
""")

# Commit Changes
conn.commit()

# Close the connection
conn.close()

root.mainloop()
