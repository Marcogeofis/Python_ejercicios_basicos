from PyPDF2 import PdfReader
# ignorando el header y footer
reader = PdfReader('4.pdf')
page = reader.pages[3]

parts = []

def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if y > 50 and y < 720:
        parts.append(text)
        
page.extract_text(visitor_text=visitor_body)
text_body = "".join(parts)

print(text_body)