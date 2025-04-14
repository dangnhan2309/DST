from bertopic import BERTopic

# Đường dẫn đến mô hình đã lưu
model_path = r"D:\model\bertopic_model(ver2-50k_Reference)"

# Tải lại mô hình đã lưu
try:
    topic_model = BERTopic.load(model_path)
    print(f"Mô hình đã được load thành công từ: {model_path}")
except Exception as e:
    print(f"Lỗi khi load mô hình: {e}")
    exit()

# Văn bản mẫu để kiểm tra

#pth_tailieu =
sample_text = "A Decision Tree is a simple yet powerful machine learning algorithm used for both classification and regression tasks. It models decisions as a tree-like structure, where each internal node represents a test on a feature, each branch shows the outcome of the test, and each leaf node gives a final prediction or decision. The tree is built by recursively splitting the dataset based on the feature that provides the most significant information gain or reduces impurity the most. Decision Trees are easy to interpret and visualize, making them a popular choice for understanding the logic behind predictions. However, they can overfit the data if not properly pruned or regulated."


predicted_topic, predicted_prob = topic_model.transform([sample_text])
if predicted_topic[0] != -1:
    topic_id = predicted_topic[0] 
    topic_words = topic_model.get_topic(topic_id) 
    topic_name = ", ".join([word for word, _ in topic_words[:20]])  # Lấy 20 từ đại diện cho chủ đề
        
    print(f"\n🔹 Chủ đề dự đoán: {topic_id}")
    print(type(predicted_prob[0]))
    print(predicted_prob[0])

    max_prob = predicted_prob.max()
    print(f"Độ tin cậy: {max_prob:.4f}")
    print(f"Tên chủ đề: {topic_name}")
else:
    print("Không thể xác định chủ đề phù hợp cho văn bản này.")

print("-"*50)


