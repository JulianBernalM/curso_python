# Lambda son funciones anónimas ya que no tienen identificador o nombre.
# Aqui un ejemplo basico con un programa que nos dice si una palabra es palindromo.

# def run():
#     palindromo = lambda string: string == string[::-1]
#     print (palindromo('ana'))


# if __name__=='__main__':
#     run()

# la funcion de orden superior es la que recibe como parametro otra funcion y 
# hace algo con ella.

def saludo(func):
    func()

def hola():
    print ('Hola a todos')

def adios():
    print ('Chao')

saludo(hola)
saludo(adios)

# Existen 3 funciones de orden superior:
# 1. filter()


