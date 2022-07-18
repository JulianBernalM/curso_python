# Puedo utilizar listas y diccionarios anidados, es decir listas en diccionarios
# y diccionarios en listas asi:

def run():
    my_list = [1,'Julian', True, 5.5]
    my_dict = {'firstname': 'Daniela', 'Lastname': 'Cardona'}

    #Lista de diccionarios:
    super_list = [
        {'firstname': 'Daniela', 'Lastname': 'Mendonza'},
        {'firstname': 'Juan', 'Lastname': 'Marin'},
        {'firstname': 'Andres', 'Lastname': 'Arica'},
        {'firstname': 'Julian', 'Lastname': 'Bernal'}
    ]

    # Para imprimir la lista con sus diccionarios:
    for i in super_list:
        print (i['firstname'], i['Lastname'])

    #Diccionaro de listas:
    super_dict = {
        'natural_nums': [1,2,3,4,5],
        'integer_nums': [4,3,-1-4,4],
        'floating_nums': [1.1, 3.5, 8.6]
    }

    #Para imprimir el diccinario con sus listas:
    # for key, value in super_dict.items():
    #     print (key, '-', value)


if __name__=='__main__':
    run()