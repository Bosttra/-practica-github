#66. Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo 
#se comporta el dado en lanzamientos producidos durante aprox 3 segundos. 
import time
import random
inicio=time.time()
un=0
dos=0
tres=0
cuatre=0
cinc=0
sis=0
set=0
#linea perque es pugui marcar la el comencement
while (time.time()-inicio)<3:
    tte=random.randint(1,6)
    match tte:
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
print("el temps que ha trigat és: ",time.time()-inicio)
print("les vegades que ha sortit el numero 1 és: ",un )
print("les vegades que ha sortit el numero 2 és: ", dos)
print("les vegades que ha sortit el numero 3 és: ",tres )
print("les vegades que ha sortit el numero 4 és: ",cuatre )
print("les vegades que ha sortit el numero 5 és: ",cinc )
print("les vegades que ha sortit el numero 6 és: ", sis)
