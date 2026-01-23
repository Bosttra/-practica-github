#85. Te piden realizar un programa en que gestionen la media y la mediana de varias de tres 
#asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el 
#programa debe mostrar la media y mediana los todos los alumnos introducidos
alumnes=[]
notes=[]
mediana=[]
rep=True
def notes_recolecte():
   alumnes.append(input("Introdueix el nom de l'alumne: "))
   notes.append(input("introdueix la nota d'angles: "))
   notes.append(input("introdueix la nota de castella: "))
   notes.append(input("introdueix la nota de catala: "))

while rep==True:
   notes_recolecte()
   rep=input("vols repetir? si/no: ")
   if rep.lower() in "sisí":
      rep=True

mediana.copy( x for x in range(3) )