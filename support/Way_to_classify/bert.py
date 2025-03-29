from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity, sigmoid_kernel

class Emberding:
    
    def create_embedding(text):
        """
        Generates an embedding for a given text using Sentence-BERT (SBERT).
        :param text: The input text (sentence or paragraph) to encode.
        :return: A numerical embedding (list of floats).
        """
        model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight and efficient model
        embedding = model.encode(text, convert_to_tensor=True)
        return embedding


    def compare_embercode(embedding,embedding_label):
        embedding1 = np.asarray(embedding)
        embedding_labeled = np.asarray(embedding_label)
        similarity_score = cosine_similarity([embedding_labeled], [embedding1])

        return similarity_score


def main():
    sample_text = "Supervised learning models can make predictions after seeing lots of data with the correct answers and then discovering the connections between the elements in the data that produce the correct answers. This is like a student learning new material by studying old exams that contain both questions and answers. Once the student has trained on enough old exams, the student is well prepared to take a new exam. These ML systems are 'supervised' in the sense that a human gives the ML system data with the known correct results."
    embedding = np.asarray(Emberding.create_embedding(sample_text))
    label = "Supervised learning"
    embedding_label1 = np.asarray(Emberding.create_embedding(label))

    label2 = "Unsupervised Learning"
    embedding_label2 =np.asarray(Emberding.create_embedding(label2).tolist())

    similarity_score = cosine_similarity([embedding_label1], [embedding])
    similarity_score2 = cosine_similarity([embedding_label2], [embedding])

    print(f"Cosine Similarity: {similarity_score[0][0]}")
    print(f"Cosine Similarity 2 : {similarity_score2[0][0]}")






if __name__ == "__main__":
    main()
