#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir 
#notas inferiores a 0 y superiores a 10
x=int(input("introdueix el numero de notas que vols introduir: "))
for y in range(x):
    z=float(input("introdueix nota: "))
    if z<=10 and z>=0:
        if z>=5:
            print("estas aprovat")
        else:
            print("estas suspes")
    else:
        print("nota no valida")