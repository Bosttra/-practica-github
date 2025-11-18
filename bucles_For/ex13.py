#47. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe 
#mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b 
#la secuencia en descenso. Respeta el formato de salida
x=int(input("introdueix el primer nombre de l'interval: "))
y=int(input("introdueix el segon nombre de l'interval: "))
if x>y:
    for i in range(x,y,-1):
        print(i,"-", end="" ,sep="")
    print(i-1)
else:
    for i in range(x,y):
        print(i,"-", end="" ,sep="")
    print(i+1)   
