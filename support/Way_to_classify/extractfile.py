import fitz  # PyMuPDF
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
def extract_content(file_path):
    try:
        if file_path.endswith('.pdf'):
            return extract_pdf_content(file_path)
        elif file_path.endswith(('.png', '.jpg', '.jpeg')):
            return extract_image_content(file_path)
        else:
            return extract_text_content(file_path)
    except Exception as e:
        return f"Error {str(e)}"

def extract_pdf_content(file_path):
    pdf_document = fitz.open(file_path)
    text_data = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text_data += page.get_text()
    return text_data

def extract_image_content(file_path):
    print("Extracting image content")
    image = Image.open(file_path)
    # Sử dụng ngôn ngữ cụ thể nếu cần, ví dụ: 'eng' cho tiếng Anh
    text_data = pytesseract.image_to_string(image, lang='eng')
    print(f"Extracted text: {text_data}")
    return text_data

def extract_text_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text_data = file.read()
    return text_data

def main():
    ##file_path = 'D:\\Planner 100 Ngày Học TA.pdf'
    file_path ="C:\\Users\\DELL\\Downloads\\img\\unlockyour.png"
    ##file_path = 'C:\\Users\\DELL\\OneDrive\\Desktop\\thu.txt'
    content = extract_content(file_path)
    print(content)

if __name__ == "__main__":
    main()