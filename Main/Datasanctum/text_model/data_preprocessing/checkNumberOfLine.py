jsonl_file = "D:/arxiv-metadata-oai-snapshot.json"

total_lines = sum(1 for _ in open(jsonl_file, "r", encoding="utf-8"))

print(f"file: {total_lines}")
