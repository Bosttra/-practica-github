print("el menu es califica per numeros escull el numero asignat a el plat que es vol: ")
print("1: hígado de panda")
print("2: panda rojo a la plancha")
print("3: cuerno de unicornio al vapor")
plato=int(input("escoje el plato: "))
if plato>3 and plato<0:
    print("increible elección!")
    input(" puedes explicarme por que este plato: ")
    print("deacuerdo aqui te viene el plato")
    var1=(input("pon aqui ti nombre para confirmar el pedido. si no lo quiere ponga no:"))
    if var1== "no" or var1== "No":
        print("nada pues asta la proxima")
    else:
        print("aqui te llecgara el plato jonto a una pequeña multa por consumo de alimentos con animales protejidos")
elif plato==3  :
    print("enserio piensas que eso existe?") 
else plato!=1 or plato!=2 or plarto!=3:
    print("este plato no esta en el menu")
