# construcao do D0
def D0(V, P, S):
    D0 = []

    for regra in P:
        if regra[0] == S:
            D0.append([S, ['.'] + regra[1] + ['/', 0]])  # (1)

    count = 0
    incluidos = [S]

    while True:
        estado = D0[count][1][1]  # (2)

        if estado in V and estado not in incluidos:
            for regra in P:
                if regra[0] == estado:
                    D0.append([estado, ['.'] + regra[1] + ['/', 0]])
            incluidos.append(estado)
        count += 1

        if count == len(D0):
            break
    print(f'D0 =')

    for regra in D0:
        print(regra)


# Construcao dos Dr's
def DRs(V, P, S):
    w = input('Digite a palavra a ser processada:')
    D = []
    D.append(D0)
    tempP = P
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
            flagP = False
            if B in V:
                A = k[0]
                for j in tempP:
                    if flagP:
                        tempP.remove(flagP)
                        flagP = False
                    if B == j[0]:
                        novo = ['.']
                        novo.extend(j[1])
                        novo = novo + ['/', r]
                        D[r].append([B, novo])
                        flagP = j.copy()
                        print(f'{D[r][-1]}')

        for k in D[r]:  # (4)
            tempP = P.copy()
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
        avalia_palavra(D, S)


def avalia_palavra(D, S):
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
