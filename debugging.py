# Funcion que recibe un numero como parametro y retorna una lista
# con todos los divisores de este numero

# def divider(number):
#     list = [i for i in range(1,number+1) if number%i == 0]
#     return list


# def run():
#     number = int(input('Ingrese un numero: '))
#     print (divider(number))
#     print ('Termino mi programa')


# if __name__=="__main__":
#     run()

# Para hacer un Debugging debo recorrer el programa linea por linea hasta encontrar el error
# El Debugging se encuentra en la parte izquierda de VSC.
# Tambien podre agregar un BreackPoint donde se pausara el programa despues de ejecutarse con el Debug.

# Poniendo a prueba el manejo de excepciones.
# Programa que permite ingresar un numero y darnos como resultado los 
# numeros que son divisibles por ese numero
# ¿Que pasaria si el usuario ingresara una letra o un numero negativo?

def divider(number):
    try:
        if number < 0:
            raise ValueError("Solo numeros positivos")
        list = [i for i in range(1,number+1) if number%i == 0]
        return list
    except ValueError as V:
        print (V)
        return False

def run():
    try:
        number = int(input('Ingrese un numero: '))
        print (divider(number))
    except ValueError:
        print ('Solo puede ingresar numeros')        
        print ('Termino mi programa')


if __name__=="__main__":
    run()