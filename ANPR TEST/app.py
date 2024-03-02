import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from yolo_detect import YOLOModel
from classify_class import ClassificationModel
from actions import add_image, add_license_image, run_image_detection, start_detection,add_video,stop_video,add_live_video

left_frame_color = "#1e1e1e"
right_frame_color = "#d0d0d0"
down_frame_color = "#8f8f8f"
navbar_color = "black"

file_path = ""

# Define global variables
down_frame = None
right_canvas = None 

# Add lists to store down canvases and labels
down_canvases = []
down_labels = []

#####_______________FUNCTIONS_________________#####
#? Adding new frame
def add_frame(container, frames, frame_func, frame_name):
    frame = frame_func(container)
    frames[frame_name] = frame
    # Configure row and column weights to make the frame expandable
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)
    # Use grid to make the frame take full width and height
    frame.grid(row=0, column=0, sticky="nsew")

#? Showing the required frame
def show_frame(frames, frame_name):
    frame = frames[frame_name]
    frame.tkraise()
    
#? Detect from image frame
def ObjectDetectionPage(parent):
    global down_frame, down_canvases, down_labels, right_canvas
    
    root = tk.Frame(parent, bg='blue')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Left Frame
    left_frame = tk.Frame(root, bg=left_frame_color)
    left_frame.grid(row=0, column=0, sticky="nsew")

    # Right Frame
    right_frame = tk.Frame(root, bg=right_frame_color)
    right_frame.grid(row=0, column=1, sticky="nsew")
    
    # Configure row and column weights for resizing
    root.grid_columnconfigure(0, weight=2)
    root.grid_columnconfigure(1, weight=7)
    
    ## * In the right frame
    # Down Frame
    down_frame = tk.Frame(right_frame, bg=down_frame_color,height=90,)
    down_frame.pack(side="bottom", fill="x")

    # Add canvas to the right frame
    right_canvas = tk.Canvas(right_frame, bg="#d0d0d0", width=640, height=640)
    right_canvas.pack(padx=15, pady=10, side="left")
    
    right_right_frame = tk.Frame(right_frame, bg="green",width=400)
    right_right_frame.pack(side="right", fill="y")
    
    
    #_________comtents of left frame____________________#

    # Add content to left frame
    tk.Label(left_frame, text="Choose option", fg="white", bg=left_frame_color, font=("Arial", 17)).pack(pady=10)

    # Add buttons to the left frame
    label1 = tk.Label(left_frame, text="Choose Image", font=("Arial", 10), fg="white", bg=left_frame_color)
    btn1 = tk.Button(left_frame, text="Button 1", command=lambda: add_image(right_canvas), width=20, height=1)
    
    label3 = tk.Label(left_frame, text="Run detection model", font=("Arial", 10), bg=left_frame_color, fg="white")
    btn3 = tk.Button(left_frame, text="Detect", command=lambda: run_image_detection(down_canvases, down_labels, down_frame, right_canvas), width=20)

    # Pack widgets in left frame
    label1.pack(pady=5)
    btn1.pack(pady=5)
    label3.pack(pady=5)
    btn3.pack(pady=5)
    
    return root


#? Detect from video frame
def VideoObjectDetectionPage(parent):
    root = tk.Frame(parent, bg="blue")
    
    ##?__________________LAYOUT SETUP___________________##
    
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=6)
    root.grid_rowconfigure(2, weight=4)
    
    root.grid_columnconfigure(0, weight=3)
    root.grid_columnconfigure(1, weight=7)
    
    option_frame = tk.Frame(root, bg="green",height=90)
    option_frame.grid(row=0,columnspan=2,sticky="nsew")
    
    live_frame = tk.Frame(root, bg ="yellow")
    live_frame.grid(row=1,column=0,sticky="nsew")
    
    live_canvas = tk.Canvas(live_frame, bg="yellow", width=350, height=350)
    live_canvas.place(x=15,y=30) 

    show_detected_frame = tk.Frame(root, bg="orange")
    show_detected_frame.grid(row=2,column=0,sticky="nsew")
    
    captured_frame = tk.Frame(root, bg="purple")
    captured_frame.grid(row=1,column=1,sticky="nsew")
    
    table_frame = tk.Frame(root, bg="pink")
    table_frame.grid(row=2,column=1,sticky="nsew")
    
    ##?_________________________ADDING ITEMS TO THE FRAMES_______________________##
    
    #? Option Frame
    video_choose_btn = tk.Button(option_frame, text="Choose Video", command=lambda: add_video(live_canvas), bg="black", fg="white")
    video_choose_btn.pack(padx=10,side="left")
 
    entry_label = tk.Label(option_frame, text="RTSP address:", bg="green")
    entry_label.pack(padx=10,side="left")
    # Add entry widget to the option frame
    entry_widget = tk.Entry(option_frame,width=60, bg="white")
    entry_widget.pack(padx=10,side='left')
    
    show_live_btn = tk.Button(option_frame, text="Show Live", command=lambda: add_live_video(entry_widget.get(),live_canvas), bg="black", fg="white")
    show_live_btn.pack(padx=10,side="left")
    
    stop_frame_btn = tk.Button(option_frame, text="Stop", command=lambda :stop_video(live_canvas), bg="black", fg="white")
    stop_frame_btn.pack(padx=5,side='left')
    
    start_detection_btn = tk.Button(option_frame, text="Start Detection", command=lambda: start_detection(show_detected_frame,live_canvas), bg="black", fg="white")
    start_detection_btn.pack(padx=5,side='left')
    
    return root
  
#########_________________________________________#########
def create_ui(root):    
     #?NAVBAR______ Top Frame (full width, height=50)
    top_frame = tk.Frame(root, bg=navbar_color, height=30)
    top_frame.pack(fill="x")
    
    # Create navigation buttons
    btn_object_detection = tk.Button(top_frame, text="Object Detection", command=lambda: show_frame(frames, "ObjectDetectionPage"),bg='black',fg='white')
    btn_object_detection.pack(side="left", padx=5, pady=5)
    btn_video_detection = tk.Button(top_frame, text="Video Detection", command=lambda: show_frame(frames, "VideoObjectDetectionPage"),bg='black', fg='white')
    btn_video_detection.pack(side="left", padx=5, pady=5)
    
    ##______________________NAVAR END AREA______________________#####
    #######_______________________ROUTING______________________##########
    ##? container frame
    container = tk.Frame(root)
    container.pack(fill="both", expand=True)
    
    ##? Dictionary to hold different frames
    frames = {}
    
    ##? Initialize and add frames to the container
    add_frame(container, frames, ObjectDetectionPage, "ObjectDetectionPage")
    add_frame(container, frames, VideoObjectDetectionPage, "VideoObjectDetectionPage")
    
    
    #####_______________________ROUTING END_______________________#####

    ## ? Show the first frame
    show_frame(frames, "VideoObjectDetectionPage")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tkinter UI with Sections")
    
    print("Loading YOLO model...")
    model = YOLOModel()
    print("YOLO model loaded successfully")
    
    print("Loading classification model...")
    classification_model = ClassificationModel()
    print("Classification model loaded successfully")

    

    create_ui(root)
    
    root.mainloop()

