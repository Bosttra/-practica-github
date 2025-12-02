#60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. 
#Utiliza únicamente el while
x=int(input("introdueix nombre: "))
multi=0
while not multi==11:
    print(f"{x} x {multi} 0 {multi*x}")
    multi+=1