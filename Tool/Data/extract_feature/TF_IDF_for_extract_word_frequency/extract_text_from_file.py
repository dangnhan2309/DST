from mailbox import mboxMessage
import fitz
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
import re

from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

class fitz_extract: 
    def __init__(self, path): 
        self.path = path
        self.stop_words = set(stopwords.words('english'))

    def extract_text(self):
        para = ""
        if self.path.endswith('.txt'): 
            with open(self.path,'r') as file : 
                text_clean = self.clean_text(file.read())
                para = text_clean
                
        elif self.path.endswith('.pdf'):
            pdf = fitz.open(self.path)
            for page in pdf: 
                text = page.get_text()
                para+= text
        para = self.clean_text(para)                
        return para

    def clean_text(self, text):
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = text.lower()
        text = self.remove_punctuation(text)
        words = word_tokenize(text)
        words = [word for word in words if word.lower() not in self.stop_words] 
        words = self.normalize(words)
        cleaned_text = ' '.join(words)

        return cleaned_text
    def remove_punctuation(self, text):
        return text.translate(str.maketrans('', '', string.punctuation))

    def get_wordnet_pos(self,tag): 
        if tag.startswith('V'):
            return wordnet.VERB
        else : 
            return None

    def normalize(self,list_of_word):

        normalized_list = []
        lemmatizer = WordNetLemmatizer()
        for word,tag in pos_tag(list_of_word):
            wordnet_pos = self.get_wordnet_pos(tag)
            if wordnet_pos is not None: 
                normalized_word = lemmatizer.lemmatize(word,pos=wordnet_pos)
            else:
                normalized_word = word 
            normalized_list.append(normalized_word)
        return normalized_list


def main(): 
    text = fitz_extract(r'D:\DST\Tool\material\Introduction to Machine Learning with Python.pdf')
    text2 = text.extract_text()

   
    
    # Sử dụng phương thức đã chỉnh sửa[]
    print(text2)


if __name__ == "__main__":
    main()
