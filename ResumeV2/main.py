import tkinter as tk

root = tk.Tk()
root.title("Resume Builder")

name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()

fields = [
    ("Name", name_var),
    ("Phone Number", phone_var),
    ("Email", email_var),
]

row = 0
for label_text, var in fields:
    tk.Label(root, text=label_text).grid(
        row=row, column=0, sticky=tk.W, padx=10, pady=2
    )
    tk.Entry(root, textvariable=var, width=40).grid(row=row, column=1, padx=10, pady=2)
    row += 1

root.mainloop()
