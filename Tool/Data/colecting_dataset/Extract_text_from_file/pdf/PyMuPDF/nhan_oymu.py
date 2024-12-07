import fitz 

class fitz_extract: 
	def __init__(self,path): 
		self.path = path
	def extraxt_text(self) : 
		pdf = fitz.open(self.path)
		for page in pdf: 
			print(page.get_text())


def main(): 
	text = fitz_extract(r'D:\DST\Tool\material\Introduction to Machine Learning with Python.pdf')
	text.extraxt_text()

if __name__ == "__main__":
	main() 
