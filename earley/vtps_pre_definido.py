def variaveis_nao_terminais_pre_definida():
    V = {'E', 'F', 'T'}
    return V


def terminais_pre_definidos():
    T = {'(', ')', '*', '+', 'x'}
    return T


def gramatica_pre_definida():
    P = [
        ['E', ['T']], ['E', ['E', '+', 'T']],
        ['T', ['F']], ['T', ['T', '*', 'F']],
        ['F', ['(', 'E', ')']], ['F', ['x']]
    ]
    return P


def palavra_inicial_pre_definida():
    return 'E'
