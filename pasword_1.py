print("     La seva contrasenya  ha de cumplir esl seguents requisits")
print("1; El primer digit ha de ser >=1 i <=5")
print("2; El segon digit ha de ser una lletra minuscula")
print("3; El tercer digit ha de ser una lletra majuscula")
print("4; El cuart digit ha de ser un simbol d'aquests: *,_,@")
print("5; El cinqué digit ha de ser una lletra minuscula")
print("6; El sise digit ha de ser un numero >=6, <=9")
print("7;(digit opcional) El sete digit ha de ser un simbol d'aquests: &,/,#")
print("8;(digit opcional) El vuite digit ha de ser uh numero <=5")
password=input("introdueix una contrasenya: ")
x=0
y=[""]
if not int(len(password)) <=8 or not int(len(password))>=6:
    print("error en la llargada de la contrasenya")
    x=0
elif int(len(password))<=8 and int(len(password))>=6:

    if password[0].isdigit()==True:
        if not int(password[0])<=5 and not int(password[0])>=1:
            y.append("error en el primer digit")
            x=1
    else:
        y.append("error en el primer digit")
        x=1

    if not password[1].isalpha():
        y.append("error en el segont digit")
        x=1

    elif password[1].isalpha():
        if not password[1].islower():
            y.append("error en el segont digit")
            x=1

    if not password[2].isalpha():
        y.append("error en el tercer digit")
        x=1
    elif password[2].isalpha():
        if not password[2].isupper():
            y.append("error en el tercer digit")
            x=1

    if not password[3]=="*"or not password[3]=="_"or not password[3]=="@":
        y.append("error en el cuart digit")
        x=1

    if not password[4].islower():
        y.append("error en el cinque digit")
        x=1

    if password[5].isdigit()==True:
        if not int(password[5])<=9 and not int(password[5])>=6:
            y.append("error en el sise digit")
            x=1
    else:
        y.append("error en el sise digit")
        x=1

    if len(password)>6:
        if not password[6]=="&"or not password[6]=="/"or not password[6]=="#":
            y.append("error en el sete digit")
            x=1

    if len(password)>7:
        if password[7].isdigit()==True:
            if int(password[7])<=5:
                y.append("error en el vuite digit")
                x=1
        else:
            y.append("error en el vuite digit")
            x==1
if x==0:
    print("contrasenya correcte")
else:
    print(y)
