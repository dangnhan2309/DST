from bertopic import BERTopic

# Đường dẫn đến mô hình đã lưu
model_path = r"D:\model\bertopic_model"

# Load lại mô hình
topic_model = BERTopic.load(model_path)

# Lấy thông tin về tất cả các chủ đề đã học
topic_info = topic_model.get_topic_info()

# In danh sách chủ đề đã học
print("📌 Danh sách các chủ đề đã học:")
print(topic_info)
