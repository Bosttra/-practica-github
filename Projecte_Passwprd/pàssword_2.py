print("     La seva contrasenya  ha de cumplir esl seguents requisits")
print("1; Ha d'haver-hi 3 numeros ho més.") 
print("2; Ha d'haver-hi 2 majusculas ho més.")
print("3; Ha d'haver-hi 2 minusculas ho més.")
print("4; Ha d'haver-hi 2 simbols ho més.")
print("minim total de dijits: 8")

malintents=""
num=0
maj=0
min=0
simbol=0

for z in range(3):

    num=0
    maj=0
    min=0
    simbol=0

    password=input("introdueix una contrasenya: ")
    if len(password)>=8:
        for j in password:
            if j.isdigit():
                num+=1
            if j.isupper():
                maj+=1
            if j.islower():
                min+=1
            if not j.isalnum():
                simbol+=1
            
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


    else:
        
        print("falta de llargada: ")
    malintents+=password+" / "




print(f"les contrasenyes han sigut {malintents[:-3]}")



#Contrasenyes de testeig:
#3IL//Mn99 ------ format incorrecte (minúscules)-----Ben executat
#lO2@%52Ol ------ format correcte--------------------Ben executat
