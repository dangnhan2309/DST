
# Step 1: Load the CSV File
import pandas as pd

# Load CSV file
data = pd.read_csv("file.csv")

# Inspect the data
print(data.head())

#Step 2: Preprocess the Data
# Check for missing values
print(data.isnull().sum())

# Drop missing rows if needed
data = data.dropna()

# Encode labels if not already encoded
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
data['Topic'] = encoder.fit_transform(data['Topic'])

# Inspect the encoded labels
print(encoder.classes_)


#Step 3: Split Data into Training and Testing Sets

from sklearn.model_selection import train_test_split

# Features (X) and Labels (y)
X = data['Concept']  # Text data
y = data['Topic']    # Encoded labels

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    


Step 4: Convert Text to Numeric Format
from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize TF-IDF Vectorizer
vectorizer = TfidfVectorizer(max_features=5000)

# Fit and transform the training data; transform the test data
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)



Step 5: Train a Machine Learning Model
from sklearn.naive_bayes import MultinomialNB

# Train a Naive Bayes Classifier
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Evaluate the model
accuracy = model.score(X_test_tfidf, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

Step 6: Predict on New Data

# Sample prediction
sample_text = ["Neural Networks"]
sample_tfidf = vectorizer.transform(sample_text)

# Predict
predicted_topic = model.predict(sample_tfidf)
print("Predicted Topic:", encoder.inverse_transform(predicted_topic))



Common Libraries for Text Classification
pandas: For handling CSV data.
scikit-learn: For preprocessing, feature extraction, and traditional ML models.
tensorflow/keras or pytorch: For building deep learning models.
nltk/spacy: For advanced text preprocessing.
Would you like a complete example file or more informat