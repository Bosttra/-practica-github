x=input().split(" ")
x=[int(x[0]),int(x[1]),int(x[2])]
x[2]+=1
if x[2]==60 or x[2]>60:
    x[2]-=60
    x[1]+=1
if x[1]>60 or x[1]==60:
    x[1]-=60
    x[0]+=1

if x[0]==0:
    print("00", end=":")
else:
    print(x[0], end=":")

if x[1]==0:
    print("00", end=":")
else:
    print(x[1], end=":")

if x[2]==0:
    print("00")
else:
    print(x[2])