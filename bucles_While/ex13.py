#62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números 
#hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.

x=int(input("introdueix el primer valor: "))
y=int(input("introdueix el segon valor: "))
par=""
inpar=""
if x<y:
    for j in range(x,y+1):
        if j%2==0:
            par+=str(j)+"-"
        else:
            inpar+=str(j)+"-"
else:
    for j in range(y,x+1):
        if j%2==0:
            par+=str(j)+"-"
            
        else:
            inpar+=str(j)+"-"

print("els numeros pars son: ",par[:-1])
print("els numeros inpars son: ",inpar[:-1])