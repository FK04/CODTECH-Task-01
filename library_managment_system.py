import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime, timedelta
import mysql.connector

# Database connection
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="your_user_name",  # Replace with your MySQL username
    password="your_password",  # Replace with your MySQL password
    database="library_db"
)
cursor = conn.cursor()

# Library Management Class
class Library:
    def __init__(self):
        pass

    def add_item(self, title, author, category, status='available', due_date=None):
        cursor.execute('''INSERT INTO books_data (title, author, category, status, due_date) 
                          VALUES (%s, %s, %s, %s, %s)''',
                       (title, author, category, status, due_date))
        conn.commit()
        return f"{title} has been added to the library."

    def search_item(self, search_field, search_value):
        query = f"SELECT * FROM books_data WHERE {search_field} LIKE %s"
        cursor.execute(query, (f"%{search_value}%",))
        return cursor.fetchall()

    def view_all_items(self):
        cursor.execute("SELECT * FROM books_data")
        return cursor.fetchall()

    def update_item(self, bid, field, new_value):
        query = f"UPDATE books_data SET {field} = %s WHERE bid = %s"
        cursor.execute(query, (new_value, bid))
        conn.commit()
        return f"{field.capitalize()} updated successfully for Book ID {bid}."

# GUI setup with Tkinter
library = Library()

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    category = category_entry.get()
    
    if title and author and category:
        message = library.add_item(title, author, category)
        messagebox.showinfo("Success", message)
        view_all_data()
    else:
        messagebox.showwarning("Input Error", "Please fill all fields")

def search_book():
    search_field = search_field_var.get().lower()  # Get selected search field
    search_value = search_entry.get()
    results = library.search_item(search_field, search_value)
    display_results(results)

def update_book():
    bid = update_id_entry.get()
    field = update_field_var.get().lower()
    new_value = update_value_entry.get()
    
    if bid and field and new_value:
        message = library.update_item(bid, field, new_value)
        messagebox.showinfo("Update", message)
        view_all_data()
    else:
        messagebox.showwarning("Input Error", "Please provide all update details")

def view_all_data():
    results = library.view_all_items()
    display_results(results)

def display_results(results):
    for row in tree.get_children():
        tree.delete(row)
    for item in results:
        tree.insert("", "end", values=item)

# Setting up main window
root = tk.Tk()
root.title("Library Management System")
root.geometry("710x645")  # Adjusted for more space

# Main Frame for Add and Update
main_frame = tk.Frame(root)
main_frame.pack(pady=10, fill="x", expand=True)

# Configure grid layout for main_frame to allow expansion
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

# Frame for Adding Items
add_frame = tk.LabelFrame(main_frame, text="Add New Item", padx=10, pady=10)
add_frame.grid(row=0, column=0, sticky="nsew", padx=5)

tk.Label(add_frame, text="Title").grid(row=0, column=0)
title_entry = tk.Entry(add_frame, width=20)
title_entry.grid(row=0, column=1)

tk.Label(add_frame, text="Author").grid(row=1, column=0)
author_entry = tk.Entry(add_frame, width=20)
author_entry.grid(row=1, column=1)

tk.Label(add_frame, text="Category").grid(row=2, column=0)
category_entry = tk.Entry(add_frame, width=20)
category_entry.grid(row=2, column=1)

add_button = tk.Button(add_frame, text="Add Item", command=add_book, width=15)
add_button.grid(row=3, column=0, columnspan=2, pady=5)

# Frame for Updating Items
update_frame = tk.LabelFrame(main_frame, text="Update Item", padx=10, pady=10)
update_frame.grid(row=0, column=1, sticky="nsew", padx=5)

tk.Label(update_frame, text="Book ID").grid(row=0, column=0)
update_id_entry = tk.Entry(update_frame, width=20)
update_id_entry.grid(row=0, column=1)

tk.Label(update_frame, text="Field to Update").grid(row=1, column=0)
update_field_var = tk.StringVar()
update_field_menu = ttk.Combobox(update_frame, textvariable=update_field_var, values=["Title", "Author", "Category"], width=18)
update_field_menu.grid(row=1, column=1)
update_field_menu.current(0)

tk.Label(update_frame, text="New Value").grid(row=2, column=0)
update_value_entry = tk.Entry(update_frame, width=20)
update_value_entry.grid(row=2, column=1)

update_button = tk.Button(update_frame, text="Update Item", command=update_book, width=15)
update_button.grid(row=3, column=0, columnspan=2, pady=5)

# Frame for Searching Items
search_frame = tk.LabelFrame(root, text="Search Item", padx=10, pady=10)
search_frame.pack(pady=10, fill="x")

# Dropdown menu for search field selection
search_field_var = tk.StringVar()
search_field_var.set("Title")  # Default search field

search_field_menu = ttk.Combobox(search_frame, textvariable=search_field_var, values=["Title", "Author", "Category"], width=10)
search_field_menu.grid(row=0, column=0)
search_field_menu.current(0)

search_entry = tk.Entry(search_frame, width=20)
search_entry.grid(row=0, column=1)

search_button = tk.Button(search_frame, text="Search", command=search_book, width=15)
search_button.grid(row=0, column=2)

# Aligning "View All Data" to the right in the same row
view_button = tk.Button(search_frame, text="View All Data", command=view_all_data, width=15)
view_button.grid(row=0, column=3, sticky="e", padx=(100, 0))

# Treeview for displaying search results
tree_frame = tk.Frame(root)
tree_frame.pack(pady=10, fill="both", expand=True)

# Adjust column widths to fit within 900 pixels for the Treeview
tree = ttk.Treeview(tree_frame, columns=("ID", "Title", "Author", "Category", "Status", "Due Date"), show="headings", height=10)
tree.heading("ID", text="ID")
tree.column("ID", width=50)

tree.heading("Title", text="Title")
tree.column("Title", width=200)

tree.heading("Author", text="Author")
tree.column("Author", width=150)

tree.heading("Category", text="Category")
tree.column("Category", width=100)

tree.heading("Status", text="Status")
tree.column("Status", width=80)

tree.heading("Due Date", text="Due Date")
tree.column("Due Date", width=100)

tree.pack(fill="both", expand=True)

# Frame for Checkout and Return
checkout_return_frame = tk.LabelFrame(root, text="Checkout / Return", padx=10, pady=10)
checkout_return_frame.pack(pady=10, fill="x")

# Checkout Section
tk.Label(checkout_return_frame, text="Checkout Title").grid(row=0, column=0)
checkout_entry = tk.Entry(checkout_return_frame, width=20)
checkout_entry.grid(row=0, column=1)
checkout_button = tk.Button(checkout_return_frame, text="Checkout", width=15)
checkout_button.grid(row=0, column=2)

# Return Section
tk.Label(checkout_return_frame, text="Return Title").grid(row=1, column=0)
return_entry = tk.Entry(checkout_return_frame, width=20)
return_entry.grid(row=1, column=1)
return_button = tk.Button(checkout_return_frame, text="Return", width=15)
return_button.grid(row=1, column=2)

# Run the main loop
root.mainloop()