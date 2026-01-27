#84. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las 
#palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la 
#palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra. 
import random
llista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
paraula=list(llista[random.randint(0,len(llista))])
desordenada=paraula.copy()
random.shuffle(desordenada)

x=""
while x!=paraula:
    print(desordenada)
    x=list(input("intenta ordenar la paraula: "))
    if x == paraula:
        print("correcte")
    else:
        print("no has acertat")

