import turtle
import random

# Definir a tela
tela = turtle.Screen()
tela.bgcolor("black")
tela.title("Formas Geométricas Aleatórias")

# Definir a tartaruga (objeto de desenho)
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)  # Para utilizar valores RGB

# Cores disponíveis
cores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]

def forma_circulo():
    raio = random.randint(10, 100)
    t.circle(raio)

def forma_triangulo():
    lado = random.randint(50, 150)
    for _ in range(3):
        t.forward(lado)
        t.left(120)

def desenhar_forma():
    # Escolher posição aleatória
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Escolher cor aleatória
    cor = random.choice(cores)
    t.color(cor)

    # Escolher uma forma aleatória para desenhar
    forma = random.choice([forma_circulo, forma_triangulo])
    forma()

# Desenhar várias formas aleatórias
for _ in range(20):  # Número de formas a desenhar
    desenhar_forma()

# Finalizar a janela ao clicar
turtle.done()