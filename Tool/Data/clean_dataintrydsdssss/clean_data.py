from py_pdf2 import * 
import re



class clean_data: 
    def __init__(self,text): 
        self.text = text  


def clean_text(self):
    text_fix = re.sub(r'[^A-Za-z0-9\s]', '', self.text)
    print(text)

    explanation = """
    Remove Unnecessary Characters:
    Use regular expressions to remove 
    non-alphanumeric characters (except spaces).
    """



