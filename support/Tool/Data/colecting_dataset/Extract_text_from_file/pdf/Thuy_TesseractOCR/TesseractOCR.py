from pdf2image import convert_from_path
from PIL import Image
import pytesseract

# Class xử lý OCR cho file PDF
class PDFOCRProcessor:
    def __init__(self, pdf_path, tesseract_cmd=None, lang='eng'):
        self.pdf_path = pdf_path
        self.tesseract_cmd = tesseract_cmd
        self.lang = lang

        # Thiết lập đường dẫn Tesseract nếu cần
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def convert_pdf_to_images(self, dpi=300):
        """Chuyển đổi PDF thành danh sách ảnh"""
        return convert_from_path(self.pdf_path, dpi)

    def extract_text_from_images(self, images):
        """Trích xuất văn bản từ danh sách ảnh"""
        text = ""
        for idx, image in enumerate(images, start=1):
            page_text = pytesseract.image_to_string(image, lang=self.lang)
            text += f"{page_text}\n"
        return text

# Hàm chính
def main():
    # Đường dẫn file PDF
    pdf_file = "material/Sample_for_test/Introduction to Machine Learning with Python.pdf"

    # Đường dẫn Tesseract (tuỳ chọn)
    tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    # Tạo đối tượng xử lý
    processor = PDFOCRProcessor(pdf_path=pdf_file, tesseract_cmd=tesseract_path, lang='eng')

    # Chuyển đổi PDF thành ảnh
    print("Converting PDF to images...")
    images = processor.convert_pdf_to_images()

    # Trích xuất văn bản từ ảnh
    print("Extracting text from images...")
    text = processor.extract_text_from_images(images)

    # In kết quả
    print("OCR Result:")
    print(text)

    # Lưu kết quả ra file
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(text)
    print("OCR result saved to output.txt.")

# Đảm bảo chạy hàm chính khi file được thực thi
if __name__ == "__main__":
    main()
