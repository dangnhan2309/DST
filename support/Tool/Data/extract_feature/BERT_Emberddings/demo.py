from transformers import BertTokenizer, BertModel
import torch
from sklearn.cluster import KMeans

# Load BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Sample text (could be a paragraph or document)
text = [
    "Word embeddings are a type of word representation.",
    "BERT model generates contextualized word embeddings.",
    "The meaning of a word depends on its context in a sentence.",
    "Embeddings capture semantic relationships between words.",
    "BERT is used for various NLP tasks, including classification."
]

# Tokenize and get embeddings for each sentence
sentence_embeddings = []

for sentence in text:
    inputs = tokenizer(sentence, return_tensors="pt")
    outputs = model(**inputs)
    # Get the [CLS] token embedding (first token)
    cls_embedding = outputs.last_hidden_state[0][0].detach().numpy()
    sentence_embeddings.append(cls_embedding)

# Perform K-means clustering to group sentences by topic (example)
kmeans = KMeans(n_clusters=2, random_state=0).fit(sentence_embeddings)

# Print the cluster labels for each sentence
for i, label in enumerate(kmeans.labels_):
    print(f"Sentence: '{text[i]}' belongs to Cluster {label}")
