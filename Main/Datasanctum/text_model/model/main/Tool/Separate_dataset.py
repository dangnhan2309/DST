import os
import json
from re import X

# File gốc và nơi lưu
jsonl_file = "D:/arxiv-metadata-oai-snapshot.json"
save_dir = r"D:\DataSanctum\Model\Dataset"
output_file = os.path.join(save_dir, "abstracts80k.json")

# Tạo thư mục nếu chưa có
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
    print(f"✅ Tạo thư mục: {save_dir}")

abstracts = []

# Đọc file JSONL
with open(jsonl_file, "r", encoding="utf-8") as file:X\


    for line in file:
        try:
            data = json.loads(line)
            if "abstract" in data and data["abstract"].strip():
                abstracts.append(data["abstract"].strip())
            if len(abstracts) >= 80000: 
                break
        except json.JSONDecodeError:
            continue  # Bỏ qua dòng lỗi

# Lưu ra file .json
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(abstracts, f, ensure_ascii=False, indent=2)

print(f"📦 Đã lưu {len(abstracts)} abstracts vào file:\n{output_file}")



0 