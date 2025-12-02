#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while
import random
x=random.randint(1,5)
y=""
intentos=3
while not y==x and intentos !=0:
    intentos-=1
    y= int(input("introdueix valor entre 1_5: "))
    if y<1 or y>5:
        print("baror no entre el rang")
    elif x!=y:
        print("valor incorrecte")
    else:
        print("valor correcte")
    print(intentos)