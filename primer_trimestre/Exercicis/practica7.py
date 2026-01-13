#7. programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes 
#forzar que el resultado de la división tenga 2 decimales?

var1=float(input("un numero: "))
var2=float(input("un alter: "))
tatal_suma=var1+var2
total_resta=var1-var2
total_multi=var1*var2
total_potencia=var1**var2
total_divi=round(var1/var2 )
total_diviTot=round(var1//var2, 2)
total_divirest=var1%var2

print(" suma", tatal_suma)
print("resta", total_resta)
print("multi", total_multi)
print("divi", total_divi)
print("resta de divi", total_divirest)
print("divi sencer", total_diviTot)
print("potencia", total_potencia)