munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

def dict_unpacker(dict):
    for name, value in dict.items():
        age = dict[name]['age']
        gender = dict[name]['gender']
        print(f'{name} is a {age}-year-old {gender}')


dict_unpacker(munsters)