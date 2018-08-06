A=str(input("Number:"))
d=A.find(".")
d=d+1
l=A[d]
if (int(l) >5):
    print(round(float(A)))
else:
    print(round(float(A)+1))