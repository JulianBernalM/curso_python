# Probando assert con proyecto palindromo
# def palindrome(string):
      # Afirmo que esta condición es verdadera, sino imprimo este mensaje de error:  
#     assert len(string) > 0, 'No se puede ingresar una cadena vacía'
#     return string == string [::-1]

# print (palindrome(''))

# Probando assert con proyecto divisores cuando el usuario ingresa una palabra
# def divider(number):
#     list = [i for i in range(1,number+1) if number%i == 0]
#     return list


# def run():
#     number = input('Ingrese un numero: ')
#     assert number.isnumeric(), 'Ingrese un numero entero'
#     print (divider(int(number)))


# if __name__=="__main__":
#     run()

# Probando assert con proyecto divisores cuando el usuario ingresa un numero negativo
# def divider(number):
#     list = [i for i in range(1,number+1) if number%i == 0]
#     return list


# def run():
#     number = int(input('Ingrese un numero: '))
#     assert number > 0, 'Ingrese un numero entero'
#     print (divider(int(number)))


# if __name__=="__main__":
#     run()

# Probando assert con proyecto divisores cuando... 
# El usuario ingresa un numero negativo
# El usuario ingreso una letra
# El usuario ingreso un string vacío
 
def divisors(num):
    try:
        if type(num) != int:
            raise TypeError('That is not a int type value.')
        
        divs = [i for i in range(1, num + 1) if num % i == 0]
        return divs

    except TypeError as ve:
        print(ve)
        return ve
    finally:
        print('finally divisors')


def run():
    try:
        num = int(input('Enter a number: '))
        assert num > 0, "It's not a positive number"
        
        print(divisors(num))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    else:
        print('run() is ok')


if __name__ == '__main__':
	run()