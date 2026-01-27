#70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez 
#introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por 
#pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el 
#formato de entrada y salida tal y como se muestra en el testeo.
x=int(input("introdueix la cantitat de paraulas: "))
lista1=[]
lista2=[]
for i in range(x):
    lista1.append( input("introdueix paraula: "))
lista2=lista1.copy()
lista2.reverse()
print(lista2)