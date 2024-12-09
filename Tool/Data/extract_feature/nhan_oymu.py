import fitz
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')

class fitz_extract: 
    def __init__(self, path): 
        self.path = path
        self.stop_words = set(stopwords.words('english')) 

    def extract_text(self): 
        pdf = fitz.open(self.path)
        full_text=""
        for page in pdf: 
            text = page.get_text()
            cleaned_text = self.clean_text(text)
            full_text +=cleaned_text
        return full_text
    def clean_text(self, text):
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        text = self.remove_punctuation(text)
        words = word_tokenize(text)  
        words = [word for word in words if word.lower() not in self.stop_words]
        cleaned_text = ' '.join(words)
        return cleaned_text
    def txt_extract (self): 
        # Open the file in read mode
        with open(self.path,'r', encoding='utf-8') as file:
            text = file.read()
        cleaded_text = self.clean_text(text)
        # Print the content of the file
        return cleaded_text
    def remove_punctuation(self, text):
        return text.translate(str.maketrans('', '', string.punctuation) 
    def nomalize() : 

def main(): 
    text = fitz_extract(r'D:\DST\Tool\material\Introduction to Machine Learning with Python.pdf')
    print(text.extract_text())


if __name__ == "__main__":
    main()

