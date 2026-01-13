#56. Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se 
#compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El 
#dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se 
#visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la 
#realización de un pedido, si quiere gestionar otro. 
#El establecimiento contempla los siguientes descuentos:
#Si el total a pagar es entre 20 y 30 euros, se aplica un descuento del 5%
#Si el total a pagar es superior a 30 euros, se aplica un descuento del 15%
#Una vez se finaliza la introducción de todos los pedidos de un cliente, debe aparecer por pantalla:
#• El número de pedidos realizados
#• Total a pagar.
#• Total con IVA (10%)
#• Total con el descuento aplicado.
m=True
total=0
ped=0
while m==True:
    ped+=1
    print("MENÚ")
    print("1. Bocadillo de calamares- 9 €")
    print("2. Bocadillo de chistorra - 4.5 €")
    print("3. Bikini de jamón - 2.5 €")
    
    Menú=int(input("introducca el numero del menu que quiera tomar: "))
    match Menú:
        case 1:
            total+=9
        case 2:
            total+=4.5
        case 3:
            total+=2.5

    print("ACOMPAÑAMIENTO")
    print("1. Patatas finas - 1.5 €")
    print("2. Patatas gruesas - 1.75 €")
    print("3. Patatas rústicas - 2 €")

    acom=int(input("introducca el numero del acompanyamiento que quiera tomar: "))
    match acom:
        case 1:
            total+=1.5
        case 2:
            total+=1.75
        case 3:
            total+=2
    print("BEBIDAS")
    print("1. Coca cola - 2 €")
    print("2. Acuarius - 1.5 €")
    print("3. Agua - 1 €")

    bebida=int(input("introducca el numero del bebida que quiera tomar: "))

    match bebida:
        case 1:
            total+=2
        case 2:
            total+=1.5
        case 3:
            total+=1
    r=input("vols fer una altre comanda? Sí/No ")
    if r in"No.no.":
        m=False

print("numero de comandes: ", ped)
print("Preu: ", total,"€")
print("IVA: ",total+total/10)
final=total+total/10
if final and final>=30:
    final-=final*0.15
    print("total a pagar amb descompte de 15%: ", final)
elif final<30:
    final-=final*0.05
    print("total a pagar amb descompte de 5%: ", final)
else:
    final-=0
    print("total a pagar amb descompte de 0%: ", final)
