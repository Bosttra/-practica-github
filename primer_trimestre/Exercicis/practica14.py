#14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área 
#y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el 
#resultado a un decimal.
import math
x=float(input("introdueix valor del diametre: "))
print(f"el perimetro es {round(math.pi*x,1)}")
print(f"el area es {round((x/2)**2*math.pi, 1)}")

