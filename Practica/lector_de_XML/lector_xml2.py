import pandas as pd
import xml.etree.ElementTree as ET

path = 'texto2.xml'

tree_ej2 = ET.parse(path)
root = tree_ej2.getroot()

ids = []
nombres = []
puestos = []

for empleado in root.findall('empleado'):
    id = int(empleado.find('id').text)
    nombre = empleado.find('nombre').text
    puesto = empleado.find('puesto').text
    
    ids.append(id)
    nombres.append(nombre)
    puestos.append(puesto)
    
df_empleados = pd.DataFrame({
    'ID': ids,
    'Nombre': nombres,
    'Puesto': puestos
})

print(df_empleados)