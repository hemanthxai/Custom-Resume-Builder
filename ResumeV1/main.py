import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageOps
import os


# Function to select a profile photo
def select_photo():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]
    )
    if file_path:
        photo_path.set(file_path)
        img = Image.open(file_path)
        img = img.resize((150, 150))
        img = ImageOps.fit(img, (150, 150))
        img_tk = ImageTk.PhotoImage(img)
        photo_label.config(image=img_tk)
        photo_label.image = img_tk


# Function to generate the HTML resume
def generate_html_resume(data, photo_path):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Resume</title>
        <style>
            body {{ font-family: 'Arial', sans-serif; background-color: white; color: black; margin: 20px; }}
            .container {{ max-width: 800px; margin: auto; padding: 20px; }}
            .header {{ display: flex; align-items: center; margin-bottom: 20px; }}
            .photo img {{ width: 150px; border-radius: 50%; margin-right: 20px; }}
            .details {{ line-height: 1.6; }}
            h1, h2 {{ margin: 0; color: black; }}
            p, ul {{ color: black; }}
            .section {{ margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="photo">
                    <img src="{photo_path}" alt="Profile Photo">
                </div>
                <div class="details">
                    <h1>{data['full_name']}</h1>
                    <p>{data['phone']} • {data['email']} • {data['location']}<br>
                    <a href="{data['linkedin']}" style="color: #00ffcc;">{data['linkedin']}</a></p>
                </div>
            </div>
            <br>
            <hr style="border: 1px solid black;">
            <br>
            <div class="section">
                <h2>Professional Summary</h2>
                <p>{data['summary']}</p>
            </div>
            <br>
            <hr style="border: 1px solid black;">
            <br>
            <div class="section">
                <h2>Skills</h2>
                <p>{data['skills']}</p>
            </div>
            <br>
            <hr style="border: 1px solid black;">
            <br>
            <div class="section">
                <h2>Education</h2>
                <p>{data['education']}</p>
            </div>
            <br>
            <hr style="border: 1px solid black;">
            <br>
            <div class="section">
                <h2>Professional Experience</h2>
                <p>{data['experience']}</p>
            </div>
            <br>
            <hr style="border: 1px solid black;">
            <br>
            <div class="section">
                <h2>Certifications</h2>
                <p>{data['certifications']}</p>
            </div>
            <br>
            <hr style="border: 1px solid black;">
            <br>
            <div class="section">
                <h2>Projects</h2>
                <p>{data['projects']}</p>
            </div>
            <br>
            <hr style="border: 1px solid black;">
            <br>
            <div class="section">
                <h2>Interests</h2>
                <p>{data['interests']}</p>
            </div>
        </div>
    </body>
    </html>
    """
    # Save the HTML to a file
    with open("resume.html", "w", encoding="utf-8") as file:
        file.write(html_content)
    messagebox.showinfo("Success", "HTML resume created successfully!")


# Create the Tkinter GUI
root = tk.Tk()
root.title("Custom Resume Builder")
root.configure(bg="black")

# Photo path variable
photo_path = tk.StringVar()

# Create labels and entry widgets for each field
fields = [
    ("Full Name", "full_name"),
    ("Phone", "phone"),
    ("Email", "email"),
    ("Location", "location"),
    ("LinkedIn Profile", "linkedin"),
    ("Professional Summary", "summary"),
    ("Skills", "skills"),
    ("Education", "education"),
    ("Professional Experience", "experience"),
    ("Certifications", "certifications"),
    ("Projects", "projects"),
    ("Interests", "interests"),
]

entries = {}
for label_text, field_name in fields:
    label = tk.Label(root, text=label_text, fg="white", bg="black", font=("Arial", 12))
    label.pack(anchor="w", padx=10, pady=2)
    entry = tk.Entry(
        root,
        textvariable=tk.StringVar(),
        bg="gray",
        fg="white",
        font=("Arial", 12),
        width=50,
    )
    entry.pack(anchor="w", padx=10, pady=2)
    entries[field_name] = entry

# Button to select a photo
photo_button = tk.Button(
    root, text="Select Profile Photo", command=select_photo, bg="#444", fg="white"
)
photo_button.pack(pady=5)

photo_label = tk.Label(root, bg="black")
photo_label.pack(pady=5)

# Button to generate the resume
generate_button = tk.Button(
    root,
    text="Generate HTML Resume",
    command=lambda: generate_resume(),
    bg="#00ffcc",
    fg="black",
)
generate_button.pack(pady=10)


# Function to collect data and generate a resume
def generate_resume():
    data = {field_name: entry.get() for field_name, entry in entries.items()}
    if not any(data.values()):
        messagebox.showwarning("Input Error", "Please fill in at least one field!")
        return

    # Check if a photo is selected
    selected_photo = photo_path.get()
    if not selected_photo:
        messagebox.showwarning("Input Error", "Please select a profile photo.")
        return

    # Generate the HTML resume
    generate_html_resume(data, selected_photo)


root.mainloop()
