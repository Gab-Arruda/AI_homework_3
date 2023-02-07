from collections import Counter
import random


def evaluate(individual):
    dic1 = [0, 0, 0, 0, 0, 0, 0, 0]
    for x in individual:
        dic1[x - 1] = dic1[x - 1] + 1
    linha = 0
    de = 0
    ed = 0

    for x in dic1:
        linha = linha + colatetal_quadratico(x)

    diagonalxy = [0, 0, 0, 0, 0, 0, 0, 0]
    diagonalyx = [0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(8):
        diagonalyx[x] = individual[x] - (x + 1)

    revertedIndividual = individual.copy()
    revertedIndividual.reverse()

    for x in reversed(range(8)):
        diagonalxy[x] = (x + 1) - revertedIndividual[x]

    dic2 = dict(Counter(diagonalxy))
    dic3 = dict(Counter(diagonalyx))

    for x in dic2.keys():
        de = de + colatetal_quadratico(dic2[x])

    for x in dic3.keys():
        ed = ed + colatetal_quadratico(dic3[x])

    return ed + de + linha  # substituir pelo seu codigo


def colatetal_quadratico(n):
    soma = 0
    for x in range(n):
        soma = soma + x

    return soma


# evaluate([2,2,4,8,1,6,3,4])


def tournament(participants):
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list melhor individuo da lista recebida
    """

    bestValue = 9999999999
    bestArray = []
    for x in participants:
        value = evaluate(x)
        if (value < bestValue):
            bestArray = x
            bestValue = value

    return bestArray  # substituir pelo seu codigo


def crossover(parent1, parent2, index):
    """
    Realiza o crossover de um ponto: recebe dois indivíduos e o ponto de
    cruzamento (indice) a partir do qual os genes serão trocados. Retorna os
    dois indivíduos com o material genético trocado.
    Por exemplo, a chamada: crossover([2,4,7,4,8,5,5,2], [3,2,7,5,2,4,1,1], 3)
    deve retornar [2,4,7,5,2,4,1,1], [3,2,7,4,8,5,5,2].
    A ordem dos dois indivíduos retornados não é importante
    (o retorno [3,2,7,4,8,5,5,2], [2,4,7,5,2,4,1,1] também está correto).
    :param parent1:list
    :param parent2:lis
    t
    :param index:int
    :return:list,list
    """

    return parent1[:index] + parent2[index - len(parent2):], parent2[:index] + parent1[index - len(parent1):]


def mutate(individual, m):
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:int - probabilidade de mutacao
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """
    indCopy = individual.copy()
    if (random.random() < m):
        indCopy[random.randint(0, 7)] = random.randint(1, 8)

    print(indCopy)
    return indCopy

def run_ga(g, n, k, m, e):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:int - número de indivíduos no elitismo
    :return:list - melhor individuo encontrado
    """
    raise NotImplementedError  # substituir pelo seu codigo


mutate([2, 2, 4, 8, 1, 6, 3, 4], 1)
