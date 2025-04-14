from sentence_transformers import SentenceTransformer
from umap import UMAP
from hdbscan import HDBSCAN
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from bertopic import BERTopic
import json
import os


jsonl_file = "D:/arxiv-metadata-oai-snapshot.json"
save_dir = r"D:\model"
model_path = os.path.join(save_dir, "bertopic_model(ver3-50k_Reference)")

if not os.path.exists(save_dir):
    os.makedirs(save_dir)  
    print(f"✅ Tạo thư mục: {save_dir}")
abstracts = []
with open(jsonl_file, "r", encoding="utf-8") as file:
    for line in file:
        data = json.loads(line)
        if "abstract" in data:
            abstracts.append(data["abstract"])
        if len(abstracts) >= 50000:
            break

print(f"📌 Số lượng abstracts thu thập được: {len(abstracts)}")
embedding_model = SentenceTransformer('all-mpnet-base-v2')
umap_model = UMAP(n_neighbors=15)
hdbscan_model = HDBSCAN(min_cluster_size=20, min_samples=1,
                        gen_min_span_tree=True,
                        prediction_data=True)

stopwords = list(stopwords.words('english')) + ['http', 'https', 'amp', 'com']
vectorizer_model = CountVectorizer(ngram_range=(1, 3), stop_words=stopwords)

topic_model = BERTopic(
    umap_model=umap_model,
    hdbscan_model=hdbscan_model,
    embedding_model=embedding_model,
    vectorizer_model=vectorizer_model,
    language='english',
    calculate_probabilities=True,
    verbose=True
)
topics, probs = topic_model.fit_transform(abstracts)
try:
    topic_model.save(model_path, save_embedding_model=True)
    print(f"✅ Mô hình đã được lưu tại: {model_path}")
except Exception as e:
    print(f"❌ Lỗi khi lưu mô hình: {e}")

try:
    loaded_model = BERTopic.load(model_path)
    print(f"✅ Mô hình đã được load lại từ: {model_path}")
except Exception as e:
    print(f"❌ Lỗi khi load mô hình: {e}")
