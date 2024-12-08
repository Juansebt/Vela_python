import turtle
import random

# Configuración de la pantalla
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("07/Diciembre")

# Función para dibujar texto
def dibujar_texto(texto, x, y, color, tamano):
    texto_turtle = turtle.Turtle()
    texto_turtle.hideturtle()
    texto_turtle.penup()
    texto_turtle.goto(x, y)
    texto_turtle.color(color)
    texto_turtle.write(texto, align="center", font=("Arial", tamano, "bold"))

# Dibujar los textos en la pantalla
dibujar_texto("Feliz Día de las Velitas", 0, 200, "white", 24)  # Texto en la parte superior
dibujar_texto("By: Juanse", 0, -200, "white", 16)  # Texto en la parte inferior

# Crear la vela
vela = turtle.Turtle()
vela.shape("square")
vela.color("white")
vela.shapesize(stretch_wid=6.4, stretch_len=2)  # Vela más alta y estrecha
vela.penup()
vela.goto(0, -100)  # Ubicar la vela en el centro de la pantalla

# Crear la mecha
mecha = turtle.Turtle()
mecha.shape("square")
mecha.color("gray")
mecha.shapesize(stretch_wid=1.5, stretch_len=0.1)
mecha.penup()
mecha.goto(0, -20)  # Ubicar la mecha sobre la vela

# Función para crear la llama
def crear_llama():
    llama = turtle.Turtle()
    llama.shape("circle")
    llama.color("yellow")
    llama.penup()
    llama.goto(0, 10)  # Posicionar la llama justo sobre la mecha
    llama.shapesize(stretch_wid=1.5, stretch_len=1.5)  # Hacer la llama más grande
    return llama

# Crear una llama grande y estática
llama = crear_llama()

# Función para crear chispas
def crear_chispa():
    chispa = turtle.Turtle()
    chispa.shape("circle")
    chispa.color(random.choice(["yellow", "orange", "red"]))
    chispa.penup()
    chispa.goto(random.uniform(-20, 20), 10)  # Posicionar las chispas sobre la mecha
    chispa.speed(1)  # Asegurarse de que las chispas se muevan rápidamente
    return chispa

# Lista para almacenar las chispas
chispas = []

# Función para simular el parpadeo de la llama y el movimiento de las chispas
def parpadeo_llama():
    while True:
        # Crear nuevas chispas al azar
        if random.random() < 0.1:  # Hay una probabilidad de 10% de crear una chispa nueva
            chispa = crear_chispa()
            chispas.append(chispa)

        # Mover las chispas hacia arriba y aleatoriamente
        for chispa in chispas:
            desplazamiento_x = random.uniform(-2, 2)
            desplazamiento_y = random.uniform(5, 10)
            chispa.setx(chispa.xcor() + desplazamiento_x)
            chispa.sety(chispa.ycor() + desplazamiento_y)
            
            # Si la chispa se aleja demasiado, eliminarla
            if chispa.ycor() > 100:
                chispa.hideturtle()
                chispas.remove(chispa)

# Ejecutar la animación
parpadeo_llama()

# Finalizar el programa al cerrar la ventana
wn.mainloop()
