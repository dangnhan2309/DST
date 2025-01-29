
import os
from types_can_accept import type_text_file_accepted

# docx

class file_interact: 
    def __init__(self,path,output): 
        self.path = path  
        self.output = output 
    def validate_file_extension_and_path(self):
        try:
            if not isinstance(self.path,str): 
                raise TypeError("File must be a string type.")
            if not os.path.exists(self.path): 
                raise ValueError("Not a valid path !")
            if os.path.splitext(self.path)[1].lower() not in type_text_file_accepted: 
                raise ValueError("File is not a text file")
            print("All input is valid !!!")
        except TypeError as e:
            print(f"Type Error : {e}")
        except ValueError as e :
            print(f"ValueError: {e}")

def is_valid_path(path):
    return os.path.exists(path)
def main (): 
    file_path1 = file_interact("asdsa.docx",1222)
if __name__ == '__main__': 
    main() 
