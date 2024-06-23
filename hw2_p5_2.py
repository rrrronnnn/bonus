pw=str(input("Input a string: "))
#first word
f=0
fw=f
n=len(pw)
#last word
lw=n
h=1
while True:
	if fw==0:
		if pw[fw:lw:1]==pw[lw-1::-1]:
			tpw=pw[fw:lw:1]
			break

		else:
			lw+=-1
			fw+=-1
	
	else:
		if pw[fw:lw:1]==pw[lw-1:fw-1:-1]:
			tpw=pw[fw:lw:1]
			break

		else:
			lw+=-1
			fw+=-1

	if fw<f:
		fw=f+h
		lw=n
		h+=1
length=len(tpw)		
print(tpw)
print("Length is:",length)


