var_total=50
#es mante el nom demanat
x=1
# x es el valor introduit pero per anar mes rapid poso "x"
while x!=0 and not var_total>60:
    print(var_total)

    # poso el valor de la variable var_total al principi per no haver de posar break so seria
    #if x!=0 and not var_total>60:
    #break

    x=int(input("introdueix valor: "))
    if x%2==0 and not x==0:
        var_total+=x
        #controlador de si x es par
        
    else:
        var_total-=x
        # tots els valors pars son posibles dividir-los entre dos per tant els que quen son impars
        
print("Final del programa")