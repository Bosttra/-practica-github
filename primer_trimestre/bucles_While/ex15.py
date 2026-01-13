#64. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:
#a) total de pares
#b) total de impares
#c) total de números positivos
#d) total de números negativos
#e) total de ceros
#f) total de la suma de todos los números introducidos
x=0
par=0
impar=0
pos=0
neg=0
ceros=0
total=0

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

print("el total de pars es: ",par)
print("el total de impars es: ", impar)
print("el total e nagatius es: ", neg)
print("el total de positius es: ",pos)
print("el total de seros es: ",ceros)
print("la suma total de tots els numeros es: ", total)
