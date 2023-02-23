Gabriel Arruda dos Santos - 00290400

Rafael Marques Rache - 00288050

Matheus Hiroyuki Suwa Moura - 00305685


Para o problema Eight Queens a melhor combinação de parâmetros encontrada que
não leva muito tempo para a execução é: run_ga(64, 256, 32, 0.5, 1).
- 64 gerações
- 256 indivíduos
- 32 participantes no sorteio
- 0.5 probabilidade de mutação
- 1 elite

Para gerar o gráfico basta chamar run_ga_with_plot(64, 256, 32, 0.5, 1).
Obs: Necessário ter o matplotlib instalado no python

Para o problema de Alegrete os valores para a melhor execução foram:
fit(matrix, 1, 1, 0.01, 2000)
- 1 para theta_0 e theta_1
- 0.01 de alpha
- 2000 iterações

O melhor erro quadrático médio obtido foi 8.52