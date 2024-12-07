import re
from nltk.corpus import stopwords
import string




class clean_text: 
    def __init__(self,text):
        self.text =text 
    def clean_extra(self):
        self.text = re.sub(r'[^A-Za-z0-9\s]', '', self.text)


        nltk.download('stopwords')
        stop_words = set(stopwords.words('english'))
        filtered_text = ' '.join([word for word in self.text.split() if word.lower() not in stop_wordsx])
        
        self.text = self.text.translate(str.maketrans('', '', string.punctuation))


        return self.text 

def main(): 
    


if __name__ == "__main__":
    main()
        







        