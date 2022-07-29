CRED = '\033[91m'
CGREEN = '\33[32m'
CEND = '\033[0m'


def Dzero(V, P, S):
    Dzero = []

    for regra in P:
        if regra[0] == S:
            # Parte 1
            Dzero.append([S, ['.'] + regra[1] + ['/', 0]])

    count = 0
    incluidos = [S]

    while True:
        # Parte 2
        estado = Dzero[count][1][1]

        if estado in V and estado not in incluidos:
            for regra in P:
                if regra[0] == estado:
                    Dzero.append([estado, ['.'] + regra[1] + ['/', 0]])
            incluidos.append(estado)
        count += 1

        if count == len(Dzero):
            break

    print(f'D0:')

    for regra in Dzero:
        r1 = regra[0]
        r2 = listToString(regra[1])
        print(r1 + " -> " + r2)

    return Dzero


def DRs(V, P, S, Dzero, palavra):
    tempP = P
    D = [Dzero]

    for r in range(1, len(palavra) + 1):
        simbolo = palavra[r - 1]
        D.append([])
        print('')
        print(f'D{r}: ')

        for k in D[r - 1]:
            if simbolo in k[1]:
                posicao_ponto = k[1].index('.')

                if k[1][posicao_ponto + 1] == simbolo:
                    copia = k[1].copy()
                    copia[posicao_ponto], copia[posicao_ponto + 1] = copia[posicao_ponto + 1], copia[posicao_ponto]
                    D[r].append([k[0], copia])

                    r1 = D[r][-1][0]
                    r2 = listToString(D[r][-1][1])
                    print(r1 + " -> " + r2)

        print('\n\n')

        # Parte 3
        for k in D[r]:
            posicao_ponto = k[1].index('.')
            B = k[1][posicao_ponto + 1]
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

                        r1 = D[r][-1][0]
                        r2 = listToString(D[r][-1][1])
                        print(r1 + " -> " + r2)
        # Parte 4
        for k in D[r]:
            tempP = P.copy()
            posicao_ponto = k[1].index('.')
            if k[1][posicao_ponto + 1] == '/':
                A, s = k[0], k[1][-1]
                for j in D[s]:
                    posicao_ponto = j[1].index('.')

                    if j[1][posicao_ponto + 1] == A:
                        copia = j[1].copy()
                        copia[posicao_ponto], copia[posicao_ponto + 1] = copia[posicao_ponto + 1], copia[posicao_ponto]
                        D[r].append([j[0], copia])

                        r1 = D[r][-1][0]
                        r2 = listToString(D[r][-1][1])
                        print(r1 + " -> " + r2)
        verifica_palavra(D, S)


def verifica_palavra(D, S):
    reconhece = False
    for k in D[-1]:
        if k[0] == S and k[1][-3] == '.' and k[1][-2] == '/' and k[1][-1] == 0:
            reconhece = True
    print()
    if reconhece:
        print(CGREEN + 'A palavra foi reconhecida' + CEND)
    else:
        print(CRED + 'A palavra NÃO foi reconhecida' + CEND)


def listToString(ls):
    string = ""
    for i in ls:
        if type(i) == int:
            i = str(i)
        string += i
    return string
