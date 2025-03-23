from sentence_transformers import SentenceTransformer, util

# Khởi tạo mô hình BERT dùng để embedding
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Topic cần tối ưu hóa
topic_description = "Machine Learning is a field of AI that enables computers to learn from data."
topic_embedding = model.encode(topic_description, convert_to_tensor=True)

# Tạo các văn bản mô tả khác nhau
candidate_texts = [
    "Machine Learning is a branch of artificial intelligence that focuses on building systems that learn from data.",
    "ML helps computers identify patterns and make predictions without being explicitly programmed.",
    "Neural networks, a subfield of machine learning, have advanced AI applications significantly."
]

# Tính toán embedding cho từng văn bản
text_embeddings = [model.encode(text, convert_to_tensor=True) for text in candidate_texts]

# Tính độ tương đồng cosine giữa topic_embedding và các văn bản
similarities = [util.pytorch_cos_sim(topic_embedding, text_embedding).item() for text_embedding in text_embeddings]

# Chọn văn bản có độ tương đồng cao nhất
best_match = candidate_texts[similarities.index(max(similarities))]

print("Best Matching Text:", best_match)
print("Similarity Scores:", similarities)


