from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Example embeddings (assuming they are numpy arrays)
embedding_supervised_learning = np.array([0.12, -0.45, 0.88, -0.23, 0.67])
embedding_paragraph = np.array([0.34, -0.12, 0.67, -0.15, 0.44])

similarity_score = cosine_similarity([embedding_supervised_learning], [embedding_paragraph])
print(f"Cosine Similarity: {similarity_score[0][0]}")
