A=input("Number:")
a=len(A)
for i in range(0,a):
    x=A[i]
    if (int(x)%2!=0):
        print(x,end=" ")
