#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te 
#indique en qué posición de la palabra se encuentra la letra.
x=input("introdueix una paraula secreta: ")
for i in range(len(x)):
    p=input("introdueix lletra: ")
    if p in x.lower():
        print(f"la lletra {p} es correcte")
        for a in range(len(x)):
            if p in x[a]:
                print(f"esta en la posició: ",a+1 )
    else:
        print(f"la lletra {p} es incorrecte")
    print(" te quedan",len(x)-i-1 ,"intentos")