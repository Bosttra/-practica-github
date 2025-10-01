x=float(input("introdueix un numero: "))
y=float(input("introdueix un numero: "))
if x> 0 and x<10 and y<10 and y>0:
    if x==y:
        print("son iguales")
    elif x<y:
        print( y, "es major")
    else:
        print(x, "es major")
else:
    print(" numero no entre el intervals de 1-10")