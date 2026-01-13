#61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es superior o igual a 40.

x=int(input("introdueix nombre: "))
multi=0

while not multi==11 and not multi*x>40:
    print(f"{x} x {multi} = {multi*x}")
    multi+=1
