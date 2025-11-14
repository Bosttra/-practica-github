#48. Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de -
#esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario-
#tenga x oportunidades para ver si letra introducida está en esa palabra.-
x=input("introdueix una paraula secreta: ")
for i in range(len(x)):
    p=input("introdueix lletra: ")
    if p in x.lower():
        print(f"la lletra {p} es correcte")
    else:
        print(f"la lletra {p} es incorrecte")
    print(" te quedan",len(x)-i-1 ,"intentos")