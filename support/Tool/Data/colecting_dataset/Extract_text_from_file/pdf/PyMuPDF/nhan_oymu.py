import fitz
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')

class fitz_extract: 
    def __init__(self, path): 
        self.path = path
        self.stop_words = set(stopwords.words('english'))  # Tải stopwords bằng NLTK

    def extract_text(self):  # Đổi tên phương thức thành extract_text
        pdf = fitz.open(self.path)
        for page in pdf: 
            text = page.get_text()
            cleaned_text = self.clean_text(text)
            print(cleaned_text)

    def clean_text(self, text):
        # Loại bỏ ký tự không phải chữ cái, số hoặc khoảng trắng
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        
        # Loại bỏ dấu câu
        text = self.remove_punctuation(text)
        
        # Phân tách văn bản thành các từ và loại bỏ stop words
        words = word_tokenize(text)  # Phân tách văn bản thành các từ (tokens)
        words = [word for word in words if word.lower() not in self.stop_words]  # Loại bỏ stop words
        
        # Kết hợp các từ lại thành một chuỗi văn bản đã làm sạch
        cleaned_text = ' '.join(words)
        
        return cleaned_text

    def remove_punctuation(self, text):
        # Loại bỏ dấu câu
        return text.translate(str.maketrans('', '', string.punctuation))

def main(): 
    text = fitz_extract(r'D:\DST\Tool\material\Introduction to Machine Learning with Python.pdf')
    text.extract_text()  # Sử dụng phương thức đã chỉnh sửa

if __name__ == "__main__":
    main()
