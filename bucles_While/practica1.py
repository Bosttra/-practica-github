import random
secret=random.randint(1,20)
x=""
x=int(input("eivina el numero de 1-20: "))
while x!=secret :
    if x<0 or x>20:
        print("numero no entre 1_20: ")
    else:
        print("numero incorrecte torna a provar.")
    x=int(input("eivina el numero: "))
print("correcte")