

# class classifying : 
#     def __init__(self): 
#         self.
#         
from pathlib import Path
from docx import Document
 # handling the incorrect path 

def read_content(path,line): 
    print(path)
    doc = Document(path)
    lines= [] 
    for para in doc.paragraphs : 
        lines.extend(para.text.splitlines())
        if len(lines) >=line:
            break
    for line in lines[:line]: 
        print(line)
def formatting_path(path): 
    path_correct = Path(path)
    return path_correct
def yes_no() : 
    answer = input("Your answer: ")
    if answer == 'yes' or 'y' or 'Yes' : 
        return True
        
    elif answer == 'No' or 'no' or 'n' : 
        return False
    else : 
        yes_no()

def main() : 
    #front end 
    # Tuong tac voi ng dung de nhan file
    print("This is a classsifying program")
    input_path = input("Nhap duong dan cua file: ")
    print("path : ")
    #because formating usually not right format ->formating lai
    path = formatting_path(input_path)
    print(f"this is your path {path} ? ")
    if yes_no() == True : 
        print("User say yes")
    else :
        print("User say no")
    global  line 
    line = 5
    # check noi dung file 
    #read_content(path,line)

    print(f"Ban co muon xem noi dung {line} line khong ? ")
    if yes_no() == True:
        read_content(path,line)
    else: 
        pass



    

    


main() 