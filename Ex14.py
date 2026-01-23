#82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al 
#azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine 
#la palabra
import random
y=""
llista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
print(llista)
x=random.randint(0,len(llista))
while llista[x]!=y:
    y=input("intanta adivinar el valor de la llista pensat: ")
    if llista[x]!=y:
        print("incorrecte")
print("Correcte")