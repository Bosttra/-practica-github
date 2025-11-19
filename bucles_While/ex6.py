#55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior 
#haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y 
#cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While

rep=0
tot=""
sum=0
while sum<50:
    rep+=1
    num1=float(input("introdueix un numero per sumar: "))
    num2=float(input("introdueix un altre numero per sumar: "))
    print(F"la suma de {num1} mes {num2} es {num1+num2}.")
    tot=str(tot)+", "+ str(num1+num2)
    sum+=num1+num2
while sum%2==0:
    rep+=1
    num1=float(input("introdueix un numero per sumar: "))
    num2=float(input("introdueix un altre numero per sumar: "))
    print(F"la suma de {num1} mes {num2} es {num1+num2}.")
    tot=str(tot)+", "+ str(num1+num2)
    sum+=num1+num2


if not rep>1:
    print(f"has repetit el programa {rep} vegada i el valor ha sigut {tot} ",end="")
else:
    print(f"has repetit el programa {rep} vegades i els valors han sigut {tot} ",end="")
print("la suma total es ", sum)

print("final del progrma.")