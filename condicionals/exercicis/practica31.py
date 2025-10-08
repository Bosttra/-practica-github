#. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. 
#Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su 
#índice.
x="A quién madruga Dios ayuda"
y=x.find("Dios")
if y<0:
    print("la palabra Dios no esta en la frase")
else:
    print("la palabra Dios empieza en el caracter", y)
y=x.find("dios")
if y<0:
    print("la palabra dios no esta en la frase")
else:
    print("la palabra dios empieza en el caracter", y)
y=x.find("madruga")
if y<0:
    print("la palabra madruga no esta en la frase")
else:
    print("la palabra madruga empieza en el caracter", y)