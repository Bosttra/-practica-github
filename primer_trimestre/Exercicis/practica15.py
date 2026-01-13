#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, 
#introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.

import math
d=float(input("introdueix diametre: "))
H=float(input("introdueix altura: "))
print(f"el perimetre es {math.pi*d*H}")
print(f"el area es {(math.pi*(d/2)**2)*H}")
