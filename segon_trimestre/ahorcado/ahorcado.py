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

def escollir():
    global Lista_partida
    palabra=Lista_palabrasecreta[random.randint(0,len(Lista_palabrasecreta))]
    Lista_partida.clear()
    for j in palabra:
        Lista_partida.append("_")
    Lista_palabrasecreta.remove(palabra)
    palabra=list(palabra)
    return palabra

def x_definr():
    x=""
    while not x.isalpha():
        x=input("introdueix lletra: \n").lower()

        if len(x)==1:
            if x.isnumeric():
                print("es un numero")
            elif not x.isalnum() or x.isspace():
                print("simbol erroni.") 
            else:
                return x
        elif len(x)==0:
            print("no s'ha escrit res")
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

    llista_errors.clear()
    Lista_ahorcado.append(0)
    Lista_ahorcado.pop(9)
    palabra=escollir()

    while Lista_ahorcado[8]!=8 and "_" in Lista_partida:

        print(Lista_partida)
        print(f"lletres no contingudes: {llista_errors}")
        print(f"errors: {Lista_ahorcado[8]}: ", Lista_ahorcado[0:Lista_ahorcado[8]])
        x=x_definr()

        if type(x)==str:
            if x in palabra:
                for j in range(len(palabra)):
                    if palabra[j]==x:
                        Lista_partida.pop(j)
                        Lista_partida.insert(j,x)

                print( "Correcte!")

            else:
                llista_errors.append(x.upper())
                llista_errors=set(llista_errors)
                list(llista_errors).sort()
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
            if correcte==True:
                print("correcte")  
                Lista_partida= palabra.copy()

            else:
                
                llista_errors.append(x)
                Lista_ahorcado.append(Lista_ahorcado[8]+1)
                Lista_ahorcado.pop(8)
                                
                print("error") 
    rep=repetir()
    if rep==True:
        joc()



def repetir():
    rep=input("Vols repetir?")
    if rep.lower() in "sísi":
        rep=True
        return rep
    elif rep.lower() in "no":
        return rep
    else:
        print("Error")
        repetir()

joc()


