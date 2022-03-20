dict = {
    'Name': 'Zara',
    'Age': '7',
    'Class': 'First',

    'dic_interno': {
        'teste': 'Teste de dicionário',
    },

    'Lista de nada': ['nada01', 'nada02', 'teste de lista'],

    ('teste'): 'teste de tupla'


}


dict2 = {
    'Name': 'Zara',
    'Age': '8'
}

dict_copia = dict.fromkeys('Name')

print(dict_copia)
