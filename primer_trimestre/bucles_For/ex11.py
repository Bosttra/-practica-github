#45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string
#distinguiendo vocales y las consonantes:
vocal=""
cons=""
x=input("introduce una palabra: ")
for i in x:
    if i.lower() in "aeiouëéèáàäíìïóòöúùü":
        vocal+=i
    else:
        cons+=i
print(f"en la paraula {x} hi ha les vocals {vocal} i les consonants {cons}")