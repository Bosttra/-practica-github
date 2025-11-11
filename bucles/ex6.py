#40. Crea un programa que cuente todos los números pares hasta el número 50
total=0
for x in range(0,50,2):
    total+=1
totalin=50-total
print("el total de pars es: ", total)
print("el total de inpars es: ",totalin)