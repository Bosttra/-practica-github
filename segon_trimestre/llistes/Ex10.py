#78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea 
#eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir
lista=["a","b","D","x","r","X","3","h","w","2","i"]
x="A"
print(lista)
while x.isalpha():
    x=input("que valor numerico quieres suprimir? ")
    if x.isalpha():
        print("Error: nomes es permeten eliminar numeros")
    elif x not in lista:
        print(f"Error: {x} no esta en la llista")
        x="A"
lista.remove(x)
print("le llista final es:")
print(lista)