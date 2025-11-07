num1=float(input("introdueix un numero: "))
num2=float(input("introdueix un altre numero: "))
num3=float(input("introdueix un altre numero: "))
frase=input("introdueix una frase: ")
print("frase en minusculas", frase.lower())
print(f"la suma es: {num1 + num2+num3}")
print(f"la media es: {round((num1 + num2 + num3)/2, 2)}")
print(f"el producto es: {num1 * num2 *num3}")
if not (num1 + num2+num3)>(num1 * num2 *num3):
    print("la suma es mayor que el producto? False")
else:
    print("la suma es mayor que el producto? thrue")


