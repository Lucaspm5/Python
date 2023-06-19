carros = ['gol', 'golf', 'ferrari']
consumo = [55, 99, 108]

economico = carros[consumo.index(min(consumo))]

print(economico)

quilometragem = [0] * 3
for i in range(len(economico)):
    quilometragem[i] = 1000 /consumo[i]
for i in range(3):
    print(f'modelo {carros[i]} - consumo {quilometragem[i] :.2f}')