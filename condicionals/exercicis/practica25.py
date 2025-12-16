#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
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