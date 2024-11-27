import math

raio = float(input("Digite o valor do RAIO: "))

perimetro = 2 * math.pi * raio

area = math.pi * (raio ** 2)

volume = (4/3) * math.pi * (raio ** 3)

print(f"Perímetro da Circunferência: {perimetro:.2f}")
print(f"Área da Circunferência: {area:.2f}")
print(f"O Volume da Esfera é: {volume:.2f}")