from mailbox import Message, mboxMessage
import tkinter as tk
from pytest import File
from tkinterdnd2 import DND_FILES, TkinterDnD
import os
import subprocess
import shutil
<<<<<<< Updated upstream
import fitz  # PyMuPDF
=======
from update_folder_structure import FolderMapper

from Main.Main_program import Create_emberding
from bert import Emberding

>>>>>>> Stashed changes
def on_button_click():
    folder_path = r"C:\Users\Marco\Desktop\dst"
    subprocess.run(["explorer", folder_path], shell=True)  # Open folder in Windows Explorer    
def change_path(current_path, newpath):
    try:
        shutil.move(current_path, newpath)
        label.config(text=f"File moved to: {newpath}")
    except Exception as e:
        label.config(text=f"Error: {str(e)}")



def extract_content(file_path):
    try:
        if file_path.endswith('.pdf'):
            return extract_pdf_content(file_path)
        else:
            return extract_text_content(file_path)
    except Exception as e:
        return f"Error {str(e)}"

def extract_pdf_content(file_path):
    pdf_document = fitz.open(file_path)
    text_data = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text_data += page.get_text()
    return text_data
<<<<<<< Updated upstream

def extract_text_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text_data = file.read()
    return text_data

def emberding(text): 
=======
>>>>>>> Stashed changes


def emberding(text): 
    emberding_code = Create_emberding(text)
    return emberding_code
def compare_ember_code(ember_code): 
    folder_check= r"C:\Users\Marco\Desktop\dst"
    file_save= r"C:\Users\Marco\Desktop\dst\cautruc_folder.json"
    updater = FolderMapper(folder_check,file_save)


    if exist : 
        return topic_path ; 
    if not :
        #tao folder, topic name , add topic to the warehouse
        return
    return topic_path
def classify(file_path): 

    data_file= extract_content(file_path)

    emberding_data_file = emberding(data_file)


    topic_path= compare_ember_code(emberding_data_file)

    return topic_path
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

