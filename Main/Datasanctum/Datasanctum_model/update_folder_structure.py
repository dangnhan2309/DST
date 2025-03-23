import os
import json

class FolderMapper:
    def __init__(self, folder_path, json_path):
        self.folder_path = folder_path
        self.json_path = json_path

    def map_folder(self):
        folder_structure = {
            "ProgramName": os.path.basename(self.folder_path),
            "Topics": self._map_directory(self.folder_path)
        }
        self._write_to_json(folder_structure)

    def _map_directory(self, path):
        topics = []
        for root, dirs, files in os.walk(path):
            for dir_name in dirs:
                topic = {
                    "TopicName": dir_name,
                    "SubTopics": self._map_subtopics(os.path.join(root, dir_name)),
                    "Files": self._list_files(os.path.join(root, dir_name))
                }
                topics.append(topic)
            # Liệt kê các file trong folder đang xét
            if files:
                topics.append({
                    "Files": self._list_files(root)
                })
            break  # Chỉ duyệt cấp đầu tiên
        return 0

    def _map_subtopics(self, path):
        subtopics = []
        for root, dirs, files in os.walk(path):
            for dir_name in dirs:
                subtopic = {
                    "SubTopicName": dir_name,
                    "SubTopics": self._map_subtopics(os.path.join(root, dir_name)),
                    "Files": self._list_files(os.path.join(root, dir_name))
                }
                subtopics.append(subtopic)
            break  # Chỉ duyệt cấp đầu tiên
        return subtopics

    def _list_files(self, path):
        return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    def _write_to_json(self, data):
        with open(self.json_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
    def _update_(folder_path,json_path): 
        mapper = FolderMapper(folder_path, json_path)
        mapper.map_folder()
        print("Successful")

def main(): 
    print("dang thuc hien")
    folder_path = r"C:\Users\Marco\Desktop\dst"
    json_path = r"C:\Users\Marco\Desktop\dst\cautruc_folder.json"
    print("dang thuc hienamp ")

    mapper = FolderMapper(folder_path, json_path)
    mapper.map_folder()
    print("Successful")
if __name__ == "__main__":
    main() 
