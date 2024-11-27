import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Atividade: Desenho de Quadrados Coloridos Juntos")


t = turtle.Turtle()


cores = ["red", "blue"]
cores2 = ["green", "yellow"]

# Função para desenhar um quadrado com uma cor específica
def desenhar_quadrado(tamanho, cor):
    t.fillcolor(cor)
    t.begin_fill()
    for _ in range(4):
        t.forward(tamanho)
        t.right(90)
    t.end_fill()

# Função para desenhar quadrados juntos
def desenhar_quadrados_juntos(tamanho, quantidade):
    for i in range(2):
        desenhar_quadrado(tamanho, cores[i % len(cores)])
        t.penup()
        t.forward(tamanho)
        t.pendown()


tamanho_quadrado = 50
quantidade_quadrados = 2

t.penup()
t.goto(-quantidade_quadrados * tamanho_quadrado / 2, 0)
t.pendown()

desenhar_quadrados_juntos(tamanho_quadrado, quantidade_quadrados)

def desenhar_quadrados_juntos2(tamanho, quantidade):
    for i in range(2):
        desenhar_quadrado(tamanho, cores2[i % len(cores2)])
        t.penup()
        t.forward(tamanho)
        t.pendown()

t.penup()
t.goto(-quantidade_quadrados * tamanho_quadrado / 2, 50)
t.pendown()

desenhar_quadrados_juntos2(tamanho_quadrado, quantidade_quadrados)

turtle.done()
