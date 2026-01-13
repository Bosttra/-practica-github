import math
x=input("introdueix el radi del cilindre: ")
y=input("introdueix el altura del cilindre: ")
May=input("vols resultat en minusculas o majusculas")
if not  x.isnumeric()== True or  y.isnumeric()== True:
    print("error")
elif not May.lower()== "minusculas"or "majusculas":
    print("error")
else:
    if May=="majusculas":
        print("EL VOLUMEN ES: ", (math.pi * x**2)*y)
    else:
        print("el volumen es: ", (math.pi * x**2)*y)