import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Welcome Application")
root.geometry("350x250")

label = tk.Label(
    root,
    text="Welcome to Python GUI",
    font=("Arial", 16)
)
label.pack(pady=15)


name_label = tk.Label(root, text="Enter your name:")
name_label.pack()


name_entry = tk.Entry(root)
name_entry.pack(pady=5)


def greet():
    name = name_entry.get()

    if name.strip() == "":
        messagebox.showwarning(
            "Warning", "Please enter your name"
        )
    else:
        messagebox.showinfo(
            "Welcome", "Hello, " + name + "!"
        )


button = tk.Button(
    root,
    text="Submit",
    command=greet
)
button.pack(pady=15)

root.mainloop()