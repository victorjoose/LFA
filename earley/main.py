from earley import Earley
from entrada import Entrada
import exemplo

CRED = '\033[91m'
CEND = '\033[0m'


def test():
    global gramatica, terminais, variavel_inicial
    palavra = ''

    escolha = input("Por favor, escolha entre digitar uma gramática (1) ou utilizar uma gramática pré-definida (2)?")

    if escolha.isdigit():
        if int(escolha) == 1:
            gramatica_nao_tratada = criar_gramatica(True)
            gramatica_sem_terminais = tratar_regras(gramatica_nao_tratada)
            terminais = cria_terminais(gramatica_nao_tratada)
            gramatica = adiciona_terminais(gramatica_sem_terminais, terminais)
            variavel_inicial = escolhe_inicial(gramatica_nao_tratada)
        elif int(escolha) == 2:
            gramatica = tratar_regras(exemplo.gramatica_pre_definida())
            #gramatica = exemplo.gramatica_pre_definida()
            terminais = exemplo.terminais_pre_definidos()
            variavel_inicial = exemplo.palavra_inicial()
        else:
            valor_invalido()
    else:
        valor_invalido()

    palavra = ['flight']
    palavra = escolhe_palavra()

    earley = Earley(palavra, gramatica, terminais, variavel_inicial)

    earley.parse()
    print(earley)


def criar_gramatica(digitando):
    regras = []

    print(CRED + "\n\nSe digitar uma variável repetida, ela será subtituida!!" + CEND)
    print(CRED + "\nO formato de entrada deve ser A->Bc. \n\n($ pra finalizar)\n" + CEND)

    while digitando is True:
        regraCrua = input("Digite uma regra: ")

        if verfica_cifrao(regraCrua) and len(regras) == 0:
            print("\n\n\tGramática vazia, por favor digite uma gramática não vazia\n\n")
        elif verfica_cifrao(regraCrua) is True and len(regras) > 0:
            digitando = False

        if not verfica_cifrao(regraCrua):
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
    criar_gramatica(digitando)


def tratar_regras(regras):
    regras_tratadas = {}

    for r in regras:
        if r[1][0].islower() is True:
            regras_tratadas[r[0]] = r[1]
        else:
            regras_tratadas[r[0]] = [r[1]]

    return regras_tratadas


def cria_terminais(gramatica):
    terminais = []

    for gram in gramatica:
        if len(gram[1]) >= 2:
            terminal = gram[1][1]
        else:
            terminal = gram[1][0]

        if terminal not in terminais:
            terminais.append(terminal)

    return terminais


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


def escolhe_palavra():
    palavra_array = []
    palavra = input("\nDigite a palavra a ser analisada: ")

    if isinstance(palavra, str):
        for p in palavra:
            palavra_array.append(p)
        return palavra_array
    else:
        print("Palavra inválida")
        escolhe_palavra()


def adiciona_terminais(gramatica_sem_terminais, terminais):
    gramatica = gramatica_sem_terminais

    gramatica[terminais]

    return gramatica



def valor_invalido():
    print(CRED + "\nValor inválido!!!!!\n" + CEND)
    test()


if __name__ == '__main__':
    test()
