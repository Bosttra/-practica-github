#65. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayo y cuál el menor.
x=0
par=0
impar=0
pos=0
neg=0
ceros=0
total=0
may=0
men=0
while x!=-99:
    x=int(input("introdueix valor: "))
    if x%2==0:
        par+=1
    else:
        impar+=1
    if x>0:
        pos+=1
    elif x==0:
        ceros+=1
    else:
        neg+=1
    total+=x
    if may<x:
        may=x
    if men>x:
        men=x
print("el total de pars es: ",par)
print("el total de impars es: ", impar)
print("el total e nagatius es: ", neg)
print("el total de positius es: ",pos)
print("el total de seros es: ",ceros)
print("la suma total de tots els numeros es: ", total)
print("el numero major es: ", may)
print("elo numero menor es: ",men)