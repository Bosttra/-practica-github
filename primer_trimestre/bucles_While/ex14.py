#63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número
#de veces que se repite cada número.
import random
input("començar")
un=0
dos=0
tres=0
cuatre=0
cinc=0
sis=0
set=0
#linea perque es pugui marcar la el comencement
for j in range(101):
    x=random.randint(1,6)
    match x:
        case 1:
            un+=1
        case 2:
            dos+=1
        case 3:
            tres+=1
        case 4:
            cuatre+=1
        case 5:
            cinc+=1
        case 6:
            sis+=1
print("les vegades que ha sortit el numero 1 es: ",un )
print("les vegades que ha sortit el numero 2 es: ", dos)
print("les vegades que ha sortit el numero 3 es: ",tres )
print("les vegades que ha sortit el numero 4 es: ",cuatre )
print("les vegades que ha sortit el numero 5 es: ",cinc )
print("les vegades que ha sortit el numero 6 es: ", sis)
