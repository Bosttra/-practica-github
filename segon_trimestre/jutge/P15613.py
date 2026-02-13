x=int(input())
if x<10:
    print("it's cold")
    if x<0 or x==0:
        print("water would freeze")
elif x>30:
    print("it's hot")
    if x==100 or x>100:
        print("water would boil")
else:
    print("it's ok")