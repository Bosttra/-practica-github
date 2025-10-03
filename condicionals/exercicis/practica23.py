#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un 
#notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota 
#introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos
x=float(input("introdueix la teva nota sobre 10: "))
if not x>=0 and x<=10:
    print("no esta entre el intelval permes") 
else:
    if x<5:
        print("has suspes!")
    elif x>=5:
        if x<6.5:
            print("has aprovat pero amb un satisfactori")
        elif x<8.5:
            print("has aprovat pero amb un notable ")
        else:
            print("has aprovat pero amb un excelent")