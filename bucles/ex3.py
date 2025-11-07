#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.
x=int(input("introdueix el numero de notas que vols introduir: "))
for y in range(x):
    z=float(input("introdueix nota"))
    if z>=5:
        print("estas aprovat")
    else:
        print("estas suspes")