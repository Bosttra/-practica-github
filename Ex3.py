#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en 
#esta lista no deben almacenarse las letras que se han introducido repetidas.
rep=True
x=[]
while rep==True:
    x.append(input("introdueix una lletra: "))
    rep=input("vol repetir?: " )
    if rep.lower() in "sií":
         rep=True
print(set(x))