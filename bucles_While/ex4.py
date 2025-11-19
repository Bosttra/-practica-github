#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las 
#sumas y el número de repeticiones. Con While
x=True
rep=0
tot=""
while x==True:
    rep+=1
    num1=float(input("introdueix un numero per sumar: "))
    num2=float(input("introdueix un altre numero per sumar: "))
    print(F"la suma de {num1} mes {num2} es {num1+num2}.")
    tot=str(tot)+" "+ str(num1+num2)
    x=input(" vols tornar a repetir? Sí/No ")
    if x.lower()=="sí" or x.lower()=="si":
        x=True
print("final del progrma.")
print(f"has repetit el programa {rep} i els valors han sigut {tot}")