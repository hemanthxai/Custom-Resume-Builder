# directory_setup.py
import tkinter as tk
from tkinter import ttk
from openpyxl import Workbook
from docxtpl import DocxTemplate
import os


def save_to_excel():
    data = {
        "Name": name_var.get(),
        "Phone Number": phone_var.get(),
        "Email": email_var.get(),
    }

    wb = Workbook()
    ws = wb.active
    headers = list(data.keys())
    ws.append(headers)
    ws.append(list(data.values()))
    wb.save("output.xlsx")


def generate_resume():
    save_directory = "C:/Users/heman/Desktop/ResumeV2"
    os.makedirs(save_directory, exist_ok=True)
    doc = DocxTemplate("ResumeTemplate.docx")
    doc.render(
        {
            "Name": name_var.get(),
            "PhoneNo": phone_var.get(),
            "Email": email_var.get(),
        }
    )
    doc.save(f"{save_directory}/Resume_{name_var.get()}.docx")
    print("Resume generated successfully!")


root = tk.Tk()
root.title("User Data Form")

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
    tk.Label(root, text=label_text, font=("Arial", 12)).grid(
        row=row, column=0, sticky=tk.W, padx=10, pady=2
    )
    tk.Entry(root, textvariable=var, width=40, font=("Arial", 12)).grid(
        row=row, column=1, padx=10, pady=2
    )
    row += 1

ttk.Button(root, text="Save to Excel", command=save_to_excel).grid(
    row=row, column=0, pady=10
)
ttk.Button(root, text="Generate Resume", command=generate_resume).grid(
    row=row, column=1, pady=10
)

root.mainloop()
