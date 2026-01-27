#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se 
#irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números 
#ordenados de menor a mayor.
x=int(input("introdueix la cantitat de numeros que vols introduir: "))
tot=[]
for j in range(x):
    tot.append(float(input("introdueix un valor: ")))
    print("valors restants: ", x-(j+1))
print("valors introduits: ",list(set(tot)))