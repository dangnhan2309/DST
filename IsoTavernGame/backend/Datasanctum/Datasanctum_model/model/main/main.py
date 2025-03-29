# Step 1: Import Necessary Libraries
import numpy as np
import pandas as pd
import umap
import hdbscan
from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load and Process Data
def load_data(file_path):
    """Load text data from a file or dataset."""
    df = pd.read_csv(file_path)  # Modify as needed
    return df['text'].tolist()

def preprocess_text(texts):
    """Perform text cleaning (lowercasing, stopword removal, etc.)."""
    # Implement tokenization, stopword removal, etc.
    return cleaned_texts

# Step 3: Convert Text to Embeddings
def generate_embeddings(texts, model_name="all-MiniLM-L6-v2"):
    """Generate vector embeddings using a Transformer-based model."""
    model = SentenceTransformer(model_name)
    embeddings = model.encode(texts, convert_to_numpy=True)
    return embeddings

# Step 4: Dimensionality Reduction
def reduce_dimensionality(embeddings, n_components=2):
    """Apply UMAP for dimensionality reduction."""
    reducer = umap.UMAP(n_components=n_components)
    reduced_embeddings = reducer.fit_transform(embeddings)
    return reduced_embeddings

# Step 5: Clustering for Topic Discovery
def cluster_embeddings(embeddings):
    """Cluster embeddings using HDBSCAN."""
    clusterer = hdbscan.HDBSCAN(min_cluster_size=5)
    labels = clusterer.fit_predict(embeddings)
    return labels

# Step 6: Extract Topic Keywords
def extract_keywords(texts, labels):
    """Use TF-IDF to extract topic keywords for each cluster."""
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    terms = vectorizer.get_feature_names_out()

    topic_keywords = {}
    for label in set(labels):
        indices = np.where(labels == label)[0]
        topic_terms = np.mean(X[indices], axis=0).A1
        top_terms = [terms[i] for i in topic_terms.argsort()[-5:]]
        topic_keywords[label] = top_terms
    
    return topic_keywords

# Step 7: Save and Compare Embeddings
def save_embeddings(embeddings, file_name="embeddings.npy"):
    """Save topic embeddings for future comparison."""
    np.save(file_name, embeddings)

def compare_embeddings(new_embedding, stored_embeddings):
    """Compare new document embeddings using cosine similarity."""
    similarities = cosine_similarity(new_embedding, stored_embeddings)
    return similarities

# Step 8: Visualization and Analysis
def visualize_topics(embeddings, labels):
    """Visualize topic clusters using UMAP projection."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=embeddings[:,0], y=embeddings[:,1], hue=labels, palette="viridis")
    plt.title("Topic Clusters")
    plt.show()

# Step 9: Main Execution
if __name__ == "__main__":
    # Load and process data
    texts = load_data("data.csv")
    cleaned_texts = preprocess_text(texts)

    # Generate embeddings and apply topic modeling
    embeddings = generate_embeddings(cleaned_texts)
    reduced_embeddings = reduce_dimensionality(embeddings)
    labels = cluster_embeddings(reduced_embeddings)

    # Extract keywords and visualize topics
    topic_keywords = extract_keywords(cleaned_texts, labels)
    visualize_topics(reduced_embeddings, labels)

    # Save embeddings for future use
    save_embeddings(embeddings)
