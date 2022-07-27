def exemplo():
    gram = {
        'S': [['E'], ['E', '+', 'T']],
        'E': [['a', 'JK'], ['substantivo']],
    }

    gramatica = {
        'S': [['NP', 'VP'], ['auxiliar', 'NP', 'VP'], ['VP']],
        'NP': [['a', 'JK'], ['substantivo']],
        'JK': [['b'], ['b', 'JK']],
        'VP': [['c'], ['c', 'NP']],
        'a': ['Z', 'aa', 'a'],
        'b': ['X', 'Y', 'bb', 'cc'],
        'c': ['X', 'dd', 'ee'],
        'auxiliar': ['ff'],
        'd': ['gg', 'to', 'on'],
        'substantivo': ['hh', 'TT']
    }
    terminais = ['a', 'b', 'c', 'auxiliar', 'd', 'substantivo']
