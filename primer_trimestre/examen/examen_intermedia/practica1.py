nombre=input("introduce tu nombre: ")
edad=int(input("introduce tu edad"))
if edad>0 and edad<100:
    ano_actual=2025
    futuro=ano_actual + (100-edad)
    print("hola", nombre.upper(), "cumpliras 100 años en el año", futuro)
else:
print("edad no valida")