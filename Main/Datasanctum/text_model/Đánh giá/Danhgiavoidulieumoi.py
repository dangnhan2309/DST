from bertopic import BERTopic

# Đường dẫn đến mô hình đã lưu
model_path = r"D:\model\bertopic_model"

# Tải lại mô hình đã lưu
try:
    topic_model = BERTopic.load(model_path)
    print(f"✅ Mô hình đã được load thành công từ: {model_path}")
except Exception as e:
    print(f"❌ Lỗi khi load mô hình: {e}")
    exit()

# Văn bản mẫu để kiểm tra
sample_text = """
A rather non-standard quantum representation of the canonical commutation
relations of quantum mechanics systems, known as the polymer representation has
gained some attention in recent years, due to its possible relation with Planck
scale physics. In particular, this approach has been followed in a symmetric
sector of loop quantum gravity known as loop quantum cosmology. Here we explore
different aspects of the relation between the ordinary Schroedinger theory and
the polymer description. The paper has two parts. In the first one, we derive
the polymer quantum mechanics starting from the ordinary Schroedinger theory
and show that the polymer description arises as an appropriate limit. In the
second part we consider the continuum limit of this theory, namely, the reverse
process in which one starts from the discrete theory and tries to recover back
the ordinary Schroedinger quantum mechanics. We consider several examples of
interest, including the harmonic oscillator, the free particle and a simple
cosmological model.

"""

# Dự đoán chủ đề
predicted_topic, predicted_prob = topic_model.transform([sample_text])

# Kiểm tra kết quả dự đoán
if predicted_topic[0] != -1:
    topic_id = predicted_topic[0]  # ID chủ đề dự đoán
    topic_words = topic_model.get_topic(topic_id)  # Lấy danh sách từ quan trọng trong chủ đề
    topic_name = ", ".join([word for word, _ in topic_words[:5]])  # Lấy 5 từ đại diện cho chủ đề

    print(f"\n🔹 Chủ đề dự đoán: {topic_id}")
    print(f"📌 Độ tin cậy: {predicted_prob[0]:.4f}")
    print(f"🔹 Tên chủ đề: {topic_name}")
else:
    print("❌ Không thể xác định chủ đề phù hợp cho văn bản này.")
