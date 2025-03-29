import pandas as pd
import numpy as np
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report

# 1. Tạo tập dữ liệu mẫu
data = {
    "text": [
        "Đội tuyển Việt Nam giành chiến thắng trong trận đấu cuối cùng.",
        "Apple ra mắt iPhone mới với nhiều tính năng đột phá.",
        "Chính phủ thông qua dự luật mới về thuế.",
        "Messi ghi bàn thắng đẹp mắt giúp PSG giành chiến thắng.",
        "Tesla phát triển công nghệ xe tự lái tiên tiến hơn."
    ],
    "label": ["Thể thao", "Công nghệ", "Chính trị", "Thể thao", "Công nghệ"]
}

df = pd.DataFrame(data)

# 2. Làm sạch văn bản
def clean_text(text):
    text = text.lower()  # Chuyển thành chữ thường
    text = re.sub(r"\d+", "", text)  # Loại bỏ số
    text = text.translate(str.maketrans("", "", string.punctuation))  # Loại bỏ dấu câu
    return text

df["text"] = df["text"].apply(clean_text)

# 3. Chia tập dữ liệu thành train và test
X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.2, random_state=42)

# 4. Chuyển đổi văn bản sang TF-IDF và huấn luyện mô hình
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

# 5. Dự đoán trên tập test
y_pred = model.predict(X_test)
    
# 6. Đánh giá mô hình
print("Độ chính xác:", accuracy_score(y_test, y_pred))
print("Báo cáo phân loại:")
print(classification_report(y_test, y_pred))

# 7. Dự đoán chủ đề của văn bản mới
def predict_topic(text):
    text = clean_text(text)
    prediction = model.predict([text])[0]
    return prediction

new_text = "Elon Musk công bố công nghệ AI mới cho xe điện."
print("Chủ đề dự đoán:", predict_topic(new_text))
