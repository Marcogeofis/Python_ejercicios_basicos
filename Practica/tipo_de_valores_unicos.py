""" Valores unicos 2

Given an array of integers, where all elements but one occur twice, find the unique element.
Example:

a = [1,2,3,4,3,2,1]

the unique element is 4.
"""


def lonelyinteger(a):
  array = onlyIntegers(a)
  countElement = {}
  onlyElement = 0
  for el in array:
    if el in countElement:
      countElement[el] += 1
    else:
      countElement[el] = 1
  
  for key, value in countElement.items():
    if value == 1:
      onlyElement = key
      
  return onlyElement

def onlyIntegers(a):
  allIntegers = [x for x in a if isinstance(x, int)]
  if len(allIntegers) == len(a):
    print("El arreglo contiene solo enteros.")
  else:
    print("El arreglo contiene elementos no enteros.")
  return allIntegers

if __name__ == "__main__":
    a = [1,2,3,4,3,2,1]
    unique_ele = lonelyinteger(a)
    print(f'El unico valor es {unique_ele} isde tipo {type(unique_ele)}')
