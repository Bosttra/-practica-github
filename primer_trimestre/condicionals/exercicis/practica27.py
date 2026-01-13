#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en 
#troducir un número, aparezca un aviso por pantalla
x=input("introduce una letra en mayuscula o minuscula")
if x.isnumeric():
    print("el valor introducido no es correcto")
else:
    if x.isupper()==True:
        print("es mayuscula")
    if not x.isupper()==True:
      print("es minuscula")
