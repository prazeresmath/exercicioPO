prob = LpProblem("Problema da Mochila", LpMaximize)


x = LpVariable.dicts("Item", list(range(1, 26)), 0, 1, LpInteger)


pesos = {i: i+1 for i in range(1, 26)}
valores = {i: 10*i for i in range(1, 26)}


prob += lpSum([valores[i]*x[i] for i in range(1, 26)])


prob += lpSum([pesos[i]*x[i] for i in range(1, 26)]) <= 50


prob.solve()


print("Status:", LpStatus[prob.status])


for i in range(1, 26):
    if x[i].varValue > 0:
        print(f"Item {i} é selecionado.")
