# AFD

# 5-tupla
estados = []
alfabeto = []
estado_inicial = ""
estados_finais = []
funcao_programa = {}

# Fita
fita = ""

if __name__ == "__main__":

    estados = input("Digite os estado separados por vírgula: ").split(",")
    alfabeto = input("Digite o alfabeto separados por vírgula: ").split(",")
    estado_inicial = input("Digite o estado inicial separado por vírgula: ").split(",")
    estados_finais = input("Digite o(s) estado(s) final(is) separado(s) por vírgula: ").split(",")