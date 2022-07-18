# Proyecto con una lista de diccionarios ya definidos y desde el cual
# voy a filtrar, segun mis requerimientos.
# Voy a usar: lista de diccionarios - funciones lambda - funciones de orden superior.

DATA = [
    {
    'name': 'Facundo',
    'age': 72,
    'organization': 'Platzi',
    'position': 'Technical Coach',
    'language': 'python',
    },
    {
    'name': 'Luisana',
    'age': 33,
    'organization': 'Globant',
    'position': 'UX Designer',
    'language': 'javascript',
    },
    {
    'name': 'Héctor',
    'age': 19,
    'organization': 'Platzi',
    'position': 'Associate',
    'language': 'ruby',
    },
    {
    'name': 'Gabriel',
    'age': 20,
    'organization': 'Platzi',
    'position': 'Associate',
    'language': 'javascript',
    },
    {
    'name': 'Isabella',
    'age': 30,
    'organization': 'Platzi',
    'position': 'QA Manager',
    'language': 'java',
    },
    {
    'name': 'Karo',
    'age': 23,
    'organization': 'Everis',
    'position': 'Backend Developer',
    'language': 'python',
    },
    {
    'name': 'Ariel',
    'age': 32,
    'organization': 'Rappi',
    'position': 'Support',
    'language': '',
    },
    {
    'name': 'Juan',
    'age': 17,
    'organization': '',
    'position': 'Student',
    'language': 'go',
    },
    {
    'name': 'Pablo',
    'age': 32,
    'organization': 'Master',
    'position': 'Human Resources Manager',
    'language': 'python',
    },
    {
    'name': 'Lorena',
    'age': 56,
    'organization': 'Python Organization',
    'position': 'Language Maker',
    'language': 'python',
    },
]


def run():
    # A.
    # Quiero conocer solo los nombres de los programadores de python usando list_comprehensions
    name_python_programmer = [programer['name'] for programer in DATA if programer['language']=='python']
    # print (name_python_programmer)
    print ('\n')

    # B.
    # Quiero conocer todos los trabajadores de Platzi usando list_comprehensions
    platzi_workers = [worker['name'] for worker in DATA if worker['organization']=='Platzi']
    # print (platzi_workers)

    # C.
    # Quiero crear una lista con todos los adultos, usando funciones de orden superior y lambdas
    adult_worker = list(filter(lambda worker:worker['age']>18, DATA))
    #print (adult_worker)
    # Ahora solo quiero que se muestren los nombres de los trabajadores.
    adult_worker = list(map(lambda worker:worker['name'], adult_worker))

    # D.
    # Crear una nueva lista de diccionarios llamada old que tendra true o false
    # si la persona es mayor o menor de 30 años.
    # Utilizamos el simbolo | para unir un nuevo diccionario
    old_worker = list(map(lambda worker:worker | {'old':worker['age']>70}, DATA))

    for worker in old_worker:
        print (worker)


if __name__=='__main__':
    run()