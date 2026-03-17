import  random
Lista_partida=[]
#conte el estat de la partida

Lista_ahorcado=["A","H","O","R","C","A","D","O",0]
#conte els errors de la partida

Lista_palabrasecreta=["maduixa","escombra","llampada","cargol","estelada","piruleta","xarxa","tortuga","bruixot"]
#conte les paraules

llista_errors=[]
#conte les lletres que no s'an probat y no estan en la paraula

palabra=""
#conte la paraula a adibinar

x=""
#conte la lletra a comprovar

rep=True
#controla les repeticions

def repetir(x):
    y=False
    while y==False:
            if x==1:
                rep=input("Vols repetir?")
            else:
                rep=input("Vols afegir una paraula?")

            if rep.lower() in "sísi":
                y=True
            elif rep.lower() in "no":
                y=None
            else:
                print("Error")
    return y

def menu(x):
    if x==1:
        print("******Menu******")
        print("1: ahrcado normal")
        print("2: ahrcado normal amb txt.(es poden repetir les paraules)")
        print("t: tancar")
        x=2
    if x==2:
        global opcio
        opcio=input("escull opció que es vol: ")
        if opcio.isnumeric():
            opcio=int(opcio)
        match opcio:
            case 1|2:
                joc()
            case "t":
                return
            case _:
                print("Error")
                menu(2)

def escollir():
    global Lista_partida
    if opcio==2:
        Lista_palabrasecreta=open("palabra.txt","r",encoding="utf-8").read().splitlines()
    if opcio==1:
        Lista_palabrasecreta=["maduixa","escombra","llampada","cargol","estelada","piruleta","xarxa","tortuga","bruixot"]
    palabra=random.choice(Lista_palabrasecreta)
    Lista_partida.clear()
    for j in palabra:
        Lista_partida.append("_")
    Lista_palabrasecreta.remove(palabra)
    palabra=list(palabra)
    return palabra

def x_definr(x,y):
    x=str(x)
    if len(x)==1:
        if x.isnumeric():
            print("es un numero")

            x_definr(input("introdueix lletra: \n").lower(),y)

        elif not x.isalnum() or x.isspace():
            print("simbol erroni.") 

            x_definr(input("introdueix lletra: \n").lower(),y)

        else:
            y=""
            if y==1:
                return x
            else:
                for j in x:
                    y+=j
                return y
        
    elif len(x)==0:
        print("no s'ha escrit res")

        x_definr(input("introdueix lletra: \n").lower(),y)

    else:
        for j in x:
            z=False
            if j.isnumeric():
                print("numeros no exceptats")
                break
            elif not j.isalnum() or x.isspace():
                print("simbols no acceptats")
                break
            else:
                z=True
                
        if z==True:
            return list(x)

def joc():
    global Lista_partida
    global llista_errors
    global palabra
    global Lista_ahorcado

    llista_errors.clear()
    Lista_ahorcado.append(0)
    Lista_ahorcado.pop(8)
    palabra=escollir()

    while Lista_ahorcado[8]!=8 and "_" in Lista_partida:

        print(Lista_partida)
        print(f"lletres no contingudes: {llista_errors}")
        print(f"errors: {Lista_ahorcado[8]}: ", Lista_ahorcado[0:Lista_ahorcado[8]])
        x=x_definr(input("introdueix lletra: \n").lower(),1)

        if type(x)==str:
            if x in palabra:
                for j in range(len(palabra)):
                    if palabra[j]==x:
                        Lista_partida.pop(j)
                        Lista_partida.insert(j,x)

                print( "Correcte!")

            else:
                llista_errors.append(x.upper())
                llista_errors.sort()
                Lista_ahorcado.append(Lista_ahorcado[8]+1)
                Lista_ahorcado.pop(8)

                print("incorrecte!")
            
        else:
            correcte=""
            for j in range(0,len(x)):
                correcte=False
                if x[j].lower()==palabra[j]:
                    correcte=True
                else:
                    correcte=False  
                    break    
            if correcte==True:
                print("correcte")  
                Lista_partida= palabra.copy()

            else:
                y=""
                for j in x:
                    y+=j
                llista_errors.append(y)
                Lista_ahorcado.append(Lista_ahorcado[8]+1)
                Lista_ahorcado.pop(8)
                                
                print("error") 
    rep=repetir(2)
    if rep:
        Lista_palabrasecreta.append(x_definr(input("introdueix paraula: \n").lower(),2))

    rep=repetir(1)
    if rep==True:
        joc()




        
menu(1)

#https://programacion.net/articulo/escribir_y_leer_ficheros_en_python_1446
