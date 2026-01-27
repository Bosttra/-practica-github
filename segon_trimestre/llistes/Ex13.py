#81. A partir de una lista definida, busca el método apropiado para que se visualice un valor de la 
#lista al azar
import random
llista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
print(llista[random.randint(0,len(llista))])