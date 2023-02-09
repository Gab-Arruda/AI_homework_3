from collections import Counter
import random
#import numpy as np


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

    reverted_individual = individual.copy()
    reverted_individual = reverted_individual[::-1]
    # reverted_individual = reverted_individual.reverse()

    for x in reversed(range(8)):
        diagonalxy[x] = (x + 1) - reverted_individual[x]

    dic2 = dict(Counter(diagonalxy))
    dic3 = dict(Counter(diagonalyx))

    for x in dic2.keys():
        de = de + colatetal_quadratico(dic2[x])

    for x in dic3.keys():
        ed = ed + colatetal_quadratico(dic3[x])

    # print('de = ',de, ', ed = ', ed,', linha = ', linha)
    return ed + de + linha


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

    best_value = 9999999999
    best_array = []
    for x in participants:
        value = evaluate(x)
        if value < best_value:
            best_array = x
            best_value = value

    return best_array


def select_two_best_individuals(participants, k):
    best_participants = []
    for x in range(2):
        random_participants = random.sample(participants, k)
        best_participants.append(tournament(random_participants))

    return best_participants


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
    individual_copy = individual.copy()
    if random.random() < m:
        individual_copy[random.randint(0, 7)] = random.randint(1, 8)

    return individual_copy

    
def elitism (population, e):
    best_individuals = []
    for x in range(e):
        best_individual = tournament(population)
        best_individuals.append(best_individual)
        population.remove(best_individual)
        
    return best_individuals
   
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
    population = []

    for x in range(n):
        # population.append(np.random.randint(1, 9, 8)) dava erro pois nao gerava list, gerava ndarray e dai nao tem
        # alguns métodos
        population.append([random.randint(1, 8) for i in range(8)])
    
    elite = []    
    if(e > 0):
        elite = elitism(population, e)
    for x in range(g):
        mutated_population = elite.copy() 
        while len(mutated_population) < n:
            # seleciona os dois melhores individuos seguindo o algoritmo passado em aula para seleção
            best_individuals = select_two_best_individuals(population, k)
            # faz crossover (considerei que sempre faz no ponto 4, mas talvez valha a pena mudar pra ver se melhora
            best_individuals = crossover(best_individuals[0], best_individuals[1], 4)

            # causa mutação nos dois novos individuos e após isso os adiciona ao mutated_population
            mutated_population.append(mutate(best_individuals[0], m))
            mutated_population.append(mutate(best_individuals[1], m))

            # fazer crossover com esses dois indivíduos que vai retornar dois novos indivíduos

            # os dois novos indivíduos vão passar por mutation
        population = mutated_population.copy()
    # retornar o melhor indivíduo da nova população gerada
    best_generated_individual = tournament(population)
    print('best_generated_individual: ', best_generated_individual)
    print('number of attacks on best individual: ', evaluate(best_generated_individual))
    return tournament(population)


test_participants = [
    [2, 2, 4, 8, 1, 6, 3, 4],
    [2, 7, 4, 1, 1, 8, 2, 8],
    [3, 3, 4, 2, 3, 6, 1, 1],
    [6, 5, 4, 8, 1, 3, 8, 2],
    [2, 4, 4, 2, 3, 6, 5, 3],
    [1, 2, 4, 8, 1, 8, 3, 5],
    [4, 1, 4, 5, 7, 6, 8, 4],
    [8, 8, 7, 3, 5, 2, 1, 7],
]

# select_two_best_individuals(test_participants, 4)
run_ga(64, 128, 64, 0.3, 1)
# best_individual_and_index(test_participants)
# elitism(test_participants, 3)
# evaluate([8, 4, 7, 3, 5, 2, 1, 7])
# mutate([2, 2, 4, 8, 1, 6, 3, 4], 1)
# evaluate([2, 2, 4, 8, 1, 6, 3, 4])

# a melhor combinação que encontrei até agora que acha em pouco tempo é run_ga(64, 128, 64, 0.3, 1)
