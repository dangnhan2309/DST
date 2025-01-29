from docx import Document
 

class Read_dox: 

    def __init__(self,path,line):
        self.path = path
        self.line = line 
    def read_5_first_line(self): 
         print(self.path)
         doc = Document(self.path)
         lines= [] 
         for para in doc.paragraphs : 
             lines.extend(para.text.splitlines())
             if len(lines) >=self.line:
                 break
         for line in lines[:self.line]: 
             print(line)

def main(): 
    doc= Read_dox(r'D:\DataSanctum_project\Nhan_file_content_classifying\BÁO_CÁO_TIỂU_LUẬN.docx'
                  ,5) 
    doc.read_5_first_line()

if __name__ == "__main__": 
    main() 