import json
import os
from bertopic import BERTopic

# Đường dẫn đến tệp JSONL
jsonl_file = "D:/arxiv-metadata-oai-snapshot.json"

# Đường dẫn lưu mô hình
save_dir = r"D:\model"
model_path = os.path.join(save_dir, "bertopic_model")

# Đảm bảo thư mục lưu mô hình tồn tại
if not os.path.exists(save_dir):
    os.makedirs(save_dir)  # Tạo thư mục nếu chưa tồn tại
    print(f"✅ Tạo thư mục: {save_dir}")

# Bước 1: Đọc và trích xuất abstracts từ tệp JSONL
abstracts = []
with open(jsonl_file, "r", encoding="utf-8") as file:
    for line in file:
        data = json.loads(line)  # Mỗi dòng là một JSON object
        if "abstract" in data:
            abstracts.append(data["abstract"])
        if len(abstracts) >= 500000:# Giới hạn 5.0000 mẫu
            break

print(f"📌 Số lượng abstracts thu thập được: {len(abstracts)}")

# Bước 2: Huấn luyện mô hình BERTopic
topic_model = BERTopic()
topics, probs = topic_model.fit_transform(abstracts)

# Bước 3: Lưu mô hình đã huấn luyện
try:
    topic_model.save(model_path, save_embedding_model=True)
    print(f"✅ Mô hình đã được lưu tại: {model_path}")
except Exception as e:
    print(f"❌ Lỗi khi lưu mô hình: {e}")

# Bước 4: Dự đoán chủ đề cho đoạn văn bản 
sample_text = """
Deep learning has achieved state-of-the-art results in many areas, including natural language processing and computer vision. 
Recently, transformers have gained popularity due to their ability to handle sequential data efficiently. 
These models utilize self-attention mechanisms to capture contextual information and generate meaningful representations.
"""

predicted_topic, predicted_prob = topic_model.transform([sample_text])

# Kiểm tra kết quả dự đoán
if predicted_topic[0] != -1:
    topic_id = predicted_topic[0]  # Chủ đề dự đoán được
    topic_words = topic_model.get_topic(topic_id)
    
    print(f"🔹 Chủ đề dự đoán: {topic_id}")
    print(f"📌 Độ tin cậy: {predicted_prob[0]:.4f}")
    print(f"🔹 Các từ đặc trưng của chủ đề {topic_id}:")
    for word, weight in topic_words:
        print(f"   - {word} ({weight:.4f})")
else:
    print("❌ Không thể xác định chủ đề phù hợp cho văn bản mẫu.")

# Bước 5: Kiểm tra có thể load lại mô hình không
try:
    loaded_model = BERTopic.load(model_path)
    print(f"✅ Mô hình đã được load lại từ: {model_path}")
except Exception as e:
    print(f"❌ Lỗi khi load mô hình: {e}")
