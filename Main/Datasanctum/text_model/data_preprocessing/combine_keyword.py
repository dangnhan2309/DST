 

# list_words =["machine learning", "deep learning", "AI", "neural networks"]
# print(list_words[0])
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
import yake
from bertopic import BERTopic

def generate_topic_name_tfidf(keywords):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform([" ".join(keywords)])
    feature_array = vectorizer.get_feature_names_out()
    tfidf_scores = X.toarray().flatten()
    top_keywords = [feature_array[i] for i in tfidf_scores.argsort()[-3:][::-1]]
    return " - ".join(top_keywords)

def generate_topic_name_yake(keywords):
    kw_extractor = yake.KeywordExtractor()
    extracted_keywords = kw_extractor.extract_keywords(" ".join(keywords))
    top_keywords = [kw[0] for kw in extracted_keywords[:3]]
    return " & ".join(top_keywords)


# Example usage
keywords = ["machine learning", "deep learning", "neural networks", "AI", "data science"]
print("TF-IDF Topic Name:", generate_topic_name_tfidf(keywords))
print("YAKE Topic Name:", generate_topic_name_yake(keywords))

