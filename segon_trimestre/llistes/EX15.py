#83. Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta 
#que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente 
#manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así 
#sucesivamente.
#Una vez el usuario desea finalizar el programa tiene que sumar todas tus puntuaciones obtenidas. 
#Si el total supera la media de la puntuación posible de todas las partidas, se puede decir que la 
#suerte le acompaña, de lo contrario mejor no Se dediques a los juegos de azar . PISTA.. ¿existe 
#algún método que permita sumar el contenido de una lista?
import random
rep=True
while rep==True:
    y=""
    llista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
    print(llista)
    x=random.randint(0,len(llista))
    while llista[x]!=y:
        y=input("intanta adivinar el valor de la llista pensat: ")
        if llista[x]!=y:
            print("incorrecte")
    print("Correcte")
    rep=input("volse repetir? sí/no: ")
    if rep.lower() in "sisí":
        rep=True
