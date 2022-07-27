from earley import Earley


def test():

    palavras = []

    escolha = input("Escolha entre digitar uma gramática (1) ou uma pré definida (2)?")

    if int(escolha) and escolha is not None:
        if escolha is 1:
            gramatica = criar_regras(True)
        else:
            gramatica = {}
            terminais = ['( , )', '*', '+', 'x']

    earley = Earley(palavras, gramatica, terminais)

    earley.parse()
    print(earley)


def criar_regras(digitando):
    regras = []
    while digitando is True:
        regraCrua = input("Digite uma regra: (Formato A->Bc) ($ pra finalizar)")
        ehCifrao = verfica_cifrao(regraCrua)

        if ehCifrao is True and len(regras) == 0:
            print("\n\n\tGramática vazia, por favor digite uma gramática não vazia\n\n")
        elif ehCifrao is True and len(regras) > 0:
            digitando = False

        if not ehCifrao:
            if "->" not in regraCrua and digitando is True:
                formato_invalido(digitando)
            regra = processaGramatica(regraCrua)
            regras.append(regra)
    return regras


def processaGramatica(regraCrua):
    regraCrua = regraCrua.split("->")

    if len(regraCrua) != 2:
        formato_invalido(True)

    regra = []

    for reg in regraCrua:
        r = reg.replace(' ', '')
        regra.append(r)

    variavel_nao_terminal = regra[0]
    variaveis = regra[1]
    lsVariaveis = list(variaveis)
    regra = [variavel_nao_terminal, lsVariaveis]
    return regra


def verfica_cifrao(entrada):
    if entrada == "$":
        return True
    else:
        return False


def formato_invalido(digitando):
    print("Formato inválido, por favor, digite um formato válido")
    criar_regras(digitando)


if __name__ == '__main__':
    test()
