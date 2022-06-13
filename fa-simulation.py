# Autômato Finito Determinístico

# 5-tupla
estados = []
alfabeto = []
estado_inicial = ""
estados_finais = []
funcao_programa = {}

# Fita
fita = ""

def popula_estado_inicial(estado_inicial, estados, estado_valido, primeira_vez):

    if estado_valido == False and primeira_vez == True:
        estado_inicial = input("Digite o estado inicial: ")

    if estado_inicial not in estados:
        estado_valido = False
        primeira_vez = False
        estado_inicial = input("Estado inválido, digite outro estado para o estado inicial: ")
        popula_estado_inicial(estado_inicial, estados, estado_valido, primeira_vez)
    else: 
        return estado_inicial

def popula_estado_final(estados_finais, estados, estado_valido, primeira_vez):

    if estado_valido == False and primeira_vez == True:
        estados_finais = input("Digite o(s) estado(s) final(is) separado(s) por vírgula: ").split(",")

    contem_estados_finais = any(estado in estados_finais for estado in estados)

    if contem_estados_finais is True:
        return estados_finais
    else: 
        estado_valido = False
        primeira_vez = False
        estados_finais = input("Estado(s) inválido(s), digite outro(s) estado(s) para o(s) estado(s) final(ais): ")
        popula_estado_final(estados_finais, estados, estado_valido, primeira_vez)

def popula_quintupla():
    estados = input("Digite os estado separados por vírgula: ").split(",")
    alfabeto = input("Digite o alfabeto separados por vírgula: ").split(",")

    estado_inicial = popula_estado_inicial("", estados, False, True)
    estados_finais = popula_estado_final([], estados, False, True)

    print("Digite o próximo estado para o seguinte (Digite - (hífen) para estados rejeitados)")
    
    for estado in estados:
        for letra in alfabeto:
            print(f"\t  {letra}")
            print(f"{estados}\t---->\t", end="")
            dest = input()
            
            # Rejected states are represented as None in the dictionary
            if dest == "-":
                funcao_programa[(estado, letra)] = None
            else:
                funcao_programa[(estado, letra)] = dest

def valida_fita(fita):

    estado_atual = estado_inicial

    for caractere in fita:
        estado_atual = funcao_programa[(estado_atual, caractere)]
        
        if estado_atual is None:
            print("Rejeitado")
            break
    else:
        # When entire string is parsed, check whether the final state is an accepted state
        if (estado_atual in estados_finais):
            print("Aceito")
        else:
            print("Rejeitado")

if __name__ == "__main__":

    popula_quintupla()
    fita = input("Digite uma palavra para verificar se ela está contida no automato: ")
    valida_fita(fita)


    