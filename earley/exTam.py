# Algoritmo de Early

# Entrada dos dados
def funcao_escolhida():  # retorna a funcao escolhida 1 ou 2
    while True:
        try:
            print('')
            e = int(input('Escolha entre digitar uma gramática (1) ou escolher uma pré-definida (2): '))
        except:
            print("### O valor digitado deve ser um número  ###")
            continue
        if e in [1, 2]:
            break
        else:
            print("###  Escolha inválida  ###")
    return e


def inicial(V):
    while True:
        i = input("Digite a variavel inicial: ")
        if i in V:
            return i
        else:
            print("###  Variável inicial inválida  ###")


def gramatica():
    print("Entrada de regras gramaticais:")
    print("(formato: A -> B c A D, com epsilon = % e $ para finalizar entrada)")
    print("-------------------------------------------------------------------")

    V = {}
    T = {}
    P = []

    while True:
        print("Digite uma regra: ($ para finalizar)")
        r = input()
        if r == "$":
            break
        r = r.replace(" ", "", -1)
        if (r[1] + r[2]) != "->":
            print("###  Formato errado. Digite novamente  ###")
            print()
            continue
        print('--')
        r = r.replace("->", "", -1)
        r = r.replace("%", "", -1)
        r = list(r)
        primeira = r.pop(0)
        V = set(primeira).union(V)
        for letra in r:
            if letra in "ABCDEFGHIJHLMNOPQRSTUVXYWZ":
                V = set(letra).union(V)
            else:
                T = set(letra).union(T)
        P.append([primeira, r])

    S = inicial(V)

    return V, T, P, S


def pre_definida():
    V = {'E', 'F', 'T'}
    T = {'(', ')', '*', '+', 'x'}
    P = [['E', ['T']], ['E', ['E', '+', 'T']],
         ['T', ['F']], ['T', ['T', '*', 'F']],
         ['F', ['(', 'E', ')']], ['F', ['x']]]
    S = 'E'
    return V, T, P, S


if funcao_escolhida() == 1:
    V, T, P, S = gramatica()
else:
    V, T, P, S = pre_definida()

print(f"V = {V}")
print(f"T = {T}")
print(f"P = {P}")
print(f"S = {S}")

# construcao do D0
D0 = []
for k in P:
    if k[0] == S:
        D0.append([S, ['.'] + k[1] + ['/', 0]])  # (1)
cont_d0 = 0
incluidos = [S]
while True:
    estado = D0[cont_d0][1][1]  # (2)
    if estado in V and estado not in incluidos:
        for k in P:
            if k[0] == estado:
                D0.append([estado, ['.'] + k[1] + ['/', 0]])
        incluidos.append(estado)
    cont_d0 += 1
    if cont_d0 == len(D0):
        break
print(f'D0 =')
for k in D0:
    print(k)

# Construcao dos Dr's
w = input('Digite a palavra a ser processada:')
D = []
D.append(D0)
for r in range(1, len(w) + 1):
    simbolo = w[r - 1]
    D.append([])
    print('')
    print(f'D[{r}] =')
    for k in D[r - 1]:
        if simbolo in k[1]:
            posicao_ponto = k[1].index('.')
            if k[1][posicao_ponto + 1] == simbolo:  # processa .(simbolo) em D[r-1]
                copia = k[1].copy()
                copia[posicao_ponto], copia[posicao_ponto + 1] = copia[posicao_ponto + 1], copia[posicao_ponto]
                D[r].append([k[0], copia])
                print(f'{D[r][-1]}')
    print('-----------------------------------')
    for k in D[r]:  # (3)
        posicao_ponto = k[1].index('.')
        B = k[1][posicao_ponto + 1]  # processa .(variavel). As variaveis estao em V
        if B in V:
            A = k[0]
            for j in P:
                if B == j[0]:
                    novo = ['.']
                    novo.extend(j[1])
                    novo = novo + ['/', r]
                    D[r].append([B, novo])
                    print(f'{D[r][-1]}')
    for k in D[r]:  # (4)
        posicao_ponto = k[1].index('.')
        if k[1][posicao_ponto + 1] == '/':
            A, s = k[0], k[1][-1]
            for j in D[s]:
                posicao_ponto = j[1].index('.')
                if j[1][posicao_ponto + 1] == A:  # processa .(A) em D[s]
                    copia = j[1].copy()
                    copia[posicao_ponto], copia[posicao_ponto + 1] = copia[posicao_ponto + 1], copia[posicao_ponto]
                    D[r].append([j[0], copia])
                    print(f'{D[r][-1]}')

# avaliar se a palavra é reconhecida pela gramatica
reconhece = False
for k in D[-1]:
    if k[0] == S and k[1][-3] == '.' and k[1][-2] == '/' and k[1][-1] == 0:
        reconhece = True
print()
if reconhece:
    print('### Palavra reconhecida ###')
else:
    print('### Palavra NÃO reconhecida ###')
