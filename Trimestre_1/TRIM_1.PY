min=int(input("introdueix el valor mes patit del interval: "))
# min es per abrebiar minim
max=int(input("introdueix el valor mes gran del interval: "))
# max es per abrebiar maxim
interval=int(input("introdueix interval: "))

#es demana els valors necesaris
tot=""
# es la variable que controla tots els valors
for x in range(min,max+1,interval):
    tot+=str(x)+","
print(tot[:-1])