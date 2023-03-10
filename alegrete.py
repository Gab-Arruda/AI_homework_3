def compute_mse(theta_0, theta_1, data):
    """
    Calcula o erro quadratico medio
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    summation = 0

    for terrain in data:
        h = theta_0 + theta_1 * terrain[0]
        square_sum = pow(h-terrain[1], 2)
        summation = summation + square_sum

    return summation / len(data)


def step_gradient(theta_0, theta_1, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de theta_0 e theta_1.
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de theta_0 e theta_1, respectivamente
    """
    summation_theta_zero = 0
    summation_theta_one = 0
    for terrain in data:
        h = theta_0 + theta_1 * terrain[0]
        error = h - terrain[1]
        summation_theta_zero = summation_theta_zero + error
        summation_theta_one = summation_theta_one + error * terrain[0]

    theta_0_deriv = 2 * summation_theta_zero / len(data)
    theta_1_deriv = 2 * summation_theta_one / len(data)

    theta_0 = theta_0 - alpha * theta_0_deriv
    theta_1 = theta_1 - alpha * theta_1_deriv

    return theta_0, theta_1


def fit(data, theta_0, theta_1, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de theta_0 e theta_1.
    Ao final, retorna duas listas, uma com os theta_0 e outra com os theta_1
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os theta_0 e outra com os theta_1 obtidos ao longo da execução
    """

    theta_0_list = []
    theta_1_list = []

    for iteration in range(num_iterations):
        thetas = step_gradient(theta_0, theta_1, data, alpha)
        theta_0 = thetas[0]
        theta_1 = thetas[1]
        theta_0_list.append(theta_0)
        theta_1_list.append(theta_1)

    # return theta_0, theta_1
    return theta_0_list, theta_1_list


# o valor correto é y = -3.45 + 1.16 * x
f = open('alegrete.csv', 'r')
lines = f.readlines()
matrix = []
for line in lines:
    array = line.split(",")
    price = array[1].replace("\n", "")
    matrix.append([float(array[0]), float(array[1])])

thetas = fit(matrix, 1, 1, 0.01, 2000)
# print(compute_mse(thetas[0], thetas[1], matrix))
# print(thetas[0][1900])
