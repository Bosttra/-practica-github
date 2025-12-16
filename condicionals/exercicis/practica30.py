#30. Realiza un programa que controle si la longitud de una frase introducida por teclado es
#igual, menor o mayor de 11 caracteres. Utiliza elif
x=input("introdueix una frase: ")
x=len(x)
if x<11:
    print("no te 11 caracters")
elif x==11:
    print("te 11 caracters")
else:
    print("te mes de 11 caracters")