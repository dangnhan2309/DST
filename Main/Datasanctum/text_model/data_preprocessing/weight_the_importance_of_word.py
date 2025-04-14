# import spacy

# # Load the English NLP model
# nlp = spacy.load("en_core_web_sm")

# # Sample text
# text = "Machine learning is a subset of artificial intelligence."

# # Process the text
# doc = nlp(text)

# # Define importance weights based on grammatical roles
# weights = {
#     "NOUN": 2.0,  # Nouns are important
#     "PROPN": 2.5, # Proper nouns are very important
#     "VERB": 1.5,  # Verbs carry meaning
#     "ADJ": 1.2,   # Adjectives modify meaning
#     "ADV": 1.1,   # Adverbs can be relevant
#     "DET": 0.5,   # Determiners (e.g., "the") are less important
#     "PRON": 0.5,  # Pronouns are less important
# }

# # Compute word importance scores
# word_importance = {token.text: weights.get(token.pos_, 1.0) for token in doc}

# # Display results
# for word, importance in word_importance.items():
#     print(f"{word}: {importance}")
#     #=--------------------------------
# from nltk.corpus import wordnet

# def semantic_importance(word):
#     synsets = wordnet.synsets(word)
#     return len(synsets)  # More synsets → more meanings → more importance

# # Example words
# words = ["learning", "is", "subset", "artificial", "intelligence"]

# # Compute importance
# importance_scores = {word: semantic_importance(word) for word in words}

# # Print scores
# print(importance_scores)



# final_scores = {word: word_importance[word] * importance_scores.get(word, 1) for word in words}

# # Print final importance ranking
# print(sorted(final_scores.items(), key=lambda x: x[1], reverse=True))


import spacy
from nltk.corpus import wordnet

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

def get_grammatical_weight(text):
    """Assign importance based on grammatical roles."""
    doc = nlp(text)
    weights = {
        "NOUN": 2.0,  # Nouns are important
        "PROPN": 2.5, # Proper nouns are very important
        "VERB": 1.5,  # Verbs carry meaning
        "ADJ": 1.2,   # Adjectives modify meaning
        "ADV": 1.1,   # Adverbs can be relevant
        "DET": 0.5,   # Determiners (e.g., "the") are less important
        "PRON": 0.5,  # Pronouns are less important
    }
    return {token.text: weights.get(token.pos_, 1.0) for token in doc}

def get_semantic_importance(words):
    """Assign importance based on meaning (WordNet synset count)."""
    return {word: len(wordnet.synsets(word)) for word in words}

def compute_final_scores(text):
    """Compute final importance scores by combining grammar and meaning."""
    grammatical_weights = get_grammatical_weight(text)
    words = list(grammatical_weights.keys())
    semantic_weights = get_semantic_importance(words)
    return {word: grammatical_weights[word] * semantic_weights.get(word, 1) for word in words}

def main():
    text = "Machine learning is a subset of artificial intelligence."
    final_scores = compute_final_scores(text)
    sorted_scores = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)
    print("Word Importance Ranking:")
    for word, score in sorted_scores:
        print(f"{word}: {score:.2f}")

if __name__ == "__main__":
    main()