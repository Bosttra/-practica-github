#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario.
x=int(input("introdueix fins a quin numero vols que es sumin els dos primers numeros naturals: "))
total=0
for y in range(1,x):
    total=total+y
print(total)