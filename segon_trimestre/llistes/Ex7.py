#75. Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por 
#pantalla los siguientes resultados:
#       a. Cantidad total de valores
#       b. Cantidad de números
#       c. Cantidad de letras
#       d. Cantidad de mayúsculas
#       e. Suma de los valores numéricos
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
nums=0
tot=0
letra=0
maj=0
print("Cantidad total de valores: ", len(lista1))
for x in lista1:
    if x.isnumeric():
        nums+=1
        tot+=int(x)
    else:
        letra+=1
        if x.isupper():
            maj+=1
print("Cantidad de números: ", nums)
print("Cantidad de letras: ", letra)
print("Cantidad de mayúsculas: ", maj)
print("Suma de los valores numéricos: ", sum)


