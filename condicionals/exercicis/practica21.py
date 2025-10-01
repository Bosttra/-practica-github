# Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
import math
a=float(input("introduce el valor a"))
b=float(input("introduce el valor b"))
c=float(input("introduce el valor c"))
arrel=(b**2 )-4*a*c
if arrel<0:
    print("la arrel cuadrada es negativa")
else :
    totsum= (-b + math.sqrt(arrel))/2*a
    totres= (-b - math.sqrt(arrel))/2*a
    print("primera opció: ", totsum)
    print("segona opció: ", totres)