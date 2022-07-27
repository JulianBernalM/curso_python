# TRY - EXCEPT
# De esta manera nos saldra un error en la consola
# def palindrome(word):
#     return word == word[::-1]


# print (palindrome(1))

# Pero si manejo el try except lo podre manejar
# def palindrome(word):
#     return word == word[::-1]


# try:
#     print (palindrome(1))
# except TypeError: #Solo funciona para excepciones de tipo TypeError
#     print ('Debe ingresar una palabra')

# RAISE
# ¿Que pasaria si el usuario nos ingresa un string vasío?
# Se envuelve con un try-except todo el código de la función y se agrega un raise
# Raise Eleva una excepción (error) de tipo ValueError y nos permite agregarle un 
# mensaje a ese error.
# def palindrome(word):
#     try:
#         if len(word) == 0:
#             raise ValueError('No se puede ingresar una cadena vacía')
#         return word == word[::-1]
#     except ValueError as ve:
#         print(ve)
#         return False


# try:
#     print (palindrome('ana'))
# except TypeError: #Solo funciona para excepciones de tipo TypeError
#     print ('Debe ingresar una palabra')

# FINALLY
# Se usa al final de una estructura try-except para poder cerrar un archivo, 
# cerrar una conexión de una base de datos o liberar recursos externos
# try:
#     f = open('archivo.txt')
# finally:
#     f.close()




