#importar librería
import turtle
#definir color de fondo
turtle.bgcolor("black")
#arreglo para seleccionar el color de la figura
c = ("yellow", "blue", "red", "yellow", "blue", "red", "yellow")
#tamaño de pincel
turtle.pensize(6)
turtle.speed(0)
#funcion que dibuja un cuadrado
def f1(a):
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
#funcion recursiva
def fractal(a, b, d):    
    if(a>d or b<0):
        return
    if(b==6):
        turtle.color( c[b] )
        b=0
    else:
        turtle.color( c[b] )
        b=b+1

    turtle.forward(a)
    turtle.right(50)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(50)
    turtle.forward(a)
    turtle.right(90)
    turtle.left(50)

    #f1(a-1.2)
    fractal(a+1,b, d)
#fractal(tamaño inicial, color(1-6), tamaño final)
fractal(5, 1, 50000)
#termina la gráfica
turtle.done()
