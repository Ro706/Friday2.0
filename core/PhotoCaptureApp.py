import cv2
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class PhotoCaptureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Capture")
        self.root.geometry("800x600")
        self.root.configure(bg='black')
        
        self.video_label = tk.Label(self.root, bg='black')
        self.video_label.pack()
        
        self.capture_button = tk.Button(self.root, text="Capture Photo", command=self.capture_photo)
        self.capture_button.pack(pady=10)
        
        self.cap = cv2.VideoCapture(0)
        self.show_video()
    
    def show_video(self):
        ret, frame = self.cap.read()
        if ret:
            # Convert the frame to an image
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)
        
        # Repeat the function after 10 milliseconds
        self.root.after(10, self.show_video)
    
    def capture_photo(self):
        ret, frame = self.cap.read()
        if not ret:
            messagebox.showerror("Error", "Could not read frame.")
            return
        
        downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
        if not os.path.exists(downloads_folder):
            os.makedirs(downloads_folder)
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(downloads_folder, f"photo_{timestamp}.jpg")
        
        cv2.imwrite(file_path, frame)
        
        messagebox.showinfo("Success", f"Photo saved to {file_path}")
    
    def on_closing(self):
        self.cap.release()
        self.root.destroy()

def create_gui():
    root = tk.Tk()
    app = PhotoCaptureApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    create_gui()
