
import tkinter as tk
from tkinter import *
import cv2
import csv
import os
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time

# Window is our Main frame of system
window = tk.Tk()
window.title("FAMS-Face Recognition Based Attendance Management System")

window.geometry('1280x720')
window.configure(background='grey80')

# Queue for thread communication
q = queue.Queue()

def take_img():
    try:
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Assuming 'Id' and 'name' are generated/available before this function call
            Id = "1"  # Replace with actual logic
            name = "user"  # Replace with actual logic
            if not os.path.exists("C:\\Users\\srina\\OneDrive\\Desktop\\vscode\\fams\\TrainingImage"):
                os.makedirs("C:\\Users\\srina\\OneDrive\\Desktop\\vscode\\fams\\TrainingImage")
            cv2.imwrite(f"C:\\Users\\srina\\OneDrive\\Desktop\\vscode\\fams\\TrainingImage\{name}.{Id}.jpg", gray)
            q.put("Image Saved for Enrollment")
        else:
            q.put("Failed to capture image")
        cam.release()
    except Exception as e:
        q.put(f"Error: {e}")

def process_queue():
    try:
        msg = q.get_nowait()
        print(msg)
    except queue.Empty:
        window.after(100, process_queue)

def start_capture():
    threading.Thread(target=take_img).start()
    window.after(100, process_queue)

# Example button to start capture
capture_button = Button(window, text="Capture Image", command=start_capture)
capture_button.pack()

window.mainloop()
