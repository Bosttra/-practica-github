llistanum=[]
llistanonum=[]
llistatot=[]

frase=input("introsueix valors separats per un guio: ")

print(frase)
llistatot=frase.split("-")
print(llistatot)
#split() converteix un string en una llista separant els valors per el lloc indicat

for x in llistatot:
    if x.isnumeric():
        llistanum.append(int(x))
    else:
        llistanonum.append(x)

print(llistanum)
print(llistanonum)
print(sum(llistanum))