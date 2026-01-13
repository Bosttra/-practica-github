#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para 
#no distinguir entre mayúsculas y minúsculas
x="A quién madruga Dios ayuda"
x=x.lower()
y=x.find("Dios.")
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