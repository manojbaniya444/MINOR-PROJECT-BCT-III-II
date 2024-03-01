import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from actions import add_image, add_license_image, run_image_detection

left_frame_color = "lightblue"
right_frame_color = "lightgreen"
down_frame_color = "lightcoral"
navbar_color = "lightgrey"

file_path = ""

# Define global variables
down_frame = None
right_canvas = None 

# Add lists to store down canvases and labels
down_canvases = []
down_labels = []


def create_ui(root):
    global down_frame, down_canvases, down_labels, right_canvas
    # Top Frame (full width, height=50)
    top_frame = tk.Frame(root, bg=navbar_color, height=30)
    top_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

    # Left Frame (1/6 width)
    left_frame = tk.Frame(root, bg=left_frame_color)
    left_frame.grid(row=1, column=0, sticky="nsew")

    # Right Frame (5/6 width)
    right_frame = tk.Frame(root, bg=right_frame_color)
    right_frame.grid(row=1, column=1, sticky="nsew")

    # Down Frame (1/5 of the total height)
    down_frame = tk.Frame(root, bg=down_frame_color, height=90)
    down_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")

    # Configure row and column weights for resizing
    root.grid_rowconfigure(0, weight=1)  # 1/8 of the total height
    root.grid_rowconfigure(1, weight=5)  # 5/8 of the total height
    root.grid_rowconfigure(2, weight=2)  # 2/8 of the total height
    root.grid_columnconfigure(0, weight=1)  # 1/6 of the total width
    root.grid_columnconfigure(1, weight=5)  # 5/6 of the total width
    
    # Add canvas to the right frame
    right_canvas = tk.Canvas(right_frame, bg="white", width=640, height=640)
    right_canvas.pack(padx=10, pady=10)

    # Add content to top frame (navbar)
    # tk.Label(top_frame, text="Navbar", bg=navbar_color, font=("Arial", 14)).pack(pady=10)

    # Add content to frames (optional)
    tk.Label(left_frame, text="Choose option", bg=left_frame_color, font=("Arial", 17)).pack(pady=10)

    # Add buttons to the left frame
    label1 = tk.Label(left_frame, text="Choose Image", font=("Arial", 10), bg=left_frame_color)
    btn1 = tk.Button(left_frame, text="Button 1", command=lambda: add_image(right_canvas), width=15, height=1)

    label2 = tk.Label(left_frame, text="Add license image", font=("Arial", 10), bg=left_frame_color)
    btn2 = tk.Button(left_frame, text="Button 2", command=lambda: add_license_image(down_canvases,down_labels,down_frame,None), width=15, height=1)
    
    label3 = tk.Label(left_frame, text="Run detection model", font=("Arial", 10), bg=left_frame_color)
    btn3 = tk.Button(left_frame, text="Detect", command=lambda: run_image_detection(down_canvases, down_labels, down_frame))

    # packing left frame
    label1.pack(pady=5)
    btn1.pack(pady=5)
    label2.pack(pady=5)
    btn2.pack(pady=5)
    label3.pack(pady=5)
    btn3.pack(pady=5)
    
    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tkinter UI with Sections")

    create_ui(root)
    
    root.mainloop()

