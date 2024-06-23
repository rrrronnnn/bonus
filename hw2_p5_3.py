n=int(input("The number of the requested elememt in Fibonacci (n) = "))
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
	k=a
else:
	k=b

s1=str(input("The first string for Palindromic detection (s1) = "))
s2=str(input("The second string for Palindromic detection (s2) = "))
si=0
while si<2:

	if si==0:
		pw=s1
	elif si==1:
		pw=s2

	#first word
	f=0
	fw=f
	n_p2=len(pw)
	#last word
	lw=n_p2
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
			lw=n_p2
			h+=1
	length=len(tpw)
	if si==0:
		l1=length
		tpw1=tpw
	elif si==1:
		l2=length
		tpw2=tpw
	si+=1		
tpt=str(input("The plaintext to be encrypted: "))
l_tpt=len(tpt)
i_tpt=0
et=""
while i_tpt<l_tpt:
	#ev= encrypted vowel
	ev_tpt=tpt[i_tpt]
	#ASCII-ord
	asc1=ord(ev_tpt)
	#Caesar Cipher
	cc=asc1+k
	#Affine Cipher
	ac=l1*cc+l2
	#back to range
	btr=((ac-65)%26)+65
	#ASCII-chr
	asc2=chr(btr)
	i_tpt+=1
	et+=asc2
print("----- extract key for encrypted method -----")
print("The "+str(n)+on,"Fibonacci sequence number is:",k)
print("Longest palindrome substring within the first string is:",tpw1)
print("Length is:",l1)
print("Longest palindrome substring within the second string is:",tpw2)
print("Length is:",l2)
print("----- The encryption completed -----")
print("The encrypted text is:",et)


