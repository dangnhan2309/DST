import os
import json

jsonl_file = "D:/arxiv-metadata-oai-snapshot.json"

# Đếm số abstract
abstracts_count = 0

# Đọc file JSONL
with open(jsonl_file, "r", encoding="utf-8") as file:
    for line in file:
        try:
            data = json.loads(line)
            if "abstract" in data and data["abstract"].strip():
                abstracts_count += 1
        except json.JSONDecodeError:
            print(f"⚠️ Lỗi khi đọc dòng: không phải JSON hợp lệ.")

# In ra số lượng abstract
print(f"Tổng số abstract có trong file: {abstracts_count}")
