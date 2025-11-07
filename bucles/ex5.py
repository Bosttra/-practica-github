#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por 
#pantalla el número total de positivos, negativos y número de 0
n=int(input("introdueix numero enter: "))
totaln=0
totalp=0
total0=0
for x in range(n):
    x=float(input("introdueix numero: "))
    if x==0:
        total0+=1
    elif x<0:
        totaln+=1
    elif x>0:
        totalp+=1
print("el total de numeros 0 es", total0)
print("el total de numeros negatius es", totaln)
print("el total de numeros positius es", totalp)