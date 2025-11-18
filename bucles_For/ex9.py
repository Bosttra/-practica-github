#43. Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima 
#por pantalla cada letra
x=input("introduce una palabra: ")
rec=0
for i in x:
    rec+=1
    print(f"en la posicion {rec} est la letra {i}")