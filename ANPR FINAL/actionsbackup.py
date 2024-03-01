import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

from yolo_detect import YOLOModel
from utils import get_license_plate_coordinates

left_frame_color = "lightblue"
right_frame_color = "lightgreen"
down_frame_color = "lightcoral"
navbar_color = "lightgrey"

# Image on the right canvas which is to be detected.
image_to_detect = None
image_to_detect_file = ""

def add_image(right_canvas, detected_image=None):
    global image_to_detect, image_to_detect_file
    
    
    
    # Show the image: detected_image if provided, else the original image
    if detected_image is not None:
        # Clear the existing content on the canvas
        right_canvas.delete("all")
        
        right_canvas.detected_image = detected_image
        right_canvas.create_image(0, 0, image=detected_image, anchor='nw')
        
    else:
        # Clear the existing content on the canvas
        right_canvas.delete("all")     
        
        image_to_detect_file = filedialog.askopenfilename(initialdir='D:\Learn Python\tkinter\Image_editing_tool\images')
        image = Image.open(image_to_detect_file)
        width, height = 640, 640
        image = image.resize((width, height), Image.LANCZOS)
        image_to_detect = ImageTk.PhotoImage(image)
        right_canvas.image_to_detect = image_to_detect
        right_canvas.create_image(0, 0, image=image_to_detect, anchor='nw')

def add_license_image(down_canvases, down_labels, down_frame, detected_image=None):
    # Create a new canvas and label for each call
    if detected_image is None:
        print("No image to add to the down frame.")
        # Create a label for the new canvas
        label_text = f"No license plate found."
        canvas_label = tk.Label(down_frame, text=label_text, font=("Arial", 10), bg=down_frame_color)
        canvas_label.grid(row=0, column=index, padx=10, pady=5)
        return
    
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
    canvas = tk.Canvas(down_frame, bg="white", width=200, height=70)
    canvas.grid(row=1, column=index, padx=5, pady=5)
    down_canvases.append(canvas)
    down_labels.append(canvas_label)

    # Configure column weights for equal horizontal distribution
    for i in range(len(down_canvases)):
        down_frame.grid_columnconfigure(i, weight=1)

    # Set the image on the new canvas
    # Resize the detected image
    canvas.image = detected_image
    canvas.create_image(0, 0, image=detected_image, anchor='nw')

def run_image_detection(down_canvases, down_labels, down_frame, right_canvas):
    model = YOLOModel()
    if image_to_detect is not None:
        print("Running detection on the image.")
        
        img_to_yolo = cv2.imread(image_to_detect_file)
        img_to_yolo = cv2.cvtColor(img_to_yolo, cv2.COLOR_BGR2RGB)
        
        results = model.predict(img_to_yolo)
        
        # Check if any detection has confidence greater than 70 percent
        if any(conf > 0.5 for result in results for conf in result.boxes.conf.float().cpu().tolist()):
            # Visualize the results on the image
            for result in results:
                annotated_image = result.plot()
                # ?Here the annotated image is in BGR format so converting it to RGB to supply to tkinter
                # annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
                # For tkinter supporting image
                annotated_image = cv2.resize(annotated_image, (640, 640))
                img = Image.fromarray(annotated_image)
                img = ImageTk.PhotoImage(image=img)
                # cv2.imshow("Result", annotated_image)
                add_image(right_canvas, img)
                
                # get license plate coordinates
                license_coordinates = get_license_plate_coordinates(results)
                
                if license_coordinates is not None:
                    x1,y1,x2,y2 = license_coordinates
                
                    # crop the license plate
                    cropped_license_plate = img_to_yolo[int(y1):int(y2), int(x1):int(x2)]
                    resized_cropped_license_plate = cv2.resize(cropped_license_plate, (200, 70))
                    # cv2.imshow("License Plate", cropped_license_plate)
                
                    # pass the cropped license plate to add_license_image
                    license_plate = Image.fromarray(resized_cropped_license_plate)
                    license_plate = ImageTk.PhotoImage(image=license_plate)
                    add_license_image(down_canvases, down_labels, down_frame, license_plate)
                else:
                    print("No license plate found.")
            print("Detection completed.")
                       
    else:
        print("Please select an image first to detect.")