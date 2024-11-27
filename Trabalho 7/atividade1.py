import turtle

tamanho = int(input("Insira o tamanho do lado do quadrado: "))

screen = turtle.Screen()
screen.title("Desenho de um Quadrado")

t = turtle.Turtle()

def desenhar_quadrado(tamanho):
    for _ in range(4):
        t.forward(tamanho)
        t.right(90)

desenhar_quadrado(tamanho)

turtle.done()
#pelo que percebi , tive que utilizar numeros grandes para o quadrado ser desenhado mas a partir de 80 ja da para ver bem