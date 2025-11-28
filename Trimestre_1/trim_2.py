x=0
# x es el valor introduit pero per anar mes rapid poso "x"
pos=0
# pos es per abrebiar posicio
neg=0
# neg es per abrebiar negatiu
for j in range(6):
    x=int(input("introdueix el valor: "))
    if x<0:
        neg+=x
         # suma+= es el mateix que "neg= neg + x" pero mes rapid
    else:
        pos+=x
        # suma+= es el mateix que "neg= neg + x" pero mes rapid

print("la suma dels numeros positius es: ", pos)
print("la suma dels numeros negatius es: ", neg)
