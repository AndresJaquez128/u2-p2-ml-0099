import numpy as np 
# Jaquez Andres NC 0074 fecha 22 octubre 2026
#ejemplos de numpy numerical python
print("---- Espaciado linealmente en array---- 0074")
arre=np.linspace(start=0,stop=1,num=5)
print(arre)
print("-- Matriz identidada en 2D array-- 0074")
matriz=np.eye(3)
print(matriz)
print("--genera numeros al azar(aleatorio) 2D array--0074")
numale=np.random.random((3,4))  #genera 12 numeros aleatorios
print(numale) 
print("genera 12 numeros aleatorios entre 0 y 1")
numale=np.random.random((3,3))  #genera 12 numeros aleatorios
print(numale) 
# como generar 9 numeros aleatorios  comprendidos entre 1 y 20
## con numpy en arreglo de 3 en 3
print("genera 9 numeros aleatorios entre 1 y 20")
arre=np.random.randint(1,21, size=9).reshape(3,3)
print(arre)
print("Jaquez Andres NC 0074")