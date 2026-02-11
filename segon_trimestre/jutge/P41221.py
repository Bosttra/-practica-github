x=[]
y=[]
while len(x)<3:
    y=input()

    y=y.split(" ")
    while '' in y:
        y.remove('')
    x=x+y

print(int(x[0])+int(x[1])+int(x[2]))