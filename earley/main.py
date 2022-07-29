import earley
import vtps_pre_definido

CRED = '\033[91m'
CEND = '\033[0m'

def test():
    global gramatica, terminais, variavel_inicial
    variaveis_nao_terminais = {}
    gramatica = []
    palavra_inicial = ''

    escolha = input(CRED + "\n\nPor favor, escolha entre digitar uma gramática (1) ou utilizar uma gramática pré-definida (2)?\n" + CEND)

    if escolha.isdigit():
        if int(escolha) == 1:
            variaveis_nao_terminais, variaveis_terminais, gramatica, palavra_inicial = criar_gramatica()
            imprimeVTPS(variaveis_nao_terminais, variaveis_terminais, gramatica, palavra_inicial)
        elif int(escolha) == 2:
            variaveis_nao_terminais = vtps_pre_definido.variaveis_nao_terminais_pre_definida()
            variaveis_terminais = vtps_pre_definido.terminais_pre_definidos()
            gramatica = vtps_pre_definido.gramatica_pre_definida()
            palavra_inicial = vtps_pre_definido.palavra_inicial_pre_definida()
            imprimeVTPS(variaveis_nao_terminais, variaveis_terminais, gramatica, palavra_inicial)
        else:
            valor_invalido()
    else:
        valor_invalido()

    earley.D0(variaveis_nao_terminais, gramatica, palavra_inicial)
    earley.DRs(variaveis_nao_terminais, gramatica, palavra_inicial)


def criar_gramatica():
    print(CRED + "\nO formato de entrada deve ser A->Bc. \n\n($ pra finalizar)(% = épsilon)\n" + CEND)

    V = {}
    T = {}
    P = []

    while True:
        regra_crua = input("Digite uma regra: ($ para finalizar)")

        if verfica_cifrao(regra_crua):
            break

        regra = remove_espacos(regra_crua)

        if verifica_flecha(regra):
            continue

        regra = remove_flecha(regra)
        regra = trata_epsilon(regra)
        regra = list(regra)

        primeira = regra.pop(0)

        V = set(primeira).union(V)

        for letra in regra:
            if letra.isalpha():
                if letra.isupper():
                    V = set(letra).union(V)
                else:
                    T = set(letra).union(T)
            else:
                T = set(letra).union(T)

        P.append([primeira, regra])

    S = get_variavel_inicial(V)

    return V, T, P, S


def verfica_cifrao(entrada):
    if entrada == "$":
        return True
    else:
        return False


def trata_epsilon(regra):
    return regra.replace("%", "", -1)


def verifica_flecha(regra):
    if (regra[1] + regra[2]) != "->":
        print(CRED + "Formato inválido, por favor, digite novamente.\n" + CEND)
        return True


def remove_flecha(regra):
    return regra.replace("->", "", -1)


def get_variavel_inicial(V):
    while True:
        i = input("Digite a variável inicial: ")
        if i in V:
            return i
        else:
            print("Variável inicial bão está nas variáveis digitadas anteriormente, por favor, digite uma nova variável.")


def escolhe_inicial(gramatica):
    variavel_inicial = input("Digite a variável inicial: ")
    inicial_valida = ''

    for g in gramatica:
        if g[0] == variavel_inicial:
            inicial_valida = variavel_inicial

    if len(inicial_valida) > 0:
        return variavel_inicial
    else:
        escolhe_inicial(gramatica)


def imprimeVTPS(variaveis_nao_terminais, variaveis_terminais, gramatica, palavra_inicial):
    print(f"\tV = {variaveis_nao_terminais}")
    print(f"\tT = {variaveis_terminais}")
    print(f"\tP = {gramatica}")
    print(f"\tS = {palavra_inicial}")


def valor_invalido():
    print(CRED + "\nValor inválido!!!!!\n" + CEND)
    test()


def remove_espacos(regra_crua):
    return regra_crua.replace(" ", "", -1)


if __name__ == '__main__':
    test()
