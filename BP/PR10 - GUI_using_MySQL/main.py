import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import mysql.connector

# ---------- MySQL Connection ----------
root = tk.Tk()
root.withdraw()  # Hide main window temporarily while asking for password

password = simpledialog.askstring(
    "Database Password", "Enter MySQL password:", show="*"
)

if not password:
    messagebox.showerror("Error", "Password is required to connect to the database.")
    root.destroy()
    exit()

try:
    db = mysql.connector.connect(
        host="localhost", user="root", password=password, database="testdb"
    )
    cursor = db.cursor()
except mysql.connector.Error as e:
    messagebox.showerror("Connection Failed", f"Could not connect to database:\n{e}")
    root.destroy()
    exit()

root.deiconify()  # Show main window now that connection is established


# ---------- Functions ----------
def insert_data():
    name = name_var.get().strip()
    email = email_var.get().strip()
    if name and email:
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        db.commit()
        messagebox.showinfo("Success", "Record added!")
        clear_fields()
        fetch_data()
    else:
        messagebox.showwarning("Input Error", "All fields required!")


def fetch_data():
    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=tuple(row))


def clear_fields():
    id_var.set("")
    name_var.set("")
    email_var.set("")


def select_row(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected, "values")
        id_var.set(values[0])
        name_var.set(values[1])
        email_var.set(values[2])


def update_data():
    if not id_var.get():
        messagebox.showwarning("Select Record", "Please select a record to update.")
        return
    cursor.execute(
        "UPDATE users SET name=%s, email=%s WHERE id=%s",
        (name_var.get(), email_var.get(), id_var.get()),
    )
    db.commit()
    messagebox.showinfo("Success", "Record updated!")
    clear_fields()
    fetch_data()


def delete_data():
    if not id_var.get():
        messagebox.showwarning("Select Record", "Please select a record to delete.")
        return
    cursor.execute("DELETE FROM users WHERE id=%s", (id_var.get(),))
    db.commit()
    messagebox.showinfo("Deleted", "Record deleted!")
    clear_fields()
    fetch_data()


# ---------- GUI Setup ----------
root.title("MySQL CRUD GUI App")
root.geometry("600x500")
root.config(bg="#f8f9fa")

# Variables
id_var = tk.StringVar()
name_var = tk.StringVar()
email_var = tk.StringVar()

# Entry Form
form_frame = tk.Frame(root, bg="#f8f9fa")
form_frame.pack(pady=10)

tk.Label(form_frame, text="Name:", font=("Arial", 12), bg="#f8f9fa").grid(
    row=0, column=0, padx=10, pady=5
)
tk.Entry(form_frame, textvariable=name_var, font=("Arial", 12), width=30).grid(
    row=0, column=1, pady=5
)

tk.Label(form_frame, text="Email:", font=("Arial", 12), bg="#f8f9fa").grid(
    row=1, column=0, padx=10, pady=5
)
tk.Entry(form_frame, textvariable=email_var, font=("Arial", 12), width=30).grid(
    row=1, column=1, pady=5
)

# Button Frame
btn_frame = tk.Frame(root, bg="#f8f9fa")
btn_frame.pack(pady=10)

tk.Button(
    btn_frame, text="Add", command=insert_data, bg="#2ecc71", fg="white", width=10
).grid(row=0, column=0, padx=5)
tk.Button(
    btn_frame, text="Update", command=update_data, bg="#f39c12", fg="white", width=10
).grid(row=0, column=1, padx=5)
tk.Button(
    btn_frame, text="Delete", command=delete_data, bg="#e74c3c", fg="white", width=10
).grid(row=0, column=2, padx=5)
tk.Button(
    btn_frame, text="Clear", command=clear_fields, bg="#95a5a6", fg="white", width=10
).grid(row=0, column=3, padx=5)

# Treeview for Data Display
tree_frame = tk.Frame(root)
tree_frame.pack(pady=10)

cols = ("ID", "Name", "Email")
tree = ttk.Treeview(tree_frame, columns=cols, show="headings", height=10)
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=180 if col != "ID" else 50)

tree.pack()
tree.bind("<ButtonRelease-1>", select_row)

# Initial fetch
fetch_data()

# Run GUI
root.mainloop()
