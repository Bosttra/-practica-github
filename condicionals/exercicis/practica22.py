#. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
x=float(input("introdueix la teva nota sobre 10: "))
if x>=5:
    print("has aprovat!")
else:
    print("has suspes")