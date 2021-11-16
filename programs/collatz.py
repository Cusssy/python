import turtle
giro = int(input("Cuantos grados quieres que gire?: "))
velocidad = int(input("Cuanto quieres que avance?: "))
numero = int(input("elije un numero: "))

tree = turtle.Turtle()

def paroinpar(numero):
    while numero > 1:
        if numero % 2 == 0:
            resultado = numero/2
            print(resultado)
            numero = resultado
            tree.right(giro)
            tree.forward(velocidad)
        else:
            resultado = numero*3+1
            print(resultado)
            numero = resultado
            tree.left(giro)
            tree.forward(velocidad)




paroinpar(numero)
input("Pulsa cualquier ENTER para salir")