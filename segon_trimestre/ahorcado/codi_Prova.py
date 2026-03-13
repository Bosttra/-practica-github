import random
palabras=open("palabra.txt","r",encoding="utf-8").read().splitlines()
x= random.choice(palabras)
print(x)
