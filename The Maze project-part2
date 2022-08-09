# Pedro Goncalves 87559

# TAD Posicao -> representa uma posicao (x,y) de um
# labirinto arbitrariamente grande
# x e y sao inteiros nao negativos
# a representacao interna deste TAD utilizara tuplos

# Operacoes Basicas:

# Construtores:


def cria_posicao(x, y):
    """2 inteiro nao negativos ---> posicao
       Verifica validade do argumento e gera erro"""

    if not (isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0):
        raise ValueError("cria_posicao: argumentos invalidos")
    else:
        return x, y


def cria_copia_posicao(posicao):
    """posicao ---> posicao
       Devolve uma copia da posicao"""

    return tuple(list(posicao).copy())


# Seletores:

def obter_pos_x(p):
    """posicao ---> inteiro nao negativo
       Devolve a coordenada x da posicao p"""

    return p[0]


def obter_pos_y(p):
    """posicao ---> inteiro nao negativo
       Devolve a coordenada y da posicao p"""

    return p[1]


# Reconhecedores:

def eh_posicao(arg):
    """universal ---> bool
       Devolve True se arg for uma posicao na forma de (x,y) com x e y inteiros
       nao negativos e False se nao se verificar a condicao"""
    return isinstance(arg, tuple) and len(arg) == 2\
           and isinstance(arg[0], int) and isinstance(arg[1], int) \
           and arg[0] >= 0 and arg[1] >= 0


# Transformadores:

def posicao_para_str(p):
    """posicao ---> str
       Devolve a cadeia de caracteres \'(x, y)\' que representa p, sendo os
       valores x e y as coordenadas de p."""

    return str(p)


# print(posicao_para_str((2,1)))

# Teste:

def posicoes_iguais(p1, p2):
    """posicao x posicao ---> bool
    Devolve True se p1 e p2 forem iguais e False se o contrario se verificar"""

    return obter_pos_x(p1) == obter_pos_x(p2) and obter_pos_y(
        p1) == obter_pos_y(p2)


# funcoes alto nivel:

def obter_posicoes_adjacentes(p):
    """posicao ---> tuplo de posicoes
       Devolve o conjunto de posicoes adjacentes da posicao na ordem de leitura
       do labirinto"""

    return tuple(adj for adj in ((obter_pos_x(p) + dx, obter_pos_y(p) + dy)
                                 for dx, dy in ((0, -1), (-1, 0), (1, 0),
                                                (0, 1))) if (adj[0] >= 0 and adj[1] >= 0))


# TAD Unidade
# O TAD unidade eh usado para representar as unidades de combate no simulador de batalhas presentes num labirinto.
# Cada unidade e caracterizada pela sua posicao, forca de ataque, pontos de vida e exercito.
# A forca de ataque e os pontos de vida sao valores inteiros positivos e o exercito eh
# qualquer cadeia de caracteres nao vazia.

# A representacao interna deste TAD usa dicionarios

# Operacoes basicas:

# Construtor:

def cria_unidade(p, v, f, cad):
    """posicao x IN x IN x str ---> unidade
       Recebe uma posicao p, dois valores inteiros maiores que 0
       correspondentes a vida e forca da unidade, e uma string
       nao vazia correspondente ao exercito da unidade; e devolve a unidade
       correspondente. Verifica a validade dos seus argumentos"""

    if not (eh_posicao(p) and isinstance(v, int) and isinstance(f, int)
            and isinstance(cad, str) and v > 0 and f > 0 and cad != ""):
        raise ValueError("cria_unidade: argumentos invalidos")
    else:
        return {"posicao": p, "vida": v, "forca": f, "exercito": cad}


def cria_copia_unidade(u):
    """unidade ---> unidade
       Recebe uma unidade e devolve uma copia dessa unidade"""

    return m.copy()


# Seletores:

def obter_posicao(u):
    """unidade ---> posicao
       Recebe uma unidade e devolve a sua posicao"""

    return u["posicao"]


def obter_exercito(u):
    """unidade ---> str
       Recebe uma unidade e devolve o nome do exercito (string)"""

    return u["exercito"]


def obter_forca(u):
    """unidade ---> IN
       Recebe uma unidade e devolve a sua forca (natural)"""

    return u["forca"]


def obter_vida(u):
    """unidade ---> IN
       Recebe uma unidade e devolve a sua vida (natural)"""
    return u["vida"]


# Modificadores:

def muda_posicao(u, p):
    """unidade x posicao ---> unidade
       Modifica destrutivamente a unidade u alterando a sua posicao com o novo
       valor p, e devolve a propria unidade."""

    u["posicao"] = p
    return u


def remove_vida(u, v):
    """unidade x IN ---> unidade
       Modifica destrutivamente a unidade u alterando os seus pontos de vida
       subtraindo o valor v, e devolve a propria unidade."""

    u["vida"] -= v
    return u


# Reconhecedor:

def eh_unidade(arg):
    """universal ---> bool
    Devolve True caso o seu argumento seja um TAD unidade e
    False caso contrario"""

    keys = ("posicao", "vida", "forca", "exercito")
    return isinstance(arg, dict) and len(arg) == 4 \
           and all([key in keys for key in arg.keys()]) \
           and eh_posicao(arg["posicao"]) and isinstance(arg["vida"], int) \
           and arg["vida"] > 0 and isinstance(arg["forca"], int) \
           and arg["forca"] > 0 and isinstance(arg["exercito"], str) \
           and arg["exercito"] != ""


# Teste:

def unidades_iguais(u1, u2):
    """unidade x unidade ---> bool
       Devolve True apenas se u1 e u2 sao unidades iguais"""

    return len(u1) == len(u2) and obter_posicao(u1) == obter_posicao(u2) \
           and obter_vida(u1) == obter_vida(u2) and obter_forca(u1) == obter_forca(u2) \
           and obter_exercito(u1) == obter_exercito(u2)


# Transformadores:

def unidade_para_char(u):
    """unidade ---> str
       Devolve a cadeia de caracteres dum unico elemento, correspondente ao
       primeiro caracter em maiuscula do exercito da unidade
       passada por argumento."""

    return u["exercito"][0].upper()


def unidade_para_str(u):
    """unidade ---> str
       Devolve a cadeia de caracteres que representa a unidade no formato
       seguinte: <exercito>[<vida>, <forca>]@<posicao>]"""

    return "{}[{}, {}]@{}".format(unidade_para_char(u), obter_vida(u),
                                  obter_forca(u), obter_posicao(u))


# Funcoes de alto nivel:

def unidade_ataca(u1, u2):
    """unidade x unidade ---> booleano
       Modifica destrutivamente a unidade u2 retirando o valor de pontos de
       vida correspondente a forca de ataque da unidade u1. Devolve
       True se a unidade u2 for destruida ou False caso contrario."""

    remove_vida(u2, obter_forca(u1))
    return obter_vida(u2) <= 0


def ordenar_unidades(t):
    """tuplo unidades ---> tuplo unidades
       Devolve um tuplo contendo as mesmas unidades do tuplo fornecido como
       argumento, ordenadas de acordo com a ordem de leitura do labirinto."""

    posicoes = [obter_posicao(unidade) for unidade in t]
    new_pos = [(y, x) for x, y in posicoes]
    new_pos = sorted(new_pos)
    ordenado = tuple(((x, y) for y, x in new_pos))
    final_ordenado = ()
    for posicao in ordenado:
        for unidade in t:
            if obter_posicao(unidade) == posicao:
                final_ordenado += (unidade,)
    return final_ordenado


# TAD Mapa
# O TAD mapa eh usado para representar um labirinto e as unidades que se
# encontram dentro do labirinto
# A representacao interna utiliza dicionarios


# Construtor:

def cria_mapa(d, w, e1, e2):
    """tuplo x tuplo x tuplo x tuplo ---> mapa
       Recebe um tuplo d de 2 valores inteiros que sao as dimensoes Nx e Ny do
       labirinto; um tuplo w de 0 ou mais posicoes correspondentes as paredes
       que nao sao dos limites exteriores do labirinto, um tuplo e1 de 1 ou
       mais unidades do mesmo exercito, e um tuplo e2 de um ou mais unidades
       de um outro exercito;
       Devolve um dicionario que eh o mapa representado internamente.
       Verifica a validade dos seus argumentos"""

    if not (eh_posicao(d) and d[0] >= 3 and d[1] >= 3
            and isinstance(w, tuple) and (not w or all((eh_posicao(p) for p in w)))
            and all((0 < parede[0] < d[0] - 1 for parede in w))
            and all((0 < parede[1] < d[1] - 1 for parede in w))
            and isinstance(e1, tuple) and len(e1) > 0
            and all((eh_unidade(u) for u in e1)) and isinstance(e2, tuple)
            and len(e2) > 0 and all((eh_unidade(u) for u in e1))):
        raise ValueError("cria_mapa: argumentos invalidos")
    else:
        return {"dim": d, "walls": w, "exercito1": e1, "exercito2": e2}


def cria_copia_mapa(m):
    return eval(str(m))


# Seletores:

def obter_tamanho(m):
    """mapa ---> tuplo
       Devolve um tuplo de dois valores inteiros correspondendo o primeiro
       deles a dimensao Nx e o segundo a dimensao Ny do mapa"""

    return m["dim"]


def obter_nome_exercitos(m):
    """mapa ---> tuplo
       Devolve um tuplo ordenado com duas cadeias de caracteres correspondendo
       aos nomes dos exercitos do mapa."""

    return (m["exercito1"][0]["exercito"], m["exercito2"][0]["exercito"]) \
        if m["exercito1"][0]["exercito"][0] <= m["exercito2"][0]["exercito"][0] \
        else (m["exercito2"][0]["exercito"], m["exercito1"][0]["exercito"])


def obter_todas_unidades(m):
    """mapa ---> tuplo
       Devolve um tuplo contendo todas as unidades do
       mapa, ordenadas em ordem de leitura do labirinto."""

    return ordenar_unidades(m["exercito1"] + m["exercito2"])


def obter_unidades_exercito(m, e):
    """mapa ---> tuplo
       Devolve um tuplo contendo as unidades do mapa pertencentes ao exercito
       indicado pela cadeia de caracteres e, ordenadas em ordem de leitura do
       labirinto."""

    return tuple(unidade for unidade in obter_todas_unidades(m)
                 if obter_exercito(unidade) == e)


def obter_unidade(m, p):
    """mapa x posicao ---> unidade
       Devolve a unidade do mapa que se encontra na posicao p."""

    for i in obter_todas_unidades(m):
        if i["posicao"] == p:
            return i


# Modificadores:

def eliminar_unidade(m, u):
    """mapa x unidade ---> mapa
       Modifica destrutivamente o mapa m eliminando a
       unidade u do mapa e deixando livre a posicao onde se encontrava a
       unidade. Devolve o proprio mapa."""

    for exercito in "exercito1", "exercito2":
        if u in m[exercito]:
            m[exercito] = list(m[exercito])
            m[exercito].remove(u)
            m[exercito] = tuple(m[exercito])
    return m


def mover_unidade(m, u, p):
    """mapa x unidade x posicao ---> mapa
       Modifica destrutivamente o mapa m e a unidade u
       alterando a posicao da unidade no mapa para a nova posicao p e deixando
       livre a posicao onde se encontrava. Devolve o proprio mapa."""

    for exercito in "exercito1", "exercito2":
        for i in range(len(m[exercito])):
            if m[exercito][i] == u:
                m[exercito][i]["posicao"] = p
    return m


# Reconhecedores

def eh_posicao_unidade(m, p):
    """mapa x posicao x ---> bool
       Devolve True apenas no caso da posicao p do mapa estar
       ocupada por uma unidade.
       """

    return obter_unidade(m, p) in obter_todas_unidades(m)


def eh_posicao_corredor(m, p):
    """mapa X posicao ---> bool
       Devolve True apenas no caso da posicao p do mapa corresponder a um
       corredor no labirinto (independentemente de estar ou nao ocupado
       por uma unidade)."""

    return p not in m["walls"] and 0 < p[0] < obter_tamanho(m)[0] - 1 and \
           0 < p[1] < obter_tamanho(m)[1] - 1


def eh_posicao_parede(m, p):
    """mapa X posicao ---> bool
       Devolve True apenas no caso da posicao p do mapa corresponder
       a uma parede do labirinto."""

    return not eh_posicao_corredor(m, p) and 0 <= p[0] < obter_tamanho(m)[0] \
           and 0 <= p[1] < obter_tamanho(m)[1]


# Teste:

def mapas_iguais(m1, m2):
    """mapa x mapa ---> bool
       Devolve True apenas se m1 e m2 forem mapas iguais."""

    return obter_todas_unidades(m1) == obter_todas_unidades(m2) \
           and obter_tamanho(m1) == obter_tamanho(m2) \
           and m1["walls"] == m2["walls"]


# Transformador:

def mapa_para_str(m):
    """mapa ---> str
       Devolve uma cadeia de caracteres que representa o mapa como descrito no
       primeiro projeto, neste caso, com as unidades representadas pela sua
       representacao externa."""

    string = ''
    max_x, max_y = obter_tamanho(m)
    for y in range(max_y):
        string += ''.join(
            unidade_para_char(obter_unidade(m, (x, y))) if (
                    (x, y) in (u["posicao"]
                               for u in obter_todas_unidades(m)))
            else ('#' if (eh_posicao_parede(m, (x, y))) else '.')
            for x in range(max_x)) + '\n'
    return string[:-1]


# Funcoes de alto nivel

def obter_inimigos_adjacentes(m, u):
    """mapa x unidade ---> tuplo unidades
       Devolve um tuplo contendo as unidades inimigas adjacentes a unidade u
       de acordo com a ordem de leitura do labirinto."""

    return tuple(obter_unidade(m, adj) for adj in
                 obter_posicoes_adjacentes(obter_posicao(u)) if eh_posicao_unidade(m, adj)
                 if unidade_para_char(obter_unidade(m, adj)) != unidade_para_char(u))


def obter_movimento(mapa, unit):
    """
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    """

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source),
                                  obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in
                  obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(
                mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (
                previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa,
                                           adj) and not eh_posicao_unidade(
                        mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(
                min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo,
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)


# Funcoes adicionais

def calcula_pontos(m, e):
    """mapa x str ---> int
       Recebe um mapa e uma string correspondente ao nome de um dos exercitos
       do mapa e devolve a sua pontuacao.
       A pontuacao dum exercito eh o total dos pontos de vida de todas
       as unidades do exercito."""

    vida_e = 0
    for u in obter_unidades_exercito(m, e):
        vida_e += obter_vida(u)
    return vida_e


def simula_turno(m):
    """mapa ---> mapa
       Modifica o mapa fornecido como argumento de acordo com a simulacao de
       um turno de batalha completo, e devolve o proprio mapa. Isto e, seguindo
       a ordem de leitura do labirinto, cada unidade (viva) realiza um unico
       movimento e (eventualmente) um ataque de acordo com as regras descritas."""

    unidades = obter_todas_unidades(m)
    for u in unidades:
        if u in obter_todas_unidades(m):
            mover_unidade(m, u, obter_movimento(m, u))  # faz um movimento
            inimigos = obter_inimigos_adjacentes(m, u)
            if inimigos:  # se houver inimigos adjacentes
                unidade_ataca(u, inimigos[0])  # ataca
                if obter_vida(inimigos[0]) <= 0:  # elimina a unidade se morrer
                    eliminar_unidade(m, inimigos[0])
    return m


def simula_batalha(config, modo):
    """str x booleano ---> str
       Simula uma batalha completa. A batalha termina quando um dos exercitos vence ou,
       se apos completar um turno, nao ocorreu nenhuma alteracao ao mapa e as unidades.
       Recebe uma string e um bool e devolve o nome do exercito vencedor. Em caso de
       empate, a funcao devolve a string "EMPATE". O arg config eh o ficheiro de
       configuracao do simulador. O arg modo ativa o modo verboso (True) ou o
       modo quiet (False). No modo quiet mostra-se pela sada standard o mapa
       e a pontuacao no incio da simulacao e apos o ultimo turno de batalha.
       No modo verboso, mostra-se tambem o mapa e a pontuacao apos cada turno de batalha"""

    with open(config, "r") as init:
        file = init.readlines()
        dim = eval(file[0])
        walls = eval(file[3])
        nome1 = eval(file[1])[0]
        nome2 = eval(file[2])[0]
        v1 = eval(file[1])[1]
        v2 = eval(file[2])[1]
        f1 = eval(file[1])[2]
        f2 = eval(file[2])[2]
        e1 = tuple(cria_unidade(p, v1, f1, nome1) for p in eval(file[4]))
        e2 = tuple(cria_unidade(p, v2, f2, nome2) for p in eval(file[5]))
        m = cria_mapa(dim, walls, e1, e2)

    print(mapa_para_str(m))
    print("[ {}:{} {}:{} ]".format(nome1, calcula_pontos(m, nome1),
                                   nome2, calcula_pontos(m, nome2)))

    copia_mapa = cria_copia_mapa(m)

    i = 0
    while calcula_pontos(m, nome1) != 0 and calcula_pontos(m, nome2) != 0:
        if mapas_iguais(m, copia_mapa) and i == 1:
            return "EMPATE"
        copia_mapa = cria_copia_mapa(m)
        if modo and i > 0:
            print(mapa_para_str(m))
            print("[ {}:{} {}:{} ]".format(nome1, calcula_pontos(m, nome1),
                                           nome2, calcula_pontos(m, nome2)))
        simula_turno(m)
        i += 1

    print(mapa_para_str(m))
    print("[ {}:{} {}:{} ]".format(nome1, calcula_pontos(m, nome1),
                                   nome2, calcula_pontos(m, nome2)))

    if calcula_pontos(m, nome1) != 0 and calcula_pontos(m, nome2) != 0:
        return "EMPATE"
    elif calcula_pontos(m, nome1) == 0:
        return nome2
    else:
        return nome1
