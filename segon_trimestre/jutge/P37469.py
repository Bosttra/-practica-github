x=int(input())
y=[(x/3600),int(x%3600/60),x%3600%60]
print(y[0],y[1],y[2])