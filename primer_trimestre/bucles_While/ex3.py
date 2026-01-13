#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por 
#pantalla. El programa preguntará si deseas o no repetir la operación. Con While
x=True
while x==True:
    num1=float(input("introdueix un numero per sumar: "))
    num2=float(input("introdueix un altre numero per sumar: "))
    print(F"la suma de {num1} mes {num2} es {num1+num2}.")
    x=input(" vols tornar a repetir? Sí/No")
    if x.lower()=="sí" or x.lower()=="si":
        x=True
print("final del progrma.")