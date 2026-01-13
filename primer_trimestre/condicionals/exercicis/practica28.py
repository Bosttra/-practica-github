#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza 
#elif
x=input("introduce una letra en mayuscula o minuscula")
if x.isnumeric():
    print("el valor introducido no es correcto")
elif not x.isalpha():
     print("el valor introducido no es correcto")
else:
    if x.isupper()==True:
        print("es mayuscula")
    if not x.isupper()==True:
      print("es minuscula")

