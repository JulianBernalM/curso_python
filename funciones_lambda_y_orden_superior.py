# Lambda son funciones anónimas ya que no tienen identificador o nombre.
# Aqui un ejemplo basico con un programa que nos dice si una palabra es palindromo.

# def run():
#     palindromo = lambda string: string == string[::-1]
#     print (palindromo('ana'))


# if __name__=='__main__':
#     run()

# la funcion de orden superior es la que recibe como parametro otra funcion y 
# hace algo con ella.


# def saludo(func):
#     func()

# def hola():
#     print ('Hola a todos')

# def adios():
#     print ('Chao')

# saludo(hola)
# saludo(adios)

# Existen 3 funciones de orden superior:
# 1. filter()
# En el siguiente ejemplo solo quiere conocer los numeros impares de la lista my_list

# my_list = [1,9,4,7,3,6,10]

# impars_nums = list(filter(lambda x : x%2 !=0, my_list))
# print (impars_nums)

# 2. map()
# En el siguiente ejemplo quiero conocer los numeros de la lista my_list pero elevados al 
# cuadrado

from functools import reduce


# my_list = [1,9,4,7,3,6,10]

# high_numbers = list(map(lambda x : x**2, my_list))
# print (high_numbers)

# 3. reduce()
# En el siguiente ejemplo quiero conocer el resultado de la multiplicacion 
# de cada uno de los numeros de una lista.

my_list = [2,2,2,2,2]

# a)Inicialmente, se llama a la función con los dos primeros elementos 
# de la secuencia (2,2) y se devuelve el resultado (4).

# b)Se vuelve a llamar a la función con el resultado obtenido en 
# el paso 1 (4) y el siguiente valor de la secuencia (2). 
# Este proceso se repite hasta que hay elementos en la secuencia.

list_multiplication = reduce(lambda a,b: a*b, my_list)
print (list_multiplication)

