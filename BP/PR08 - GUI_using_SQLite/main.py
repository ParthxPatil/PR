import sqlite3
import ttkbootstrap as tb
from tkinter import messagebox, ttk

DB_NAME = "users.db"

# ---------- Database ----------
def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                address TEXT NOT NULL
            )
        """
        )

# ---------- CRUD ----------
def add_user():
    name, age, address = get_inputs()
    if not validate(name, age, address):
        return

    with get_connection() as conn:
        conn.execute(
            "INSERT INTO users (name, age, address) VALUES (?, ?, ?)",
            (name, age, address),
        )

    messagebox.showinfo("Success", "User added successfully!")
    clear_fields()
    view_users()

def view_users():
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM users").fetchall()

    tree.delete(*tree.get_children())
    for row in rows:
        tree.insert("", "end", values=row)

def update_user():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "Select a user to update.")
        return

    user_id = tree.item(selected[0], "values")[0]
    name, age, address = get_inputs()

    if not validate(name, age, address):
        return

    with get_connection() as conn:
        conn.execute(
            "UPDATE users SET name=?, age=?, address=? WHERE id=?",
            (name, age, address, user_id),
        )

    messagebox.showinfo("Success", "User updated successfully!")
    clear_fields()
    view_users()

def delete_user():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "Select a user to delete.")
        return

    user_id = tree.item(selected[0], "values")[0]

    with get_connection() as conn:
        conn.execute("DELETE FROM users WHERE id=?", (user_id,))

    messagebox.showinfo("Success", "User deleted successfully!")
    view_users()

# ---------- Helpers ----------
def get_inputs():
    return (name_var.get().strip(), age_var.get().strip(), address_var.get().strip())

def validate(name, age, address):
    if not (name and age and address):
        messagebox.showwarning("Input Error", "All fields are required.")
        return False
    if not age.isdigit():
        messagebox.showwarning("Input Error", "Age must be a number.")
        return False
    return True

def clear_fields():
    name_var.set("")
    age_var.set("")
    address_var.set("")

def on_row_selected(event):
    selected = tree.selection()
    if selected:
        values = tree.item(selected[0], "values")
        name_var.set(values[1])
        age_var.set(values[2])
        address_var.set(values[3])

# ---------- GUI ----------
init_db()

root = tb.Window(themename="superhero")
root.title("User Management System")
root.geometry("550x500")
root.resizable(False, False)

frame = tb.Frame(root, padding=15)
frame.pack(fill="both", expand=True)

tb.Label(frame, text="User Management System", font=("Arial", 16, "bold")).pack(pady=5)

# Inputs
input_frame = tb.Frame(frame, padding=10)
input_frame.pack(fill="x")

name_var = tb.StringVar()
age_var = tb.StringVar()
address_var = tb.StringVar()

labels = ["Name:", "Age:", "Address:"]
vars_ = [name_var, age_var, address_var]

for i, (label, var) in enumerate(zip(labels, vars_)):
    tb.Label(input_frame, text=label).grid(row=i, column=0, padx=5, pady=5, sticky="w")
    tb.Entry(input_frame, textvariable=var, width=30).grid(
        row=i, column=1, padx=5, pady=5
    )

# Buttons
btn_frame = tb.Frame(frame, padding=10)
btn_frame.pack(fill="x")

buttons = [
    ("Add", "success", add_user),
    ("Update", "info", update_user),
    ("Delete", "danger", delete_user),
    ("Clear", "secondary", clear_fields),
]

for i, (text, style, cmd) in enumerate(buttons):
    tb.Button(btn_frame, text=text, bootstyle=style, command=cmd).grid(
        row=0, column=i, padx=5, pady=5
    )

# Table
tree_frame = tb.Frame(frame, padding=10)
tree_frame.pack(fill="both", expand=True)

columns = ("ID", "Name", "Age", "Address")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.pack(fill="both", expand=True)
tree.bind("<ButtonRelease-1>", on_row_selected)

view_users()
root.mainloop()
