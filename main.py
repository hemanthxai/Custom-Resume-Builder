import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


def select_photo():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]
    )
    if file_path:
        img = Image.open(file_path)
        img = img.resize((150, 150))
        img_tk = ImageTk.PhotoImage(img)
        photo_label.config(image=img_tk)
        photo_label.image = img_tk


root = tk.Tk()
root.title("Custom Resume Builder")
root.configure(bg="black")


photo_button = tk.Button(
    root, text="Select Profile Photo", command=select_photo, bg="#444", fg="white"
)
photo_button.pack(pady=5)

photo_label = tk.Label(root, bg="black")
photo_label.pack(pady=5)

root.mainloop()
