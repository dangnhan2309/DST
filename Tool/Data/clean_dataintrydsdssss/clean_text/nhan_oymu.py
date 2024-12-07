from queue import Full
import fitz 

class fitz_extract: 
	def __init__(self,path): 
		self.path = path
	def extraxt_text(self) : 
		pdf = fitz.open(self.path)
		full_text =""
		for page in pdf:
			full_text+= page.get_text() 
		return full_text
			


def main(): 
	text = fitz_extract(r'D:\DST\Tool\material\Introduction to Machine Learning with Python.pdf').extraxt_text()
	print(text)

if __name__ == "__main__":
	main() 
