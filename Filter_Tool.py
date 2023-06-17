import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter

root = tk.Tk()
root.geometry("1000x600")
root.resizable(width=False, height=False)
root.title("Image Filters Tool")

left_frame = tk.Frame(root, width=200, height=600, bg="white")
left_frame.pack(side="left", fill="y")
left_frame.pack_propagate(0)

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(side="right", fill="both", expand=True)

file_path = ""


def add_image():
    global file_path
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    image = image.resize((600, int((image.height / image.width) * 600)))
    tkimage = ImageTk.PhotoImage(image)
    canvas.image = tkimage
    canvas.create_image(0, 0, image=tkimage, anchor="nw")


image_button = tk.Button(left_frame, text="Add Image", command=add_image)
image_button.pack(pady=15)


def Apply_filter(filter):
    image = Image.open(file_path)
    image = image.resize((600, int((image.height / image.width) * 600)))
    filtered_image = image.filter(filter)
    tkimage = ImageTk.PhotoImage(filtered_image)
    canvas.image = tkimage
    canvas.create_image(0, 0, image=tkimage, anchor="nw")


def selection_changed(event):
    selection = combo.get()
    print(selection)
    if selection == "Blur":
        Apply_filter(ImageFilter.BLUR)
    if selection == "Smooth":
        Apply_filter(ImageFilter.SMOOTH)
    if selection == "Sharpen":
        Apply_filter(ImageFilter.SHARPEN)
    if selection == "GrayScale":
        image = Image.open(file_path)
        image = image.resize((600, int((image.height / image.width) * 600)))
        filtered_image = image.convert("L")
        tkimage = ImageTk.PhotoImage(filtered_image)
        canvas.image = tkimage
        canvas.create_image(0, 0, image=tkimage, anchor="nw")


combo = ttk.Combobox(
    values=["Blur", "Smooth", "Sharpen", "GrayScale"], state="readonly"
)
combo.bind("<<ComboboxSelected>>", selection_changed)
combo.place(x=30, y=50)


root.mainloop()
