n=int(input("Input a integer number: "))
a=0
b=1
i=n-1
while i>0:
	a+=b
	i+=-1
	b+=a
	i+=-1
ont=n-(n//10*10)
if ont==1:
	on="st"
elif ont==2:
	on="nd"
elif ont==3:
	on="rd"
else:
	on="th"
if n==11 or n==12 or n==13:
	on="th"


if n%2==0:
	print("The "+str(n)+on,"Fibonacci sequence number is:",a)
else:
	print("The "+str(n)+on,"Fibonacci sequence number is:",b)	