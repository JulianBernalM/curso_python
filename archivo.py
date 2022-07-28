# Lee un archivo que contiene una serie de numeros
# Convierte cada linea en una lista para poderla trabajar
# encoding='utf-8' Nos asegura de que no existan caracteres extraños
 
def read():
    with open('./archivos/numbers.txt', 'r', encoding='utf-8') as f:
        numbers = [int(line) for line in f]

    print(numbers)


# Crea un archivo que contenga en cada linea
# la lista de nombres
# Puedo cambiar el segundo parametro de open por la letra a
# Los elementos que estan en la lista names se agregaran y no es
# sobreescribiran    
 
def write():
    names = ['Julian', 'Adriana', 'Daniela', 'Andrea', 
    'Rocío', 'Birman', 'Rosemberg', 'Catalina', 'Mario']
    
    with open('./archivos/names.txt', 'w', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')


def run():
    write()


if __name__=='__main__':
    run()