# Custom Resume Builder Using Python

This project consists of two Python applications for building customized resumes. One generates a resume in HTML format, and the other generates a resume in DOCX format by using user inputs, saving the data in an Excel file, and creating the resume using a template.

# Project 1: HTML Resume Generator

## Features:
- A simple GUI built using Tkinter.
- User can enter their personal details, professional summary, skills, education, experience, and more.
- Allows the user to upload a profile picture.
- Generates a clean HTML file that can be opened in a web browser.

## How to Use:
1. Run the `html_resume.py` script.
2. Fill in the form with your details.
3. Click on "Select Profile Photo" to upload a picture.
4. Click "Generate HTML Resume" to create the resume.

## Dependencies:
- `tkinter` (for GUI)
- `Pillow` (for image handling)

Install them using:
pip install tkinter pillow




# Project 2: DOCX Resume Generator (ResumeV2)

This project allows users to generate personalized resumes in DOCX format. It involves entering user details via a simple form, saving the information to an Excel file, and then generating the resume using a pre-designed DOCX template.

## Features:
- A form where users can input their resume data, including personal information, experience, education, certifications, and projects.
- Data is saved in an Excel file (`output.xlsx`), which can be used for future reference or updates.
- Uses a DOCX template to generate the resume, with placeholders replaced by user data.
- The generated resume is saved as a DOCX file for each user.

## How to Use:
1. Run the `resume_v2.py` script.
2. Fill in the form with your details, including personal information, experience, education, projects, and certifications.
3. After filling the form, click the "Generate Resume" button.
4. The data will be saved to an Excel file (`output.xlsx`), and the DOCX resume will be generated and saved as a new file.

## Dependencies:
- `tkinter` (for GUI)
- `openpyxl` (for Excel file handling)
- `docxtpl` (for DOCX file generation)

Install the dependencies using:
pip install tkinter openpyxl docxtpl




# Disclaimer

Please make sure to **UPDATE THE FILE PATHS** in the scripts before running the project. The default paths in the code may not work on your system, so you need to specify the correct paths for files such as the **profile picture**, **template DOCX**, **Excel file**, and the **output paths** for both the HTML and DOCX resume files.

Ensure that you modify the file paths in the following files:
- `html_resume.py` (for the HTML resume generator)
- `resume_v2.py` (for the DOCX resume generator)

Failing to update the paths may lead to errors or incorrect file handling.

