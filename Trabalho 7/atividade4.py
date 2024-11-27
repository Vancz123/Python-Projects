import turtle
import random

tela = turtle.Screen()
tela.bgcolor("black")
tela.title("Atividade 1 com escolha")

t = turtle.Turtle()
t.speed(1)
turtle.colormode(255)

cores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]

def desenhar_circulo(raio):
    t.circle(raio)


def desenhar_quadrado(lado):
    for _ in range(4):
        t.forward(lado)
        t.right(90)


def desenhar_retangulo(lado1, lado2):
    for _ in range(2):
        t.forward(lado1)
        t.right(90)
        t.forward(lado2)
        t.right(90)


def desenhar_forma():
    while True:
        forma = input("Qual forma deseja desenhar? (círculo, quadrado, retângulo): ").lower()
        if forma in ['circulo', 'quadrado', 'retangulo']:
            break
        else:
            print("Opção inválida! Por favor, escolha uma das opções: círculo, quadrado, ou retângulo.")

    # Perguntar o tamanho conforme a forma escolhida
    if forma == 'circulo':
        raio = int(input("Informe o raio do círculo: "))
        desenhar_circulo(raio)

    elif forma == 'quadrado':
        lado = int(input("Informe o tamanho do lado do quadrado: "))
        desenhar_quadrado(lado)

    elif forma == 'retangulo':
        lado1 = int(input("Informe o tamanho do primeiro lado do retângulo: "))
        lado2 = int(input("Informe o tamanho do segundo lado do retângulo: "))
        desenhar_retangulo(lado1, lado2)


def posicionar_tartaruga():
    # Escolher posição aleatória
    t.penup()
    t.goto(0, 0)
    t.pendown()

    # Escolher cor aleatória
    cor = random.choice(cores)
    t.color(cor)


for _ in range(5):  # Número de formas que serão desenhadas
    posicionar_tartaruga()
    desenhar_forma()

# Finalizar a janela ao clicar
turtle.done()
