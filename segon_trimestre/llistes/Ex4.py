#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y 
#no deben almacenarse en la lista
rep=True
x=[]
while rep==True:
    x.append(input("introdueix una lletra: "))
    rep=input("vol repetir?: " )
    if rep.lower() in "sií":
         rep=True
print(set(x))