import math

raio = float(input("Digite o valor do RAIO: "))

n = 2 * math.pi * raio

numeros_divisiveis_por_10 = []

for i in range(10, int(n), 10):
    numeros_divisiveis_por_10.append(i)

print(f"Perímetro da Circunferência: {n:.2f}")
print(f"Números divisíveis por 10 e menores que {n:.2f}:")
print(numeros_divisiveis_por_10)
