milista=[1,2,3,4,5,6]
por2=[]
maximo=max(milista)
#max trova el valor maxim de la llista. min el minim
minim=min(milista)
suma=sum(milista)
print(milista)
print("maximo: ",maximo)
print("minimo: ",minim)
print("suma total: ", suma)

for j in milista:
    por2.append(j*2)
    
milistapro=[n*2 for n in milista]

print(por2)