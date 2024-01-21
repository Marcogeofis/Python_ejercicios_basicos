import PyPDF2

reader = PyPDF2.PdfReader('4.pdf')
page = reader.pages[0]
print(page.extract_text(0, 99))
