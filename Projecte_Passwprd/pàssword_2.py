print("     La seva contrasenya  ha de cumplir esl seguents requisits")
print("1; Ha d'haver-hi 3 numeros ho més.") 
print("2; Ha d'haver-hi 2 majusculas ho més.")
print("3; Ha d'haver-hi 2 minusculas ho més.")
print("4; Ha d'haver-hi 2 simbols ho més.")
print("minim total de dijits: 8")

#es diuen tots els requisits. 
# no hi ha limit de xifres establertes.

rejistre=""#es la variable que registrara totes les contrasenyes introduides.
num=0#variable que conta el numero de numeros que hi ha en la contrasenya introduida
maj=0#variable que conta el numero de lletres Majuscules que hi ha en la contrasenya introduida
min=0#variable que conta el numero de lletres minsucules que hi ha en la contrasenya introduida
simbol=0#variable que conta el numero de simbols no numerics ni alfavetics que hi ha en la contrasenya introduida

for z in range(3):

    num=0
    maj=0
    min=0
    simbol=0

    #es reinicien les variables per a caa contrasenya

    password=input("introdueix una contrasenya: ")
    if len(password)>=8:
        for j in password:

            #la variable obtrindra el valor de tots el simbols de la contrasenya

            if j.isdigit():
                num+=1
                #calcula si es un numero
            if j.isupper():
                maj+=1
                #calcula si es una lletra majuscula
            if j.islower():
                min+=1
                #calcula si es una lletra minuscula
            if not j.isalnum():
                simbol+=1
                #calcula si es un simbol no alfanumeric

        if not num>=3:
            print("error en el numero de numeros")
        if not maj>=2:
            print("error en el numero de majusculas")
        if not min>=2:
            print("error en el numero de minuscula")
        if not simbol>=2:
            print("error en el numero de simbols")
        if  simbol>=2 and min>=2 and maj>=2 and num>=3:
            print("contrasenya correcte")
        #calcula si els requisits es compleixen si no es dibuixen per pantalla, 
        # no es dibuixen junts per millor visualització


    else:
        
        print("falta de llargada: ")
        # en cas de que no es compleixi el minim de caracters no es calculara la resta, es obi que fallara algun

    rejistre+=password+" / "
    # en tots es casos es rejistrarà la contrasenya 




print(f"les contrasenyes han sigut {rejistre[:-3]}")



#Contrasenyes de testeig:
#1)3IL//Mn99 --------------format incorrecte (minúscules)-----Ben executat
#2)lO2@%52Ol --------------format correcte--------------------Ben executat
#3)EST3334-----------------falta de llargada------------------Ben executat
#4)çççÇÇÇ22@---------------error en el numero de numeros 
#)                         error en el numero de simbols------Ben executat
#5)##eses··ENs234----------contrasenya correcte---------------Ben executat
#6)43r45kUJt#@4------------contrasenya correcte---------------Ben executat
#7)ednpus43----------------error en el numero de numeros
#                          error en el numero de majusculas
#                          error en el numero de simbols------Ben executat
#8)pic.·$mama--------------error en el numero de numeros
#                          error en el numero de majusculas---Ben executat
#9)eS,   23----------------error en el numero de numeros
#                          error en el numero de majusculas
#                          error en el numero de minuscula----Ben executat
#yj64e5w7goñ8/G&F%(E#~#----contrasenya correcte-----------Ben executat