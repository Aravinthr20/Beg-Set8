A=str(input("Number:"))
x=[]
for i in range(0,2):
    i=input("Value:")
    x.append(i)
    x.sort()
if (A>x[0]) and (A<x[1]):
    print("Yes")
else:
    print("No")