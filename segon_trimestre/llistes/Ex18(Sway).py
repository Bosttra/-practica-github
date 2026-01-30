#86. Realiza el ejercicio del DNI que encontrarás en el Sway
llista_intents=[]
DNIcorectes=[]
DNIincorectes=[]
rep=True
lletres=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
while rep==True:
    x=input("introdueix els valors numerics del DNI: ")
    if len(x)!=8:
        DNIincorectes.append(x)
        llista_intents.append(0)
        print("ERROR; ERROR DE LLARGADA")
    elif not x.isnumeric():
        DNIincorectes.append(x)
        llista_intents.append(1)
        print("ERROR; VALORS NO NUMERICS")
    elif not int(x)%23>=0 or not int(x)%23<=22:
        DNIincorectes.append(x)
        llista_intents.append(2)     
        print("ERROR; DNI INCORRECTE")
    else:
        llista_intents.append(3)
        x+=lletres[int(x)%23]
        DNIcorectes.append(x)
        print("DNI ES: ",x)
    rep=input("\nVOLS REPETIR? s/n: ")
    if rep.lower() in "sisí":
        rep=True


print("\n*************MENU*************\n")
print("1: LISTAR DNI CORRECTOS DE MAYOR A MENOR")
print("2: LISTAR DNI INCORRECTOS DE MAYOR A MENOR")
print("3: NUMERO TOTAL DE ERRORES")
print("4: NUMERO TOTAL DE DNI CORECTOS")
print("5: PORCENTAGE DE DNI INCORRECTOS")
print("6: FINALITZAR PROGRAMA\n")

rep=int(input("INTRODUEIX VALOR D'INSTRUCCIÓ: "))

match rep:
    case 1:
        DNIcorectes.sort()
        print("ELS DNI CORRECTES SON:", DNIcorectes)
    case 2:
        DNIincorectes.sort()
        print("ELS DNI CORRECTES SON:", DNIincorectes)
    case 3:
        x=llista_intents.count(0)+llista_intents.count(1)+llista_intents.count(3)
        print(x)
