x=input().split(" ")
if x[1]==x[0]:
    print(x[0],"=",x[1])
elif max(x)==x[0]:
    print(x[0],">",x[1])
else:
    print(x[0],"<",x[1])