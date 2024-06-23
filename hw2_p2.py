n=int(input("Input the range number"))
m=2
while m<=n:
	tn=1
	sum=0
	while tn<m:
		if m%tn==0:
			sum+=tn
		tn+=1
	if sum==m:
		print(m)
	m+=1
