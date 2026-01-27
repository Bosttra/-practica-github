#80. Utilizando listas, crea un programa que te permita determinar si un número es decimal o no. 
x=input("introdueix  un valor: ")
dec=list(x.split(","))
if len(x)!=1:
    print(x,"es decimal")
else:
    print(x,"no es decimal")