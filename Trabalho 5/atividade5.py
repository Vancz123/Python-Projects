import math

numero = int(input("Insira um número inteiro: "))

quadrado = numero ** 2
cubo = numero ** 3
raiz_quadrada = math.sqrt(numero)

print(f"O quadrado de {numero} é: {quadrado}")
print(f"O cubo de {numero} é: {cubo}")
print(f"A raiz quadrada de {numero} é: {raiz_quadrada:.2f}")
