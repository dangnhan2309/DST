import json
import os
import pandas as pd
from tqdm import tqdm
from collections import Counter
from bertopic import BERTopic

# 1?? ??c d? li?u t? t?p JSONL
jsonl_file = "D:/arxiv-metadata-oai-snapshot.json"
save_dir = "D:/model"
model_path = os.path.join(save_dir, "bertopic_arxiv")

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

abstracts = []
categories = []

# ??c file và trích xu?t abstracts + categories
with open(jsonl_file, "r", encoding="utf-8") as file:
    for line in tqdm(file, desc="?? ??c d? li?u"):
        data = json.loads(line)  
        if "abstract" in data and "categories" in data:
            abstracts.append(data["abstract"])
            categories.append(data["categories"].split())  # Có th? có nhi?u nhãn

        if len(abstracts) >= 50000:  # Gi?i h?n 50,000 m?u
            break

print(f"?? ?ã thu th?p {len(abstracts)} abstracts.")

# 2?? Hu?n luy?n mô hình BERTopic
print("?? Hu?n luy?n mô hình BERTopic...")
topic_model = BERTopic()
topics, probs = topic_model.fit_transform(abstracts)

# 3?? Xây d?ng ánh x? topic ? category
topic_to_category = {}

# Duy?t qua t?t c? các abstracts
for topic_id, cats in zip(topics, categories):
    if topic_id not in topic_to_category:
        topic_to_category[topic_id] = []
    topic_to_category[topic_id].extend(cats)

# L?y category ph? bi?n nh?t cho m?i topic
for topic_id in topic_to_category:
    most_common_category = Counter(topic_to_category[topic_id]).most_common(1)[0][0]
    topic_to_category[topic_id] = most_common_category

print("? ?ã ánh x? topic ? category.")

# 4?? L?u mô hình ?ã hu?n luy?n
try:
    topic_model.save(model_path, save_embedding_model=True)
    print(f"? Mô hình ?ã ???c l?u t?i: {model_path}")
except Exception as e:
    print(f"? L?i khi l?u mô hình: {e}")

# 5?? D? ?oán m?t abstract m?i
sample_text = "Deep learning has transformed natural language processing with models like transformers."
predicted_topic, predicted_prob = topic_model.transform([sample_text])

# In k?t qu? d? ?oán
if predicted_topic[0] != -1:
    topic_id = predicted_topic[0]
    topic_words = topic_model.get_topic(topic_id)
    predicted_category = topic_to_category.get(topic_id, "Unknown")

    print(f"?? Ch? ?? d? ?oán: {topic_id}")
    print(f"?? ?? tin c?y: {predicted_prob[0]:.4f}")
    print(f"?? Tên ch? ??: {', '.join([w for w, _ in topic_words])}")
    print(f"?? D? ?oán category: {predicted_category}")
else:
    print("? Không th? xác ??nh ch? ?? phù h?p.")
