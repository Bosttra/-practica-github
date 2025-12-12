#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El 
#resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un 
#resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso
#(raíz y división).
import math
X=float(input("introdueix valor: "))
print("la arrec cuadrada es: ", round(math.sqrt(X)))
print("la divi es: ", round((math.sqrt(X))/2))