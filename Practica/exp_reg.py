"""
Expresiones Regulares.

Las expresiones regulares se usan en las cadenas de carácteres para poder hacer: extracciones, remplazar,
buscar metacarácteres.

\d  -Digitos (0-9)
\D  -No digitos
\W  -Alfanumérico (a-z, A-Z, 0-9)
\w  -No alfanumérico
\s  -Espacios en blanco (tab, nueva línea)
\S  -No espacios en blanco (tab, nueva línea)
\.  -Cualquier carácter excepto nueva línea
^   -Inicio de una cadena de carácteres
$   -Fin de una cadena de carácteres
\   -Cancela carácteres especiales
"""

import re

texto = """ 
    Hola Mundo.
    Me gusta python!!
    Mi número de la suerte es 888
    Mi segundo número de la sierte es 769-871
    Mi tercere número de la suerte es 912-456-787
"""

print(re.search(r'\d', texto)) # <re.Match object; span=(70, 71), match='8'>
print(re.findall(r'\d', texto)) # ['8', '8', '8', '7', '6', '9', '8', '7', '1', '9', '1', '2', '4', '5', '6', '7', '8', '7']
print(re.search(r'Mundo.$', texto, flags=re.M)) # <re.Match object; span=(11, 17), match='Mundo.'>


