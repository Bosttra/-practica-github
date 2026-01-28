#86. Realiza el ejercicio del DNI que encontrarás en el Sway
llista_intents=[]
llista_nums=[]
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
    elif x.isalnum():
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
    rep=input("VOLS REPETIR? s/n: ")
    if rep.lower() in "sisí":
        rep=True