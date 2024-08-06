import PyPDF2

pdf_file = open('/home/jahrebel/Documentos/Lenguejes_Programacion/Python/Libros_sobre_Pytho/pandas.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
print(pdf_reader.documentInfo)
