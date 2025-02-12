from bert import Emberding
from labels_ML import ml_topics 
import json
import os

topic_emberding_path = r"D:\DST\Main\Main_program\topic_emberding.json"

def saving_into_json(topic, embedding_code, path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}  #
        data = {}

    data[topic] = {
        "topic_emberding_code": embedding_code.tolist(),
        "description": "empty",
        "des_emberding": []
    }

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def main(): 
    for topic_name in ml_topics: 
        emberding_code = Emberding.create_embedding(topic_name)
        print(topic_name)
        print(emberding_code.shape)
        #saving_into_json(topic_name, emberding_code, topic_emberding_path)

if __name__ == "__main__":
    main()
