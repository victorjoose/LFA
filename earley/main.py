from earley import Earley


def test():
    """
    grammar = {
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
    terminals = ['Det', 'Noun', 'Verb', 'Aux', 'Prep', 'Proper-Noun']
    earley = Earley(['book', 'that', 'flight'], grammar, terminals)
    """

    grammar = {
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
    terminals = ['a', 'b', 'c', 'auxiliar', 'd', 'substantivo']
    earley = Earley(['X', 'Z', 'Y'], grammar, terminals)

    earley.parse()
    print(earley)


if __name__ == '__main__':
    test()


