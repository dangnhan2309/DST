from sklearn.feature_extraction.text import CountVectorizer
from nhan_oymu import * 


# Sample text data


text1 = fitz_extract(r'D:\DST\Tool\material\Introduction to Machine Learning with Python.pdf')
text_clean1 = text1.extract_text()


text2 = fitz_extract(r'D:\DST\Tool\material\Sample_for_test\sample1.txt')
text_clean2 = text2.txt_extract()


text3 = fitz_extract(r'D:\DST\Tool\material\Sample_for_test\sample2.txt')
text_clean3 = text3.txt_extract()

print(text_clean2)


documents = [text_clean1,text_clean2,text_clean3]

# Create a BoW model
vectorizer = CountVectorizer()
bow_features = vectorizer.fit_transform(documents)

# Inspect BoW matrix
print(bow_features.toarray())
print(vectorizer.get_feature_names_out())

