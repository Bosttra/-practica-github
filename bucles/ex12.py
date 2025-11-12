#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la 
#palabra Abrigo utilizando únicamente una instrucción.
vocal=""
cons=""
x=input("introduce una palabra: ")
for i in x:
    if i.lower() in "aeiouëéèáàäíìïóòöúùü":
        vocal+=i
    else:
        cons+=i
print(f"en la paraula {x} hi ha les vocals {vocal} i les consonants {cons}")