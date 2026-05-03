import tkinter as tk


# ---------- Functions ----------
def press(value):
    """Handle number/operator button press"""
    current = expression_label["text"]
    expression_label.config(text=current + str(value))


def equalpress():
    """Calculate the result of the expression"""
    try:
        expr = expression_label["text"]
        result = str(eval(expr))
        result_label.config(text="= " + result)
    except Exception:
        result_label.config(text="Error")


def clear():
    """Clear expression and result"""
    expression_label.config(text="")
    result_label.config(text="")


# ---------- GUI Setup ----------
root = tk.Tk()
root.title("Improved Calculator")
root.geometry("450x450")
root.config(bg="white")
root.resizable(False, False)

# Expression display
expression_label = tk.Label(
    root, text="", anchor="e", bg="white", fg="black", font=("Arial", 22), height=2
)
expression_label.pack(fill="both")

# Result display
result_label = tk.Label(
    root, text="", anchor="e", bg="white", fg="green", font=("Arial", 20), height=1
)
result_label.pack(fill="both")

# ---------- Buttons ----------
button_frame = tk.Frame(root, bg="white")
button_frame.pack()

# Button layout: (text, row, column, optional colspan)
buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("C", 4, 2),
    ("+", 4, 3),
    ("=", 5, 0, 4),
]

for (text, row, col, *span) in buttons:
    colspan = span[0] if span else 1
    if text == "=":
        btn = tk.Button(
            button_frame,
            text=text,
            width=32,
            height=2,
            font=("Arial", 14),
            bg="#00b894",
            fg="white",
            command=equalpress,
        )
    elif text == "C":
        btn = tk.Button(
            button_frame,
            text=text,
            width=8,
            height=2,
            font=("Arial", 14),
            bg="#d63031",
            fg="white",
            command=clear,
        )
    else:
        btn = tk.Button(
            button_frame,
            text=text,
            width=8,
            height=2,
            font=("Arial", 14),
            bg="#dfe6e9",
            command=lambda val=text: press(val),
        )
    btn.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2)

# ---------- Run GUI ----------
root.mainloop()
