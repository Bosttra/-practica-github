#19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales

x=float(input("introdueix un numero: "))
y=float(input("introdueix un numero: "))
if x==y:
    print("son iguales")
else:
    if x<y:
        print( y, "es major")
    else:
        print(x, "es major")
