#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total 
#de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta 
#preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la 
#operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el 
#mensaje del acumulado es singular o plural.. . Con While

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

print("final del progrma.")
if not rep>1:
    print(f"has repetit el programa {rep} vegada i el valor ha sigut {tot} ",end="")
else:
    print(f"has repetit el programa {rep} vegades i els valors han sigut {tot} ",end="")
print("la suma total es ", sum)