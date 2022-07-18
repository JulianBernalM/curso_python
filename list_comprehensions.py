    #Crear una lista con los primeros 100 numeros al cuadrado

# def run():
#     nums = []

#     for i in range(1,101):
#         nums.append(i**2)
#     print (nums)
        


# if __name__=='__main__':
#     run()

#Guardar solo el cuadrado de los numeros que no sean divisibles entre 3

# def run():
#     nums = []

#     for i in range(1,101):
#         if i % 3 != 0:
#             nums.append(i**2)
#     print (nums)
        


# if __name__=='__main__':
#     run()

#Ahora usando list comprehensions:

# def run():
#     nums = [i**2 for i in range(1,11) if i % 3 != 0]

#     print (nums)

# if __name__=='__main__':
#     run()


# Crear con una list comprehension, una lista de los multiplos de 4
# que a la vez son multiplos de 6 y de 9, hasta 5 digitos

# def run():
#     new_list = [i for i in range (1,100000) if i%4 == 0 and i%6 == 0 and i%9 == 0]
#     print (new_list)

# if __name__=='__main__':
#     run()



