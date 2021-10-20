#nombre = input("¿Cual es el nombre?")
nombre = "abcdefghijklmnopqrstuvwxyz"
print('' + nombre)
print('Upper ' + nombre.upper())
print('Capitalize' + nombre.capitalize())
print('Lower ' + nombre.lower())
print('Strip ' + nombre.strip())
print('[0:3] ' + nombre[0:3])  # Del indice 0 hasta antes del 3
print('[:3] ' + nombre[:3])  # Del principio hasta antes del 3
print('[3:] ' + nombre[3:])  # Del 3 hasta el final
print('[1:7] ' + nombre[1:7])  # Del 1 hasta el 7
print('[::] ' + nombre[::])  # Del principio al final
print('[1:20:2] ' + nombre[1:20:1])  # Del 1 hasta el 20 en pasos de 2 en 2
print('[::-1] ' + nombre[::-1])  # Del principio al final en pasos inversos
print('[1::3] ' + nombre[1::3])  # Del 1 al final en pasos de 3
