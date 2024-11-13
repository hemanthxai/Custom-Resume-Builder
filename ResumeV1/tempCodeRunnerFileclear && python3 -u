import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageOps


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
                    <p>{data['phone']} • {data['email']} • {data['location']}</p>
                </div>
            </div>
            <div class="section">
                <h2>Professional Summary</h2>
                <p>{data['summary']}</p>
            </div>
        </div>
    </body>
    </html>
    """
    with open("resume.html", "w", encoding="utf-8") as file:
        file.write(html_content)
    messagebox.showinfo("Success", "HTML resume created successfully!")


def generate_resume():
    data = {field: entry.get() for field, entry in entries.items()}
    selected_photo = photo_path.get()
    if not selected_photo or not any(data.values()):
        messagebox.showwarning(
            "Input Error", "Please fill in all fields and select a photo."
        )
        return
    generate_html_resume(data, selected_photo)


root = tk.Tk()
root.title("Custom Resume Builder")
root.configure(bg="black")

fields = [
    ("Full Name", "full_name"),
    ("Phone", "phone"),
    ("Email", "email"),
    ("Location", "location"),
    ("Summary", "summary"),
]

entries = {}
photo_path = tk.StringVar()

for label, var_name in fields:
    tk.Label(root, text=label, fg="white", bg="black", font=("Arial", 12)).pack(
        anchor="w", padx=10, pady=2
    )
    entry = tk.Entry(root, bg="gray", fg="white", font=("Arial", 12), width=50)
    entry.pack(anchor="w", padx=10, pady=2)
    entries[var_name] = entry

photo_button = tk.Button(
    root, text="Select Profile Photo", command=select_photo, bg="#444", fg="white"
)
photo_button.pack(pady=5)

photo_label = tk.Label(root, bg="black")
photo_label.pack(pady=5)

generate_button = tk.Button(
    root, text="Generate HTML Resume", command=generate_resume, bg="#00ffcc", fg="black"
)
generate_button.pack(pady=10)

root.mainloop()
