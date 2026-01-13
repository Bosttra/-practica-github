#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa 
#debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random
x=random.randint(1,5)
y=""
while not y==x:
    y= int(input("introdueix valor entre 1_5: "))
    if y<1 or y>5:
        print("baror no entre el rang")
    elif x!=y:
        print("valor incorrecte")
print("valor correcte")