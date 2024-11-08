# Custom Resume Builder

The **Custom Resume Builder** is a Python-based tool designed to simplify the process of creating professional resumes. By entering personal and professional details into an Excel sheet, users can automatically generate a customized resume in either Word or PDF format. This tool provides flexibility with custom themes, section visibility, and the option to add a profile picture, making it easy to create a resume tailored to specific job applications.

## Features

- **Input from Excel**:  
  Users can input their personal details (e.g., name, contact information), professional experience, skills, education, and achievements into an Excel sheet. This data is then used to populate the resume template automatically.

- **Template-based Resume Generation**:  
  The program allows users to choose between generating resumes in **Word** or **PDF** format. The data from the Excel sheet is inserted into a pre-designed template, which can be customized to match individual preferences.

- **Customizable Themes**:  
  The tool includes multiple resume themes. Users can select from a variety of styles that change the visual layout of the resume, including font choices, colors, and formatting. This ensures the resume fits the user's personal or professional preferences.

- **Section Visibility**:  
  Users can choose to **show** or **hide** specific sections of their resume (e.g., work experience, education, skills). This feature is useful for tailoring the resume to specific job roles or industries by highlighting only the most relevant information.

- **Profile Picture**:  
  The tool also allows users to include a **profile picture** in the resume, which can be added either by uploading a file from a local directory or using an image URL. This is particularly useful for creative professions or where visual presence is important.

## Libraries Used

The **Custom Resume Builder** utilizes the following Python libraries to handle the Excel input, template creation, and resume generation:

- **`openpyxl`**:  
  A library for reading and writing Excel files (`.xlsx`). It is used to import user data from the Excel sheet.

- **`docxtpl`**:  
  This library is used for generating Word documents by filling in the fields of a Word template with the data from the Excel sheet.

- **`reportlab`**:  
  This library allows for generating custom PDF files, providing full control over the document's layout and design.

## Requirements

Before using the **Custom Resume Builder**, you need to have the following installed on your system:

- **Python 3.x** (Python 3.6 or later recommended)
- **`openpyxl`**: For reading and writing Excel files.
- **`docxtpl`**: For Word document generation.
- **`reportlab`**: For creating PDF resumes.

You can install these dependencies by running:

```bash
pip install openpyxl docxtpl reportlab
