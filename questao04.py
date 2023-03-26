dataDicio = [
    {'estado':'SP', 'valor':67836.43},
    {'estado':'RJ', 'valor':36678.66},
    {'estado':'MG', 'valor':29229.88},
    {'estado':'ES', 'valor':27165.48},
    {'estado':'Outros', 'valor':19849.53}
]

soma = 0
for i in dataDicio:
    soma = soma + i['valor']

print(soma)

for i in dataDicio:
    perc = (i['valor'] / soma) * 100
    print('O estado {} representa {:.2f}% do faturamento total.'.format(i['estado'], perc))