# Autômato Finito Determinístico

# 5-tupla
estados = []
alfabeto = []
estado_inicial = ""
estados_finais = []
funcao_programa = {}
Afn = None

# Fita
fita = ""


def popula_estado_inicial(estado_inicial, estados, estado_valido, primeira_vez):
    if estado_valido is False and primeira_vez is True:
        estado_inicial = input("Digite o estado inicial: ")

    if estado_inicial not in estados:
        estado_valido = False
        primeira_vez = False
        estado_inicial = input("Estado inválido, digite outro estado para o estado inicial: ")
        popula_estado_inicial(estado_inicial, estados, estado_valido, primeira_vez)
    else:
        return estado_inicial


def popula_estado_final(estados_finais, estados, estado_valido, primeira_vez):
    if estado_valido is False and primeira_vez is True:
        estados_finais = input("Digite o(s) estado(s) final(is) separado(s) por vírgula: ").split(",")

    contem_estados_finais = any(estado in estados_finais for estado in estados)

    if contem_estados_finais is True:
        return estados_finais
    else:
        estado_valido = False
        primeira_vez = False
        estados_finais = input("Estado(s) inválido(s), digite outro(s) estado(s) para o(s) estado(s) final(ais): ")
        popula_estado_final(estados_finais, estados, estado_valido, primeira_vez)


def valida_destino_afd(destinos, estados, dest_valido):
    dest_valido = any(dest in destinos for dest in estados)
    if dest_valido is True:
        return destinos
    else:
        destinos = input("Por favor, digite um estado válido: ")
        valida_destino_afd(destinos, estados, dest_valido)



def valida_destino_afn(destinos, estados, dest_valido):
    dest_valido = any(dest in destinos for dest in estados)
    if dest_valido is True:
        return destinos
    else:
        destinos = input("Por favor, digite um estado válido: ").split(",")
        valida_destino_afn(destinos, estados, dest_valido)


def imprime_resultado_afd(fita, estado_atual, estados_finais):
    print("\n\nAutômato Finito Determinístico\n\n")
    for simbolo in fita:
        estado_atual = funcao_programa[''.join(estado_atual), simbolo]

        if estado_atual is None:
            return print("Rejeitado")
    else:
        if any(e in estado_atual for e in estados_finais):
            return print("Palavra '" + fita + "' Aceita")
        else:
            return print("Palavra '" + fita + "' Rejeitada")


def imprime_resultado_afn(fita, estado_atual, estados_finais):
    print("\nAutômato Finito Não Determinístico\n\n")
    for simbolo in fita:
        if type(estado_atual) is list and len(estado_atual) > 1:
            for e in estado_atual:
                estado_atual = funcao_programa[(''.join(e), simbolo)]
        else:
            estado_atual = funcao_programa[(''.join(estado_atual), simbolo)]

        if estado_atual is None:
            print("Rejeitado")
            break
    else:
        if any(e in estado_atual for e in estados_finais):
            print("Palavra '" + fita + "' Aceita")
        else:
            print("Palavra '" + fita + "' Rejeitada")


if __name__ == "__main__":

    # estados = input("Digite os estado separados por vírgula: ").split(",")
    estados = ["s0", "s1", "s2"]
    # alfabeto = input("Digite o alfabeto separados por vírgula: ").split(",")
    alfabeto = ["0", "1"]

    # estado_inicial = popula_estado_inicial("", estados, False, True)
    estado_inicial = "s0"
    # estados_finais = popula_estado_final([], estados, False, True)
    estados_finais = ["s0"]

    print("Digite o estado destino para o seguinte estado: (Digite - (hífen) para cancelar a ligação)")

    for estado in estados:
        for letra in alfabeto:
            print(f"\t  {letra}")
            print(f"{estado}\t---->\t", end="")

            destino = input().split(",")

            if len(destino) > 1 or Afn is True:
                Afn = True
                dest = valida_destino_afn(destino, estados, None)
            else:
                dest = valida_destino_afd(destino, estados, None)

            if dest == "-":
                funcao_programa[(estado, letra)] = None
            else:
                funcao_programa[(estado, letra)] = dest

    fita = input("Digite uma palavra para verificar se ela está contida no automato: ")

    estado_atual = estado_inicial

    if Afn is True:
        imprime_resultado_afn(fita, estado_atual, estados_finais)
    else:
        imprime_resultado_afd(fita, estado_atual, estados_finais)
