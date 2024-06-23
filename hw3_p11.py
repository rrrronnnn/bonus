n=int(input("Input the total number of student (n>0)"))
y=list(range(1,n+1))
x=y*n
j=3
if n==2:
	print("The last ID is :2")
while len(x)!=n:
	k=	x.index(j)-1
	while j in x:
		x.remove(j)
	j=x[k+3]
print("The last ID is :",x[0])
