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

# A.
# Utilizando filter y maps o listas de orden superior crear las listas
# name_python_programmer (nombre de los programadores de python) y 
# platzi_workers (trabajadores de platzi) los ejercicios A y B.

# B.
# Utilizando list comprehensions crear las listas
# adult_worker y old_worker los ejercicios C y D.

def run():
    # A.Nombre de los programadores de python
    name_python_programmer = list(filter(lambda worker:worker['language']=='python' ,DATA))
    name_python_programmer = list(map(lambda worker:worker['name'], name_python_programmer))

    # Trabajadores de platzi
    platzi_workers = list(filter(lambda worker:worker['organization']=='Platzi', DATA))
    platzi_workers = list(map(lambda worker:worker['name'], platzi_workers))

    # B. Adult_worker (trabajadores mayores de 18)
    adult_worker = [worker['name'] for worker in DATA if worker['age'] >= 18]
    
    # Crear una nueva lista de diccionarios llamada old worker que tendra true o false
    old_worker = [worker | {'old': worker['age']>70} for worker in DATA]

    for worker in old_worker:
        print (worker)


if __name__=='__main__':
    run()