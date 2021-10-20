#texto = input("¿Cual es el indice  texto?")
texto = "abcdefghijklmnopqrstuvwxyz"
print('' + texto)
print('Upper ' + texto.upper())
print('Capitalize' + texto.capitalize())
print('Lower ' + texto.lower())
print('Strip ' + texto.strip())
print('[0:3] ' + texto[0:3])  # Desde el indice 0 hasta antes del 3
print('[:3] ' + texto[:3])  # Desde el indice principio hasta antes del 3
print('[3:] ' + texto[3:])  # Desde el indice 3 hasta el indice final
print('[1:7] ' + texto[1:7])  # Desde el indice 1 hasta el indice 7
print('[::] ' + texto[::])  # Desde el indice principio al final
# Desde el indice 1 hasta el indice 20 en pasos de 2 en 2
print('[1:20:2] ' + texto[1:20:1])
# Desde el indice principio al final en pasos inversos
print('[::-1] ' + texto[::-1])
print('[1::3] ' + texto[1::3])  # Desde el indice 1 al final en pasos de 3
