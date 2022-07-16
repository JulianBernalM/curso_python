# Lambda son funciones anónimas ya que no tienen identificador o nombre.
# Aqui un ejemplo para con un programa que nos dice si una palabra es palindromo.

palindromo = lambda string: string == string[::-1]

print (palindromo('ana'))