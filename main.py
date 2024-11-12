import tkinter as tk


root = tk.Tk()
root.title("Custom Resume Builder")
root.configure(bg="black")


fields = ["Full Name", "Phone", "Email", "Location"]
entries = {}

for field in fields:
    label = tk.Label(root, text=field, fg="white", bg="black", font=("Arial", 12))
    label.pack(anchor="w", padx=10, pady=2)
    entry = tk.Entry(root, bg="gray", fg="white", font=("Arial", 12), width=50)
    entry.pack(anchor="w", padx=10, pady=2)
    entries[field] = entry

root.mainloop()
