import math
x=input().split(" ")
x=[int(i) for i in x]
print(math.floor(x[0]/x[1]), math.ceil(x[0]%x[1]))