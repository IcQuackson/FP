# 87559 Pedro Goncalves


def eh_labirinto(maze):

    """Esta funcao recebe um argumento de qualquer tipo e devolve True se o seu argumento
       corresponde a um labirinto e False caso contrario, sem nunca gerar erros. Considera-se que um labirinto
       corresponde a um tuplo contendo Nx tuplos, cada um deles contendo Ny inteiros, com valores 0 ou 1.
       O labirinto tem tamanho minimo de 3 x 3. Num labirinto, as posicoes externas correspondem sempre a paredes.
       Define-se parede como sendo um 1 e posicoes livres como um 0."""

    # verifica se o labirinto nao eh um tuplo
    if not isinstance(maze, tuple):
        return False

    # verifica se o tuplo tem no minimo dimensao 3 de abcissas
    if not(len(maze) >= 3):
        return False

    for row in maze:

        # verifica se o labirinto nao eh um tuplo de tuplos
        if not isinstance(row, tuple):
            return False

        # verifica se o labirinto nao tem dimensao minima de 3 em ordenadas
        if not len(row) >= 3:
            return False

        # verifica se os elementos dos tuplos nao sao 0 ou 1 inteiros
        for e in row:
            if not ((e == 0 or e == 1) and isinstance(e, int)):
                return False

        # verifica se o labirinto nao tem paredes nos limites superior e inferior
        if not(row[0] == 1 and row[len(row)-1] == 1):
            return False

        # verifica se os tuplos do labirinto nao tem todos o mesmo tamanho
        if not len(row) == len(maze[0]):
            return False

    for i in range(len(maze[0])):

        # verifica se o labirinto nao tem paredes nos limites a esquerda e direita
        if not(maze[0][i] == 1 and maze[len(maze)-1][i] == 1):
            return False

    # se argumento for valido
    return True


def eh_posicao(posicao):

    """Esta funcao recebe um argumento de qualquer tipo e devolve True se o seu argumento corresponde a uma posicao
       e False caso contrario, sem nunca gerar erros. Considera-se que uma posicao corresponde a um tuplo contendo 2
       valores inteiros nao negativos correspondendo a uma posicao (x, y) num labirinto."""

    # verifica se a posicao nao eh um tuplo
    if not isinstance(posicao, tuple):
        return False

    # verifica se a posicao nao tem dois elementos
    if not len(posicao) == 2:
        return False

    # verifica se a posicao eh um tuplo de numeros inteiros
    for e in posicao:
        if not isinstance(e, int):
            return False

    # verifica se a posicao tem coordenadas negativas
    if not (posicao[0] >= 0 and posicao[1] >= 0):
        return False

    # se o argumento for valido
    return True


def eh_conj_posicoes(conj_posicoes):  # checked

    """Esta funcao recebe um argumento de qualquer tipo e devolve True se o seu argumento corresponde a um conjunto de
       posicoes diferentes e False caso contrario, sem nunca gerar erros. Considera-se que um conjunto de posicoes
       corresponde a um tuplo contendo 0 ou mais posicoes diferentes."""

    # verifica se o conj_posicoes nao eh um tuplo
    if not isinstance(conj_posicoes, tuple):
        return False

    # verifica se o conj_posicoes eh um tuplo contendo 0 posicoes
    if len(conj_posicoes) == 0:
        return True

    for tuplo in conj_posicoes:

        # verifica se o tuplo dentro de conj_posicoes nao eh uma posicao
        if not eh_posicao(tuplo):
            return False

    # verifica se a posicao nao eh unica no conj_posicoes
    if sorted(tuple(set(conj_posicoes))) != sorted(conj_posicoes):
        return False

    # se o argumento for valido
    return True


def tamanho_labirinto(maze):  # checked

    """Esta funcao recebe um labirinto e devolve um tuplo de dois valores inteiros correspondendo o primeiro deles a
       dimensao Nx e o segundo a dimensao Ny do labirinto.
       Se o argumento dado for invalido, a funcao gera um erro"""

    # verifica se o maze nao eh um labirinto valido
    if not eh_labirinto(maze):
        raise ValueError("tamanho_labirinto: argumento invalido")

    nx = len(maze)  # largura
    ny = len(maze[0])  # comprimento

    # retorna dimensoes do labirinto
    return nx, ny


def eh_mapa_valido(maze, conj_posicoes):  # checked

    """Esta funcao recebe um labirinto e um conjunto de posicoes correspondente as unidades
       presentes no labirinto, e devolve True se o segundo argumento corresponde a um conjunto
       de posicoes compativeis (nao ocupadas por paredes) dentro do labirinto e False caso
       contrario. Se algum dos argumentos dado for invalido, a funcao gera um erro."""

    # verifica se o labirinto ou conj_posicoes nao sao validos
    if not (eh_labirinto(maze) and eh_conj_posicoes(conj_posicoes)):
        raise ValueError("eh_mapa_valido: algum dos argumentos e invalido")

    # verifica se conj_posicoes nao eh valido
    if not eh_conj_posicoes(conj_posicoes):
        raise ValueError("eh_mapa_valido: algum dos argumentos e invalido")

    dimensoes = tamanho_labirinto(maze)
    for posicao in conj_posicoes:
        for i in range(len(posicao)):

            # verifica se as coordenadas nao estao dentro do labirinto
            if not (0 <= posicao[i] < dimensoes[i]):
                return False

        # verifica se a posicao corresponde a uma posicao do labirinto nao livre (uma parede)
        if maze[posicao[0]][posicao[1]] == 1:
            return False

    # se o argumento for valido
    return True


def eh_posicao_livre(maze, conj_posicoes, posicao):

    """Esta funcao recebe um labirinto, um conjunto de posicoes correspondente a unidades
       presentes no labirinto e uma posicao, e devolve True se a posicao corresponde a uma
       posicao livre (nao ocupada nem por paredes, nem por unidades) dentro do labirinto e
       False caso contrario. Se algum dos argumentos dado for invalido, a funcao gera um erro"""

    # verifica se o labirinto, conj_posicoes ou posicao nao sao validos
    if not (eh_labirinto(maze) and eh_conj_posicoes(conj_posicoes) and eh_posicao(posicao)):
        raise ValueError("eh_posicao_livre: algum dos argumentos e invalido")

    if not eh_mapa_valido(maze, conj_posicoes):
        raise ValueError("eh_posicao_livre: algum dos argumentos e invalido")

    # verifica se a posicao requisitada esta ocupada por paredes
    if not eh_mapa_valido(maze, (posicao,)):
        return False

    # verifica se a posicao requisitada esta ocupada por outras unidades)
    if posicao in conj_posicoes:
        return False

    # se a unidade estiver numa posicao livre
    return True


def posicoes_adjacentes(posicao):

    """Esta funcao recebe uma posicao e devolve o conjunto de posicoes adjacentes da posicao em ordem de leitura de
       um labirinto. Se o argumento dado for invalido, a funcao gera um erro."""

    # verifica se a posicao nao e valida
    if not eh_posicao(posicao):
        raise ValueError("posicoes_adjacentes: argumento invalido")

    up = posicao[0], posicao[1] - 1  # (x, y-1)
    left = posicao[0] - 1, posicao[1]  # (x-1, y)
    right = posicao[0] + 1, posicao[1]  # (x+1, y)
    down = posicao[0], posicao[1] + 1  # (x, y+1)
    adjacentes = (up, left, right, down)
    adjacentes_validas = ()

    for posicao in adjacentes:
        # verifica se a posicao adjacente estiver dentro do labirinto
        if posicao[0] >= 0 and posicao[1] >= 0:
            adjacentes_validas += (posicao,)

    return adjacentes_validas


def mapa_str(maze, conj_posicoes):

    """Esta funcao recebe um labirinto e um conjunto de posicoes correspondente as unidades
       presentes no labirinto e devolve a cadeia de caracteres que as representa (a representacao
       externa), por meio de simbolos como o cardinal (paredes), o ponto (corredores livres) e O (posicao das unidades).
       Se algum dos argumentos dado for invalido, a funcao gera um erro."""

    if not eh_mapa_valido(maze, conj_posicoes):
        raise ValueError("mapa_str: algum dos argumentos e invalido")

    mapa = ""
    for i in range(len(maze[0])):  # os 2 primeiros for percorrem o i-esimo elemento de cada tuplo do labirinto
        for j in range(len(maze)):
            for posicao in conj_posicoes:
                # verifica se a unidade esta nesta posicao do labirinto
                if posicao[0] == j and posicao[1] == i:
                    mapa += "O"
                    break
            else:
                # verifica se a posicao esta ocupada por uma parede
                if maze[j][i] == 1:
                    mapa += "#"
                else:
                    # verifica se a posicao e um corredor livre
                    mapa += "."
        # adiciona um \n (nova linha) no final de cada iteracao de i exceto a ultima
        if i != len(maze[0]) - 1:
            mapa += "\n"
    return mapa


def obter_objetivos(maze, conj_posicoes, posicao):

    """Esta funcao recebe um labirinto, um conjunto de posicoes correspondente as unidades
       presentes no labirinto e uma posicao correspondente a uma das unidades, e devolve o
       conjunto de posicoes nao ocupadas dentro do labirinto correspondente
       a todos os possveis objetivos da unidade correspondente a posicao dada.
       Se algum dos argumentos dado for invalido, a funcao gera um erro."""

    # verifica se algum dos argumentos eh invalido
    if not (eh_labirinto(maze) and eh_conj_posicoes(conj_posicoes) and eh_posicao(posicao)):
        raise ValueError("obter_objetivos: algum dos argumentos e invalido")

    # verifica se a unidade introduzida esta no labirinto
    if posicao not in conj_posicoes:
        raise ValueError("obter_objetivos: algum dos argumentos e invalido")

    else:
        objetivos = ()
        for unidade in conj_posicoes:
            if unidade != posicao:
                for adjacente in posicoes_adjacentes(unidade):
                    # adiciona-se a posicao adjacente da unidade a lista de objetivos se for uma posicao livre
                    # e nao estiver ja na lista
                    if eh_posicao_livre(maze, conj_posicoes, adjacente) and adjacente not in objetivos:
                        objetivos += (adjacente,)
        return objetivos


def adjacentes_validas(maze, conj_posicoes, posicao):

    """Esta funcao determina as adjacentes de uma unidade que nao estao ocupadas por unidades, paredes,
    ou que nao estao fora do labirinto, pela ordem de leitura do labirinto"""

    adjacentes = ()
    for i in range(len(posicoes_adjacentes(posicao))):
        if eh_posicao_livre(maze, conj_posicoes, posicoes_adjacentes(posicao)[i]):
            adjacentes += (posicoes_adjacentes(posicao)[i],)
    return adjacentes


def obter_caminho(maze, conj_posicoes, posicao):

    """Esta funcao recebe um labirinto, um conjunto de posicoes correspondente as unidades
presentes no labirinto, e uma posicao correspondente a uma das unidades, e devolve um
conjunto de posicoes correspondente ao caminho de numero mınimo de passos desde a posicao dada ate a
posicao objetivo. Se algum dos argumentos dado for invalido, a funcao gera um erro."""

    # verifica se algum dos argumentos eh invalido
    if not (eh_labirinto(maze) and eh_conj_posicoes(conj_posicoes) and eh_posicao(posicao)):
        raise ValueError("obter_objetivos: algum dos argumentos e invalido")
    if posicao not in conj_posicoes:
        raise ValueError("obter_objetivos: algum dos argumentos e invalido")
    else:
        lst_exploracao = [pos for pos in adjacentes_validas(maze, conj_posicoes, posicao)]
        pos_visitadas = [posicao]
        objetivo = obter_objetivos(maze, conj_posicoes, posicao)[0]

        while lst_exploracao:
            if lst_exploracao[0] not in pos_visitadas:
                pos_visitadas.append(lst_exploracao[0])
                lst_exploracao += adjacentes_validas(maze, conj_posicoes, lst_exploracao[0])
                path_group = [(objetivo,)]
                j = len(pos_visitadas) - 1
                while j >= 0:
                    for k in range(len(path_group)):
                        for i in range(len(path_group[k]) - 1, -1, -1):
                            if pos_visitadas[j] in adjacentes_validas(maze, conj_posicoes,
                                                                      path_group[k][i]) and i == len(
                                    path_group[k]) - 1 and pos_visitadas[j] not in path_group[k]:
                                path_group[k] += (pos_visitadas[j],)
                            elif pos_visitadas[j] in adjacentes_validas(maze, conj_posicoes,
                                                                        path_group[k][i]) and i != len(
                                    path_group[k]) - 1 and pos_visitadas[j] not in path_group[k]:
                                path_group += [(path_group[k][:i + 1] + (pos_visitadas[j],))]
                            else:
                                continue
                    j -= 1
            del(lst_exploracao[0])
        shortest = 0
        shortest_paths = []
        while not shortest_paths:
            for path in path_group:
                if len(path) == shortest:
                    shortest_paths += [path]
            shortest += 1
        final = []
        adjacente_saved = posicao
        l = len(shortest_paths[0]) - 1
        m = len(shortest_paths) - 1
        while len(shortest_paths) != 1:
            for adjacente in adjacentes_validas(maze, conj_posicoes, adjacente_saved):
                while l >= 0:
                    while m >= 0:
                        if shortest_paths[m][l] == adjacente and shortest_paths[m]:
                            final += [shortest_paths[m]]
                        m -= 1
                    if final:
                        l -= 1
                        for n in range(len(shortest_paths)-1, -1, -1):
                            if shortest_paths[n] not in final:
                                del(shortest_paths[n])
                                final = []
                    final = []
                    break
                m = len(shortest_paths) - 1
                if len(shortest_paths) == 1:
                    break

            adjacente_saved = shortest_paths[m][l]
        return (posicao,) + shortest_paths[0][::-1]


def mover_unidade(maze, conj_posicoes, posicao):

    """Esta funcao recebe um labirinto, um conjunto de posicoes correspondente as unidades
       presentes no labirinto, e uma posicao correspondente a uma das unidades, e devolve
       o conjunto de posicoes actualizado correspondente as unidades presentes no labirinto
       apos a unidade dada ter realizado um unico movimento."""

    # verifica se algum dos argumentos eh invalido
    if not (eh_labirinto(maze) and eh_conj_posicoes(conj_posicoes) and eh_posicao(posicao)):
        raise ValueError("mover_unidade: algum dos argumentos e invalido")
    if posicao not in conj_posicoes:
        raise ValueError("mover_unidade: algum dos argumentos e invalido")
    if len(obter_caminho(maze, conj_posicoes, posicao)) == 1:
        return posicao

    unidade_updated = obter_caminho(maze, conj_posicoes, posicao)[1]
    for i in range(len(conj_posicoes)):
        if conj_posicoes[i] == posicao:
            conj_posicoes = conj_posicoes[:i] + (unidade_updated,) + conj_posicoes[i+1:]
    return conj_posicoes
