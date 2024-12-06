import os
import tkinter
def list_files_in_directory(directory_path):
    try:
        # Lấy danh sách tất cả các tệp và thư mục trong thư mục chỉ định
        files = os.listdir(directory_path)
        
        # Lặp qua và in ra tên từng tệp hoặc thư mục
        for file in files:
            print(file)
    except FileNotFoundError:
        print("Thư mục không tồn tại.")
    except Exception as e:
        print("Đã xảy ra lỗi:", e)

# Thay 'your_directory_path' bằng đường dẫn đến thư mục bạn muốn quét
directory_path = 'your_directory_path'
list_files_in_directory(directory_path)