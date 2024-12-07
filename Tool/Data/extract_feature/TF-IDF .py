from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy as np

import fitz
import re
import string


from nhan_oymu import * 



text1 = fitz_extract(r'D:\DST\Tool\material\Introduction to Machine Learning with Python.pdf')
text_clean1 = text1.extract_text()


text2 = fitz_extract(r'D:\DST\Tool\material\Sample_for_test\sample1.txt')
text_clean2 = text2.txt_extract()


text3 = fitz_extract(r'D:\DST\Tool\material\Sample_for_test\sample2.txt')
text_clean3 = text3.txt_extract()

# Dữ liệu văn bản ví dụ
documents = [text_clean1, text_clean2 , text_clean3]

# Tạo vectorizer TF-IDF và CountVectorizer
# TfidfVectorizer tự động loại bỏ các từ không mang ý nghĩa thông tin hoặc xuất hiện quá thường xuyên, loại bỏ các từ stopword. 
tfidf_vectorizer = TfidfVectorizer()
count_vectorizer = CountVectorizer()

# Chuyển đổi các tài liệu thành các đặc trưng TF-IDF và số lần xuất hiện của từ
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
count_matrix = count_vectorizer.fit_transform(documents)

# Chuyển kết quả thành ma trận dày đặc và xem các giá trị TF-IDF và số lần xuất hiện
tfidf_array = tfidf_matrix.toarray()
count_array = count_matrix.toarray()
print(tfidf_matrix.toarray())
print(count_matrix.toarray())
# Lấy tên các từ từ các đặc trưng trong TF-IDF
feature_names = tfidf_vectorizer.get_feature_names_out()

# Tìm từ xuất hiện nhiều nhất trong các tài liệu (theo CountVectorizer)
word_counts = count_array.sum(axis=0)
max_count_idx = np.argmax(word_counts)

# Tìm giá trị TF-IDF cao nhất cho từ đó
max_count_word = feature_names[max_count_idx]
max_count_value = word_counts[max_count_idx]

# Tìm giá trị TF-IDF của từ xuất hiện nhiều nhất
max_word_tfidf_value = tfidf_array[:, max_count_idx].max()

print(f"Từ xuất hiện nhiều nhất là '{max_count_word}' với số lần xuất hiện {max_count_value}")
print(f"Trọng số TF-IDF của từ '{max_count_word}' trong tài liệu là {max_word_tfidf_value:.4f}")


# Tìm từ xuất hiện trên 10 lần
words_above_threshold = {}

for idx, count in enumerate(word_counts):
    if count > 10:
        words_above_threshold[feature_names[idx]] = count

# In các từ và số lần xuất hiện
for word, count in words_above_threshold.items():
    print(f"Từ: '{word}' - Số lần xuất hiện: {count}")

# Nếu không có từ nào trên ngưỡng, thông báo
if not words_above_threshold:
    print("Không có từ nào xuất hiện trên 10 lần.")

