cif=int(input("introdueix numero de xifres: "))
# cif es per abrebiar cifra
num=input("introdueix el valor: ")
# num es per abrebiar numero
suma=0
# suma es la variable que contara la suma de les xifres
if len(num)!=cif:
    print("Error, no coincideix amb el numero de xifres introduides")
    # es mante el format de sortida pero amb catala que s`hem fa mes comoda
else:
    for x in num:
        suma+=int(x)
        # suma+= es el mateix que "suma= suma + int(x)" pero mes rapid
    print("la suma total dels digits introduits es",suma)