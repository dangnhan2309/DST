import PyPDF2

class text_extract : 
    def __init__(self,file_path):
        self.path = file_path; 
    def extract_text_from_pdf(self):
        try: 
            with open(self.file_path,'rb') as file : 
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages: 
                    text += page.extract_text()
            return text
        except Exception as e : 
            return f"en error : {e}"
            
