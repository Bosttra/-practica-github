#77. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras 
#y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás 
#en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
nums=[]
orde=""
letra=[]
maj=0
print("Cantidad total de valores: ", len(lista1))
for x in lista1:
    if x.isnumeric():
        nums.append(int(x))
    else:
        letra.append(x)
        if x.isupper():
            maj+=1
orde=input("vols el orde de numeros ascendent? si/no")
if orde.lower() in "sísi":
    nums.sort()
else:
    nums.sort(reverse=True)

orde=input("vols el orde de lletres alfaveticamen? si/no")
if orde.lower() in "sísi":
    letra.sort()
else:
    letra.sort(reverse=True)
print("Cantidad de números: ", len(nums))
print("Cantidad de letras: ", len(letra))
print("Cantidad de mayúsculas: ", maj)
print("Suma de los valores numéricos: ", sum(nums))
print("els numerso de la llista ordenada son: ", nums)
print("les lletres de la llista ordenada son: ", letra)