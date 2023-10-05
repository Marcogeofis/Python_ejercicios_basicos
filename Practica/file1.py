import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dict_data2 = {
    'edad': [10,9,13,14,12,11,12],
    'cm': [115,110,130,155,125,120,125],
    'pais': ['co','mx','co','mx','mx','ch','ch'],
    'genero': ['M','F','F','M','M','M','F'],
    'Q1': [5,10,8,np.nan,7,8,3],
    'Q2': [7,9,9,8,8,8,9.0]
}
dict_data2

columns = ['Ana','Benito','Camilo','Daniel','Erika','Fabian','Gabriela']

df = pd.DataFrame(dict_data2, index=columns)

paises = df[df['pais'].isin(['cm', 'mx']).tolist()]
"""response paises
        edad   cm pais genero    Q1   Q2
Benito     9  110   mx      F  10.0  9.0
Daniel    14  155   mx      M   NaN  8.0
Erika     12  125   mx      M   7.0  8.0
"""

print(df.describe())


