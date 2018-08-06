A=int(input("Number:"))
B=int(input("Number:"))
a=A*B
num=0
for i in range(2,a):
    if (a%i==0):
        if (i*i==a):
            num=num+1
if (num>0):
    print("Yes")
else:
    print("No")