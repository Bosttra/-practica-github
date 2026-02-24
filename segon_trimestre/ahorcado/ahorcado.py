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
    palabra=list(Lista_palabrasecreta[random.randint(0,len(Lista_palabrasecreta))])
    Lista_partida.clear()
    for j in palabra:
        Lista_partida.append("_")
    return palabra

def x_definr():
    x=""
    while not x.isalpha():
        x=input("introdueix lletra: \n").lower()
        print(f"lletres no contingudes: {llista_errors}")
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
    
    llista_errors.clear()
    while Lista_ahorcado[8]!=8 and "_" in Lista_partida:
        print(Lista_partida)
        x=x_definr()
        if type(x)==str:
            if x in palabra:
                for j in range(len(palabra)):
                    if palabra[j]==x:
                        Lista_partida.pop(j)
                        Lista_partida.insert(j,x)
                print("Correcte!")
            else:
                llista_errors.append(x.upper()).sort()
                Lista_ahorcado.append(Lista_ahorcado[8]+1)
                Lista_ahorcado.pop(8)
                print("incorrecte!")
        else:
            if str(x).lower()== palabra:
                print("correcte")
            else:
                print("error")
                llista_errors.append(x)
        print(f"errors: {Lista_ahorcado[8]}: ", Lista_ahorcado[0:Lista_ahorcado[8]])

def repetir():
    rep=input("Vols repetir?")
    if rep.lower() in "sísi":
        rep=True
    elif rep.lower() in "no":
        return rep
    else:
        print("Error")
        repetir()
        
while rep==True:
    palabra =escollir()
    joc()
    rep = repetir()
print("adivina la paraula: ")


