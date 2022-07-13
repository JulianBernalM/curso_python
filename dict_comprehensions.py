import math
# 1. Crear diccionario cuyas llaves sean los 100 primeros numeros naturales
# y cuyos valores sean esos numeros pero elevados al cubo

# def run():
    # my_dict = {}

    # for i in range(1,101):
    #     my_dict[i] = i**3
    
    # print (my_dict)

    #Usando dict comprehensions:
    # my_dict = {i:i**3 for i in range(1,101)}
    # print (my_dict)

# if __name__=='__main__':
#     run()

# 2. Solo guardar en las llaves del diccionario los numeros que no sean 
# divisibles por 3

# def run():
#     # my_dict = {}

#     # for i in range(1,101):
#     #     if i%3 != 0:
#     #         my_dict[i] = i**3

#     # print (my_dict)

#     #Usando dict comprehensions:
#     my_dict = {i:i**3 for i in range(1,101) if i%3 != 0}
#     print (my_dict)

# if __name__=='__main__':
#     run()


# Crear con un diccionary comprehensions, un diccionario cuyas llaves
# sean los 1000 primeros numeros naturales con sus raices cuadradas como valores

def run():
    my_dic = {i:round(math.sqrt(i),2) for i in range(1,1001)}
    print (my_dic)


if __name__=='__main__':
    run()


    