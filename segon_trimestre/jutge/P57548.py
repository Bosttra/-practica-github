x=input()
x=x.split(" ")
if len(x)<2:
    x.append(int(input()))
print(int(x[0])+int(x[1]))