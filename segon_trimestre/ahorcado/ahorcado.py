import  random
Lista_partida=[]
#conte el estat de la partida

Lista_ahorcado=["A","H","O","R","C","A","D","O",0]
#conte els errors de la partida

Lista_palabrasecreta=["maduixa","escombra","llampada","cargol","estelada","piruleta","xarxa","tortuga","bruixot"]
#conte les paraules

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


def joc():
    while Lista_ahorcado[8]!=8 and "_" in Lista_partida:
        print(Lista_partida)
        x=input("introdueix lletra: ")
        if x in palabra:
            for j in range(len(palabra)):
                if palabra[j]==x:
                    Lista_partida.pop(j)
                    Lista_partida.insert(j,x)
            print("Correcte!")
        else:
            Lista_ahorcado.append(Lista_ahorcado[8]+1)
            Lista_ahorcado.pop(8)
            print("incorrecte!")
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


