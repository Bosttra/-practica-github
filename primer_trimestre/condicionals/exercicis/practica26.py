#26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si 
#está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición
x=input("introduce una letra en mayuscula o minuscula")
if x.isupper()==True:
    print("es mayuscula")
if not x.isupper()==True:
    print("es minuscula")
