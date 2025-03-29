import os

packages = [
    "nltk",
    "tqdm",
    "bertopic",
    "sentence-transformers",
    "hdbscan"
]

for package in packages:
    os.system(f"pip install {package}")
