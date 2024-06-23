l=int(input("Enter the number of layers (2 to 5) = "))
slt=int(input("Enter the side length of the top layer = "))
gl=int(input("Enter the growth of each layer = "))
tw=int(input("Enter the trunk width (odd number< 3 to 9) = "))
th=int(input("Enter the trunk height (4 to 10) = "))
w=gl*(l-1)+slt-1
rw=w
t=1
ln=1
at=t
while ln<=l:
	while t<=slt:
		if t==1 or at==slt:
			a=0
		else:
			a=2*(at-1)-1
		if t==1:
			last=0
		elif t==slt:
			last=slt*2-2
		else:
			last=1
		print(" "*rw,end="")
		print("#"+"@"*a+"#"*last)
		at+=1
		t+=1
		rw+=-1
	rw=w-1
	at=2
	t=2
	slt+=gl
	ln+=1
while th>0:
	print(" "*int((w-(tw-1)/2)),end="")
	print("|"*tw,end="\n")
	th+=-1

