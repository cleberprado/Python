# -*- coding: utf-8 -*-
"""0005.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16uXMjSmPuv70_8muPPg1rFskX6ML-hnL
"""

numeros = list(range(0, 21))
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros_pares)

numeros_impares = list(filter(lambda x: x % 2 != 0, numeros))
print(numeros_impares)