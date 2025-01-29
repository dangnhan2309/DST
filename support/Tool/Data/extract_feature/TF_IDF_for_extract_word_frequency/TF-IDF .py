from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy as np

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet 

from extract_text_from_file.py import * 



text1 = fitz_extract(r'D:\DST\Tool\material\Introduction to Machine Learning with Python.pdf')
text_clean1 = text1.extract_text()

print(text_clean1)

text2 = fitz_extract(r'D:\DST\Tool\material\Sample_for_test\sample1.txt')
text_clean2 = text2.extract_text()

print(text_clean2)


text3 = fitz_extract(r'D:\DST\Tool\material\Sample_for_test\sample2.txt')
text_clean3 = text3.extract_text()

print(text_clean3)




documents = [text_clean1, text_clean2 , text_clean3]

tfidf_vectorizer = TfidfVectorizer()
count_vectorizer = CountVectorizer()

tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
count_matrix = count_vectorizer.fit_transform(documents)

tfidf_array = tfidf_matrix.toarray()
count_array = count_matrix.toarray()
print(tfidf_matrix.toarray())
print(count_matrix.toarray())
feature_names = tfidf_vectorizer.get_feature_names_out()



word_counts = count_array.sum(axis=0)
max_count_idx = np.argmax(word_counts)

max_count_word = feature_names[max_count_idx]
max_count_value = word_counts[max_count_idx]

max_word_tfidf_value = tfidf_array[:, max_count_idx].max()
print(f"Từ xuất hiện nhiều nhất là '{max_count_word}' với số lần xuất hiện {max_count_value}")
print(f"Trọng số TF-IDF của từ '{max_count_word}' trong tài liệu là {max_word_tfidf_value:.4f}")


words_above_threshold = {}
for idx, count in enumerate(word_counts):
    if count < 2:
        words_above_threshold[feature_names[idx]] = count
for word, count in words_above_threshold.items():
    print(f"Từ: '{word}' - Số lần xuất hiện: {count}")
if not words_above_threshold:
    print("Không có từ nào xuất hiện trên 10 lần.")




