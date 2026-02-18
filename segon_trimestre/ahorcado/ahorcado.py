import  random
Lista_partida=[]
Lista_ahorcado=""
Lista_palabrasecreta=["maduixa","escombra","llampada","cargol","estelada","piruleta","xarxa","tortuga","bruixot"]
palabra=list(Lista_palabrasecreta[random.randint(0,len(Lista_palabrasecreta))])

for x in palabra:
    Lista_partida.append("_" )

print("adivina la paraula")
print(Lista_partida)
while len(Lista_ahorcado)==8 or "_" in Lista_partida:
    x=input("introdueix lletra: ")
    if x in palabra:
        while palabra.index(x):
            Lista_partida.pop(palabra.index(x))
            Lista_partida.insert(palabra.index(x), x)

