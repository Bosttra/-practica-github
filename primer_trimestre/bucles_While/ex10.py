#59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que 
#intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o 
#menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe 
#mostrarse por pantalla un mensaje y el número de intentos.
import random
numero=random.randint(1,1000)
x="!"
intents=0
while not x==numero:
    intents+=1
    x=int(input("adivina el numero pensat entre el 1 i el 1000: "))
    if x<1 or x>1000:
        print(f"nmero {x} no entre el rang")
    elif x<numero:
        print(f"numero {x} menor a numero pensat")
    elif x>numero: 
        print(f"numero {x} major a numero pensat")
    else:
        print("numero correcte")
print("intents utilitzats", intents)