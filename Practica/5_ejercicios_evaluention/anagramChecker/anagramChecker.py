"""
La palabra nacionalista es un anagrama de la palabra altisonancia. mi versión.

Mi código resuelve el problema de verificar si dos palabras son anagramas,
pero se puede mejorar en términos de eficiencia y claridad.

Sugerencias:

Puedes simplificar la verificación de anagramas utilizando directamente las funciones sorted() y ==.
Evitar Bucles Innecesarios: No necesitas convertir las palabras en listas explícitamente ni recorrerlas para comparar elementos.
Mejor Nombres de Funciones: Los nombres de las funciones deben seguir las convenciones de nombres en Python (snake_case).

"""


def anagramCheker(word1, word2):
    long_word1 = len(word1)
    long_word2 = len(word2)
    w1 = []
    w2 = []
    if long_word1 == long_word2:       
        for i in word1:
            w1.append(i)

        for j in word2:
            w2.append(j)

        w1 = sorted(w1)
        w2 = sorted(w2)
        
    for i in range(long_word1):
        if w1[i] == w2[i]:
            return True
        else:
            return False
        
def isAnagram(param):
    if param:
        print('The words are anagram')
    else:
        print('The words are not anagram')




if __name__ == '__main__':
    word1 = 'nacionalista'
    word2 = 'altisonancia'


    print(sorted(word1)) # desde un inicio se puede ordenear una cadena de texto 
    result = anagramCheker("hello", "world")
    isAnagram(result)

