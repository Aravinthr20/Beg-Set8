A=str(input("String:"))
a=len(A)
l=a//2
if(a%2==0):
    x=A.replace(A[l], "*")
    print(x.replace(A[l-1], "*"))
else:
    print(A.replace(A[l], "*"))