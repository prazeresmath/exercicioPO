from pulp import LpProblem, LpVariable, lpSum, LpStatus, LpInteger, LpMaximize
import time

capacidade_mochila = 50

pesos = {i: i+1 for i in range(1, 26)}
valores = {i: 10*i for i in range(1, 26)}

print(f'Capacidade da mochila: {capacidade_mochila}')
def solucao_exata():  
    peso_total = 0
    valor_total = 0
    itens_selecionados = []

    problema = LpProblem('Problema da Mochila', LpMaximize)

    variaveis = LpVariable.dicts('Item', list(range(1, 26)), 0, 1, LpInteger)    

    # Função objetivo: soma os valores dos itens
    problema += lpSum([valores[i]*variaveis[i] for i in range(1, 26)])
    # A soma não pode passar de 50
    problema += lpSum([pesos[i]*variaveis[i] for i in range(1, 26)]) <= capacidade_mochila

    inicio = time.time()
    problema.solve()
    tempo_execucao = time.time() - inicio

    print('Método exato:')  
    print(f'Solver utilizado: {problema.solver}')
    print('Status:', LpStatus[problema.status])
    for i in range(1, 26):
        if variaveis[i].varValue > 0:
            peso_total += pesos[i]
            valor_total += valores[i]
            itens_selecionados.append(pesos[i])

    print(f'Itens selecionados com otimização: {itens_selecionados}.')
    print(f'Peso total: {peso_total}')
    print(f'Valor total: {valor_total}')
    return peso_total, valor_total, itens_selecionados, tempo_execucao

def solucao_heuristica():
    peso_total = 0
    valor_total = 0
    itens_selecionados = []

    # Calcula a razão valor-peso para cada item
    razoes = {i: valores[i] / pesos[i] for i in range(1, 26)}
    # Ordena os itens com base na razão valor-peso em ordem decrescente
    itens_ordenados = sorted(razoes, key=lambda i: razoes[i], reverse=True)    

    inicio = time.time()
    for item in itens_ordenados:
        if peso_total + pesos[item] <= capacidade_mochila:
            peso_total += pesos[item]
            valor_total += valores[item]
            itens_selecionados.append(pesos[item])
    tempo_execucao = time.time() - inicio

    print('-' * 30)
    print('Heurística:')
    print('Itens selecionados pela heurística:', itens_selecionados)
    print('Peso total:', peso_total)
    print('Valor total:', valor_total)

    return peso_total, valor_total, itens_selecionados, tempo_execucao

peso_total_exato, valor_total_exato, itens_selecionados_exatos, tempo_execucao_exato = solucao_exata()
peso_total_heuristica, valor_total_heuristica, itens_selecionados_heuristica, tempo_execucao_heuristica = solucao_heuristica()

print('-' * 30)
print('Comparação:')
print('Solução exata: ', valor_total_exato)
print('Solução da heurística: ', valor_total_heuristica)

print(f'Itens selecionados na solução exata: {itens_selecionados_exatos}')
print(f'Itens selecionados na heurística: {itens_selecionados_heuristica}')

print(f'Tempo de execução na solução exata: {tempo_execucao_exato} segundos')
print(f'Tempo de execução na heurística: {tempo_execucao_heuristica} segundos')
