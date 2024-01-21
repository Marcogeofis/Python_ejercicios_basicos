# Instalar pillow, pytesseract, tesseract y openCV 

#Op: 1
import pytesseract as tess
from PIL import Image

#Op:2
import cv2

#Acorde al vídeo que ví, se ponia la ruta donde se instalo tesseract.exe
#tess.pytesseract.tesseract_cmd = r'PATH/tesseract.exe'


#Op: 1
my_image = Image.open('imagen_texto.png')
txt = tess. image_to_string(my_image)
# my_image.show() Abrira la imagen para comperar la imagen con el texto
print(txt) 


#Op:2 display original image
path_image = 'imagen_texto.png'
imageDisplay = cv2.imread(path_image)
if imageDisplay is not None:
    cv2.imshow('Matlike', imageDisplay)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else: 
    print(f'No se puede cargar la imagen {path_image}')