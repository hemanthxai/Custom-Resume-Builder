import tkinter as tk
from tkinter import ttk, messagebox
from openpyxl import Workbook
import openpyxl
from docxtpl import DocxTemplate
import os


# Function to save data to Excel and generate a resume
def save_and_generate_resume():
    # Collect data from the form
    data = {
        "Name": name_var.get(),
        "Phone Number": phone_var.get(),
        "Email": email_var.get(),
        "LinkedIn": linkedin_var.get(),
        "Location": location_var.get(),
        "Experience 1 - Role": exp1_role_var.get(),
        "Experience 1 - Duration": exp1_duration_var.get(),
        "Experience 1 - Description": exp1_desc_var.get(),
        "Experience 2 - Role": exp2_role_var.get(),
        "Experience 2 - Duration": exp2_duration_var.get(),
        "Experience 2 - Description": exp2_desc_var.get(),
        "Experience 3 - Role": exp3_role_var.get(),
        "Experience 3 - Duration": exp3_duration_var.get(),
        "Experience 3 - Description": exp3_desc_var.get(),
        "Project 1 - Title": proj1_title_var.get(),
        "Project 1 - Description": proj1_desc_var.get(),
        "Project 2 - Title": proj2_title_var.get(),
        "Project 2 - Description": proj2_desc_var.get(),
        "Project 3 - Title": proj3_title_var.get(),
        "Project 3 - Description": proj3_desc_var.get(),
        "Training/Certification 1": cert1_name_var.get(),
        "Provider 1": cert1_provider_var.get(),
        "Training/Certification 2": cert2_name_var.get(),
        "Provider 2": cert2_provider_var.get(),
        "Training/Certification 3": cert3_name_var.get(),
        "Provider 3": cert3_provider_var.get(),
        "Course": course_var.get(),
        "College": college_var.get(),
        "Duration": college_duration_var.get(),
        "CGPA": cgpa_var.get(),
    }

    # Save data to Excel
    output_path = r"C:/Users/heman/Desktop/Py/Custom Resume Builder/Custom-Resume-Builder/ResumeV2/output.xlsx"
    wb = Workbook()
    ws = wb.active
    headers = list(data.keys())
    ws.append(headers)
    ws.append(list(data.values()))
    wb.save(output_path)
    print("Data saved to output.xlsx")

    # Load Excel data for template rendering
    workbook = openpyxl.load_workbook(output_path)
    sheet = workbook.active
    list_values = list(sheet.values)

    doc_template_path = r"C:/Users/heman/Desktop/Py/Custom Resume Builder/Custom-Resume-Builder/ResumeV2/Resume.docx"
    doc = DocxTemplate(doc_template_path)

    for i in list_values[1:]:
        doc.render(
            {
                "Name": i[0],
                "PhoneNo": i[1],
                "Email": i[2],
                "LinkedIn": i[3],
                "Location": i[4],
                "About": i[5],
                "Skills": i[6],
                "ExpRole1": i[7],
                "ExpTime1": i[8],
                "ExpDesc1": i[9],
                "ExpRole2": i[10],
                "ExpTime2": i[11],
                "ExpDesc2": i[12],
                "ExpRole3": i[13],
                "ExpTime3": i[14],
                "ExpDesc3": i[15],
                "ProjectTitle1": i[16],
                "ProjectDesc1": i[17],
                "ProjectTitle2": i[18],
                "ProjectDesc2": i[19],
                "ProjectTitle3": i[20],
                "ProjectDesc3": i[21],
                "CertificateName": i[22],
                "CertificateProvider": i[23],
                "CourseDetails": i[24],
                "CollegeName": i[25],
                "CollegeDuration": i[26],
                "CGPA": i[27],
            }
        )

        # Save the generated document
        save_directory = r"C:/Users/heman/Desktop/Py/Custom Resume Builder/Custom-Resume-Builder/ResumeV2"
        doc_name = os.path.join(
            save_directory, f"Resume_{i[0] if i[0] else 'Unnamed'}.docx"
        )
        doc.save(doc_name)
        print(f"Document saved to {doc_name}")

    # Display success message and exit
    messagebox.showinfo("Success", "Resume generated successfully!")
    root.destroy()  # Close the window


# Create the main window
root = tk.Tk()
root.title("User Data Form")
root.geometry("600x800")  # Adjust size as needed

# Styling with ttk for better aesthetics
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 10))
style.configure("TEntry", font=("Helvetica", 10))

# Define StringVar for form fields
name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
linkedin_var = tk.StringVar()
location_var = tk.StringVar()
exp1_role_var = tk.StringVar()
exp1_duration_var = tk.StringVar()
exp1_desc_var = tk.StringVar()
exp2_role_var = tk.StringVar()
exp2_duration_var = tk.StringVar()
exp2_desc_var = tk.StringVar()
exp3_role_var = tk.StringVar()
exp3_duration_var = tk.StringVar()
exp3_desc_var = tk.StringVar()
proj1_title_var = tk.StringVar()
proj1_desc_var = tk.StringVar()
proj2_title_var = tk.StringVar()
proj2_desc_var = tk.StringVar()
proj3_title_var = tk.StringVar()
proj3_desc_var = tk.StringVar()
cert1_name_var = tk.StringVar()
cert1_provider_var = tk.StringVar()
cert2_name_var = tk.StringVar()
cert2_provider_var = tk.StringVar()
cert3_name_var = tk.StringVar()
cert3_provider_var = tk.StringVar()
course_var = tk.StringVar()
college_var = tk.StringVar()
college_duration_var = tk.StringVar()
cgpa_var = tk.StringVar()

# Create and place the form fields
fields = [
    ("Name", name_var),
    ("Phone Number", phone_var),
    ("Email", email_var),
    ("LinkedIn", linkedin_var),
    ("Location", location_var),
    ("Experience 1 - Role", exp1_role_var),
    ("Experience 1 - Duration", exp1_duration_var),
    ("Experience 1 - Description", exp1_desc_var),
    ("Experience 2 - Role", exp2_role_var),
    ("Experience 2 - Duration", exp2_duration_var),
    ("Experience 2 - Description", exp2_desc_var),
    ("Experience 3 - Role", exp3_role_var),
    ("Experience 3 - Duration", exp3_duration_var),
    ("Experience 3 - Description", exp3_desc_var),
    ("Project 1 - Title", proj1_title_var),
    ("Project 1 - Description", proj1_desc_var),
    ("Project 2 - Title", proj2_title_var),
    ("Project 2 - Description", proj2_desc_var),
    ("Project 3 - Title", proj3_title_var),
    ("Project 3 - Description", proj3_desc_var),
    ("Training/Certification 1", cert1_name_var),
    ("Provider 1", cert1_provider_var),
    ("Training/Certification 2", cert2_name_var),
    ("Provider 2", cert2_provider_var),
    ("Training/Certification 3", cert3_name_var),
    ("Provider 3", cert3_provider_var),
    ("Course", course_var),
    ("College", college_var),
    ("College Duration", college_duration_var),
    ("CGPA", cgpa_var),
]

row = 0
for label_text, var in fields:
    ttk.Label(root, text=label_text).grid(
        row=row, column=0, sticky=tk.W, padx=10, pady=2
    )
    ttk.Entry(root, textvariable=var, width=40).grid(row=row, column=1, padx=10, pady=2)
    row += 1

# Add a save button
ttk.Button(root, text="Generate Resume", command=save_and_generate_resume).grid(
    row=row, column=1, pady=10
)

# Run the main loop
root.mainloop()
