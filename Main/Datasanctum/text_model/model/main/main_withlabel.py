import json
import os
from bertopic import BERTopic

jsonl_file = "D:/arxiv-metadata-oai-snapshot.json"
save_dir = r"D:\model"
model_path = os.path.join(save_dir, "bertopic_model(50k)")

if not os.path.exists(save_dir):
    os.makedirs(save_dir)  
    print(f"? T?o th? m?c: {save_dir}")

abstracts = []
with open(jsonl_file, "r", encoding="utf-8") as file:
    for line in file:
        data = json.loads(line)
        if "abstract" in data:
            abstracts.append(data["abstract"])
        if len(abstracts) >= 50000:
            break

print(f"?? S? l??ng abstracts thu th?p ???c: {len(abstracts)}")

topic_model = BERTopic()
topics, probs = topic_model.fit_transform(abstracts)
try:
    topic_model.save(model_path, save_embedding_model=True)
    print(f"? Mô hình ?ã ???c l?u t?i: {model_path}")
except Exception as e:
    print(f"? L?i khi l?u mô hình: {e}")

try:
    loaded_model = BERTopic.load(model_path)
    print(f"? Mô hình ?ã ???c load l?i t?: {model_path}")
except Exception as e:
    print(f"? L?i khi load mô hình: {e}")
