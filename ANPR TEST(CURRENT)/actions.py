import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

left_frame_color = "lightblue"
right_frame_color = "lightgreen"
down_frame_color = "lightcoral"
navbar_color = "lightgrey"

down_canvases = []
down_labels = []

def add_image(right_canvas): # right_canvass
    file_path = filedialog.askopenfilename(initialdir='D:\Learn Python\tkinter\Image_editing_tool\images')
    image = Image.open(file_path)
    width, height = 640, 640
    image = image.resize((width, height), Image.LANCZOS)
    right_canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    right_canvas.image = image
    right_canvas.create_image(0, 0, image=image, anchor='nw')

def add_license_image(down_canvases, down_labels, down_frame): # down_canvas
    file_path = filedialog.askopenfilename(initialdir='D:\Learn Python\tkinter\Image_editing_tool\images')
    image = Image.open(file_path)
    width, height = 200, 50
    image = image.resize((width, height), Image.LANCZOS)

    # Create a new canvas and label for each call
    if len(down_canvases) == 5:
        # Remove all canvases and labels if there are already 5
        for canvas, label in zip(down_canvases, down_labels):
            canvas.destroy()
            label.destroy()
        down_canvases.clear()
        down_labels.clear()

    # Calculate the index for placing the new canvas
    index = len(down_canvases)

    # Create a label for the new canvas
    label_text = f"CanvasDown {index + 1}"
    canvas_label = tk.Label(down_frame, text=label_text, font=("Arial", 10), bg=down_frame_color)
    canvas_label.grid(row=0, column=index, padx=10, pady=5)

    # Create a new canvas and store it in the list
    canvas = tk.Canvas(down_frame, bg="white", width=200, height=50)
    canvas.grid(row=1, column=index, padx=5, pady=5)
    down_canvases.append(canvas)
    down_labels.append(canvas_label)

    # Configure column weights for equal horizontal distribution
    for i in range(len(down_canvases)):
        down_frame.grid_columnconfigure(i, weight=1)

    # Set the image on the new canvas
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor='nw')