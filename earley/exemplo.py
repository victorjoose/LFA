def gramatica_pre_definida():
    P = {
        'S': [['NP', 'VP'], ['Aux', 'NP', 'VP'], ['VP']],
        'NP': [['Det', 'Nominal'], ['Proper-Noun']],
        'Nominal': [['Noun'], ['Noun', 'Nominal']],
        'VP': [['Verb'], ['Verb', 'NP']],

        'Det': ['that', 'this', 'a'],
        'Noun': ['book', 'flight', 'meal', 'money'],
        'Verb': ['book', 'include', 'prever'],
        'Aux': ['does'],
        'Prep': ['from', 'to', 'on'],
        'Proper-Noun': ['Houston', 'TWA']
    }

    gramatica = [
        ['E', ['G', '+', 'H']],
        ['G', ['H']],
        ['H', ['I', '*', 'J']],
        ['I', ['F']],
        ['F', ['(', 'E', ')']],
        ['J', ['x']],

        ['(', '/'],
        [')', '/'],
        ['*', '/'],
        ['+', '/'],
        ['x', '/'],
    ]
    return gramatica


def terminais_pre_definidos():
    terminais = ['Det', 'Noun', 'Verb', 'Aux', 'Prep', 'Proper-Noun']
    terminais = ['(', ')', '*', '+', 'x']

    return terminais


def palavra_inicial():
    return 'E'


def variaveis_nao_terminais():
    nao_terminais = ['E', 'F', 'T']
    return nao_terminais
