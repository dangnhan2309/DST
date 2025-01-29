import os
import json
import pandas as pd
import PyPDF2
import librosa
import numpy as np
from PIL import Image
from docx import Document
from sklearn.preprocessing import LabelEncoder

# Thư mục chứa dữ liệu đầu vào
DATASET_PATH = r"D:\DST"
OUTPUT_FILE = "file_dataset.csv"

# Hàm trích xuất văn bản từ file PDF
def extract_text_pdf(file_path):
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = "".join([page.extract_text() for page in reader.pages if page.extract_text()])
        return text[:500]  # Lấy 500 ký tự đầu tiên
    except:
        return ""

# Hàm trích xuất văn bản từ file DOCX
def extract_text_docx(file_path):
    try:
        doc = Document(file_path)
        return " ".join([para.text for para in doc.paragraphs])[:500]
    except:
        return ""

# Hàm trích xuất đặc trưng hình ảnh
def extract_image_features(file_path):
    try:
        img = Image.open(file_path).convert("L")
        img = img.resize((64, 64))  # Resize để thống nhất kích thước
        return np.array(img).flatten()
    except:
        return np.zeros(64*64)

# Hàm trích xuất đặc trưng âm thanh
def extract_audio_features(file_path):
    try:
        y, sr = librosa.load(file_path, duration=5)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        return np.mean(mfcc, axis=1)
    except:
        return np.zeros(13)

# Duyệt qua thư mục và thu thập dữ liệu
data = []
for root, _, files in os.walk(DATASET_PATH):
    for file in files:
        file_path = os.path.join(root, file)
        ext = file.split(".")[-1].lower()
        features = ""
        
        if ext == "pdf":
            features = extract_text_pdf(file_path)
        elif ext == "docx":
            features = extract_text_docx(file_path)
        elif ext in ["jpg", "png"]:
            features = extract_image_features(file_path)
        elif ext in ["mp3", "wav"]:
            features = extract_audio_features(file_path)
        
        data.append({"filename": file, "extension": ext, "features": features})

# Lưu dataset thành CSV
df = pd.DataFrame(data)
df.to_csv(OUTPUT_FILE, index=False)
print("Dataset created successfully!")
