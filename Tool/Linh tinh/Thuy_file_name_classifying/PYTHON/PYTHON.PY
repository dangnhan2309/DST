import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
import os
import shutil
from tkinter import filedialog

# Tạo cửa sổ ứng dụng Tkinter
root = TkinterDnD.Tk()
root.title("Data Sanctum")
root.geometry("400x300")

# Đặt icon cho cửa sổ từ file .png

# Biến lưu thư mục gốc
base_path = ""

# Hàm để người dùng chọn thư mục lưu
def choose_directory():
    global base_path
    base_path = filedialog.askdirectory()  # Mở cửa sổ chọn thư mục
    if base_path:  # Nếu người dùng chọn thư mục
        label.config(text=f"Chosen directory: {base_path}")
    else:
        label.config(text="No directory selected!")

# Thêm nhãn để hướng dẫn người dùng
label = tk.Label(root, text="Drag and drop a file here", font=("Comic Sans MS", 12))
label.pack(pady=20)

# Hàm phân loại và di chuyển file vào thư mục đã chọn
def classify_and_move_file(file_path):
    if not base_path:  # Kiểm tra nếu người dùng chưa nơi chứa file
        label.config(text="Please choose a directory first!")
        return
    # basename: sử dụng để lấy tên file từ một đường dẫn đầy đủ (path), tức là phần cuối cùng của đường dẫn.
    file_name = os.path.basename(file_path)  # Lấy tên file gốc
    #splitext():dùng để tách tên file thành hai phần: phần tên file và phần mở rộng (đuôi file).
    file_extension = os.path.splitext(file_name)[1].lower()  # Lấy phần mở rộng .docx 
    main_folder_name = os.path.splitext(file_name)[0].lower()  # Lấy tên file và chuyển thành chữ thường

    # Tìm thư mục có tên chứa một phần của main_folder_name (không phân biệt hoa thường)
    target_main_folder = None
    # os.listdir() là một hàm trong module os, nó trả về một danh sách các mục (tên file và thư mục) trong thư mục được chỉ định.
    for folder in os.listdir(base_path):
        # os.path.join(base_path, folder) sẽ nối base_path và folder lại thành một đường dẫn đầy đủ đến thư mục hoặc file.
        # os.path.isdir(path) là một hàm trong module os.path, dùng để kiểm tra xem đường dẫn path có phải là một thư mục không.
        if os.path.isdir(os.path.join(base_path, folder)) and folder.lower() in main_folder_name:
            target_main_folder = os.path.join(base_path, folder)
            break
    # Nếu chưa có thư mục chứa tên file, tạo thư mục mới
    if not target_main_folder:
        target_main_folder = os.path.join(base_path, main_folder_name)
        os.makedirs(target_main_folder)

    # Tạo thư mục con theo phần mở rộng (đuôi file) trong thư mục chính
    if file_extension:
        sub_folder = file_extension[1:]  # Lấy tên thư mục là phần mở rộng không có dấu "."
    else:
        sub_folder = "others"  # Nếu không có đuôi file
    # Tạo thư mục con trong thư mục chính nếu chưa tồn tại
    target_subfolder = os.path.join(target_main_folder, sub_folder)
    if not os.path.exists(target_subfolder):
        os.makedirs(target_subfolder)

    # Di chuyển file vào thư mục con trong thư mục chính
    target_path = os.path.join(target_subfolder, file_name)
    shutil.move(file_path, target_path)

    # Cập nhật nhãn hiển thị đường dẫn
    label.config(text=f"File moved to: {target_path}")


# Hiển thị nội dung đường dẫn file khi thả vào ứng dụng
def on_drop(event):
    dropped_file = event.data
    classify_and_move_file(dropped_file)

def on_enter(event):
    choose_button.config(bg="#45a049")  # Đổi màu nền khi di chuột vào

def on_leave(event):
    choose_button.config(bg="#4CAF50")  # Quay lại màu nền ban đầu khi di chuột ra

choose_button = tk.Button(
    root,
    text="Choose Directory",
    command=choose_directory,
    bg="#4CAF50",
    fg="white",
    font=("Helvetica", 9, "bold"),
    relief="raised",
    bd=2,
    padx=5,
    pady=5
)

choose_button.pack(pady=20)

# Thêm sự kiện hover
choose_button.bind("<Enter>", on_enter)
choose_button.bind("<Leave>", on_leave)

# Kích hoạt hỗ trợ kéo thả file vào cửa sổ
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', on_drop)

# Chạy ứng dụng
root.mainloop()
