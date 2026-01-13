#x=3
#for x in range(10):
#    print(x)
#print(x)
#for x in range(3):
#    x=0
#    print(x)
#neuronas=int(input("introduze el numero de neuronas: "))
#for x in range( 1,neuronas +1):
#    print(x, "neurona es tonta")
password="a1e4jkE"
total= 0
totalV=0
for x in password:
    if x.isnumeric():
        total+= int(x)
    elif x.lower() in "aeiou":
        totalV +=1 
print(total)
print(totalV)