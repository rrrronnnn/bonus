n=6
tn=1
sum=0
while tn<n:
	if n//tn==0:
		sum+=tn
	tn+=1
if sum==n:
	print(n)

