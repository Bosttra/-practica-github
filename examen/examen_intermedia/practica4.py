print("opcion / tarifa/ precio/descuento")
print("1: Tarifa Nocturna/ 0.158/5%")
print("2: Tarifa plana/0.192/0%")
print("3: Tarifa solar/ 0.143/8%")
print("4: Tarifa Ecologica/ 0.170/10%")
x=input("introdueix tarifa")
kilovatios=float(input("introduce Kilovatios "))
if x=="1":
    no=0.158* kilovatios
    des= no - no*0.05
