x=float(input("introduce in numero: "))
y=float(input("introdueix un altre: "))
total=x/y
rest=x%y
if y%2==0:
 print("el resultat es ", total, "y el resto es ", rest, "a mes el dividendo es par")
else:
  print("el resultat es ", total, "y el resto es ", rest, "a mes el dividendo es impar")