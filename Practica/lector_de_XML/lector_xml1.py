#no se requiere instalr xml.etree.ElementTree

import pandas as pd
import xml.etree.ElementTree as ET

#Especificar ruta del xml
PATH_xml = 'texto.xml'

#Parsea el archivo XML
tree = ET.parse(PATH_xml)
root = tree.getroot()

# Crea listas para almacenar los datos

nombres = []
edades = []
ciudades = []

# Iterar sobre los elementos del XML
for registro in root.findall('registro'):
    nombre = registro.find('nombre').text
    edad = int(registro.find('edad').text)
    ciudad = registro.find('ciudad').text
    
    # Añadir los datos a las listas
    nombres.append(nombre)
    edades.append(edad)
    ciudades.append(ciudad)

# Crear un dataFrame de pandas
df = pd.DataFrame({
    'Nombre': nombres,
    'Edad': edades,
    'Ciudad': ciudades
})

# Imprime el DataFrame
print(df)