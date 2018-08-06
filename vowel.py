a=str(input())
l=len(a)
L=a.lower()
count=0
for i in range(0,l):
    if (a[i]=='a') or (a[i]=='e') or (a[i]=='i') or(a[i]=='o') or (a[i]=='u'):
        count=count+1
        break
if (count>0):
    print("Yes")
else:
    print("No")