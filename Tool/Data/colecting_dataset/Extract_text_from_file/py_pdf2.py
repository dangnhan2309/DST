import PyPDF2

def extract_text_from_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
file_path = r'D:\DST\Tool\material\Introduction to Machine Learning with Python.pdf'  # Replace with the actual path to your PDF file
text = extract_text_from_pdf(file_path)
print(text)



