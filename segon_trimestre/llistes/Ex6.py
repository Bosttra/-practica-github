#74. A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de 
#entre las 2 listas.
lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]
repetits=[]
norepetides=[]
for x in lista2:
    if x in lista1:
        repetits.append(x)
    else:
        norepetides.append(x)

for x in lista1:
    if x not in lista2:
        norepetides.append(x)

print("les paraules repetides son: ",repetits)
print("les paraules que no esta repetides de la llista dos son:", norepetides)