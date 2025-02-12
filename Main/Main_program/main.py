from mailbox import Message, mboxMessage
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import os
import subprocess
import shutil

def on_button_click():
    folder_path = r"C:\Users\Marco\Desktop\dst"
    subprocess.run(["explorer", folder_path], shell=True)  # Open folder in Windows Explorer    
def change_path(current_path, newpath):
    try:
        shutil.move(current_path, newpath)
        label.config(text=f"File moved to: {newpath}")
    except Exception as e:
        label.config(text=f"Error: {str(e)}")
def classify(file_path): 
    #decided the topic of the file 

    #------
    #choose the suitable folder to classify
    return r"C:\Users\Marco\Desktop\dst"
def on_drop(event): 
    file_path = event.data.strip().strip('{}')
    file_name = os.path.basename(file_path)
    newpath = classify(file_path)
    change_path(file_path,newpath)
# Create the main window

def main(): 

    root = TkinterDnD.Tk()
    root.title("Tkinter Window")
    root.geometry("300x200")

    # Create a label
    label = tk.Label(root, text="Drag a file here", font=("Arial", 14))
    label.pack(pady=20)

    # Create a button
    button = tk.Button(root, text="Click Me", command=on_button_click, font=("Arial", 12))
    button.pack()

    # Enable file drag and drop
    root.drop_target_register(DND_FILES)
    root.dnd_bind('<<Drop>>', on_drop)

    # Run the application
    root.mainloop()
if "__name__" == "__main__": 
    main() 

