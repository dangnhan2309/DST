from cProfile import label
from mailbox import Message, mboxMessage
import tkinter as tk
from pytest import File
from tkinterdnd2 import DND_FILES, TkinterDnD
import os
import subprocess
import shutil
import fitz
from torch import embedding  # PyMuPDF
from update_folder_structure import FolderMapper
from bert import Emberding
from topic_emberding import topic_emberding
from topic_emberding import topic_emberding

def on_button_click():
    folder_path = r"C:\Users\Marco\Desktop\dst"
    subprocess.run(["explorer", folder_path], shell=True) 
    
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


def extract_text_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text_data = file.read()
    return text_data


def emberding(text): 
    emberding_code = Emberding.create_embedding(text)
    return emberding_code

def compare_ember_code(ember_code): 

    folder_check= r"C:\Users\Marco\Desktop\Testing"
    file_save= r"C:\Users\Marco\Desktop\Testing\cautruc_folder.json"
    updater = FolderMapper(folder_check,file_save)
    print("-" * 50 )
    print(ember_code)
    print("-" * 50 )
    Max_similarities = 0.000000
    topic_max = ""
    for topic, details in topic_emberding.items():
        #print(f"  Code: {details["topic_emberding_code"]}")
        simi_num = Emberding.compare_embercode(details["topic_emberding_code"],ember_code)
        if simi_num >= Max_similarities:
            topic_max = topic
            Max_similarities = simi_num
        print(f"{topic} :  {simi_num}")

    print("--"*55+ "keets qua")
    print (Max_similarities)
    print(topic_max) 

    return Max_similarities,topic_max
    #______12/2 :  đã hoàn thành các chức năng đọc file , phan tích , chưa haonfg thành so sánh emberding

    # if exist : 
    #     return topic_path ; 
    # if  :
    #     #tao folder, topic name , add topic to the warehouse
    #     return
    #return topic_path




def classify(file_path): 

    data_file= extract_content(file_path)

    emberding_data_file = emberding(data_file)

    siminum,topic= compare_ember_code(emberding_data_file)

    print(f"{topic}: {siminum}")

def on_drop(event): 
    file_path = event.data.strip().strip('{}')
    file_name = os.path.basename(file_path)

    newpath = classify(file_path)


    #change_path(file_path,newpath)




    #Create the main window


def screenprogram():
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


def main(): 
    screenprogram()
if __name__ == "__main__": 
    main() 

