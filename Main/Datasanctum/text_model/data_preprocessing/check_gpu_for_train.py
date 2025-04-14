import torch

print("🔥 GPU có khả dụng không?", torch.cuda.is_available())
print("🚀 Số lượng GPU:", torch.cuda.device_count())

if torch.cuda.is_available():
    for i in range(torch.cuda.device_count()):
        print(f"🎮 GPU {i}: {torch.cuda.get_device_name(i)}")
