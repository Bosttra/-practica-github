#9. programa que pida los segundos y muestre por pantalla y en la misma frase los minutos 
#y las horas
segundos=float(input("Introdueix segons: "))
min=round(segundos/60, 3)
hora=round(min/60, 3)
print (f"´{segundos} equivalen a {min} minuts i a {hora} horas")