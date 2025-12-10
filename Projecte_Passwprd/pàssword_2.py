print("     La seva contrasenya  ha de cumplir esl seguents requisits")
print("1; El primer digit ha de ser>=1 i <=5") 
print("2; El segon digit ha de ser una lletra minuscula")
print("3; El tercer digit ha de ser una lletra majuscula")
print("4; El cuart digit ha de ser un simbol d'aquests: *,_,@")
print("5; El cinqué digit ha de ser una lletra minuscula")
print("6; El sise digit ha de ser un numero >=6, <=9")
print("7;(digit opcional) El sete digit ha de ser un simbol d'aquests: &,/,#")
print("8;(digit opcional) El vuite digit ha de ser uh numero <=5")
malintents=""
num=0
maj=0
min=0
simbol=0
rep=0
while not num>=3 or not maj>=2 or not min>=2 or not simbol>=2:
    rep+=1
    num=0
    maj=0
    min=0
    simbol=0
    rep=0
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
            
        if not num>=2:
            print("error en el numero de numeros")
        if not maj>=2:
            print("error en el numero de majusculas")
        if not min>=2:
            print("error en el numero de minuscula")
        if not simbol>=2:
            print("error en el numero de simbols")


    else:
        malintents+=password+" / "
        print("falta de llargada: ")


if rep>1:
    print(f"el numero d'intents ha sigut {rep} les contrasenyes han sigut {malintents[:-3]}")
print("la contrannya final ha sigyt", password)