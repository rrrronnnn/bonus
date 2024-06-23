s=["+","-","^","*",]
s2=["*","^"]
pn=input("Input polynomial: ")
p=list(pn)
x=int(input("the value of X"))
print(p)
print(len(p))
y=[]
i=0
n=0
z=[]
m=0
#若開頭為負X
if p[0]=="-":
	y.append(-x)
	i+=1
while i<len(p):
	if p[i]=="X":
		y.append(x)
		i+=1
		
	
	elif p[i] in s:
		z.append(p[i])
		i+=1
		
	else:
		if i < len(p)-1:
			l=0
			i_n=i
			while i < len(p)-1:
				if not p[i+1] in s :
					i+=1
					l+=1
				else:
					break
			y.append(int(pn[i_n:i_n+1+l]))
			i+=1
		else:
			y.append(p[i])	
			i+=1
ans=[]
ia=0
ans.append(int(y[0]))
while m<len(z):

	if z[m]=="^":
		ans[ia]=ans[ia]**int(y[m+1])
		m+=1

	elif z[m]=="*":
		if z[m+1]=="^":
			ans[ia]=ans[ia]*int(y[m+1])**int(y[m+2])
			m+=2
		else:
			ans[ia]=ans[ia]*int(y[m+1])
			m+=1


	
	elif z[m]=="+":
		if m < len(z)-1:
			if not z[m+1] in s2:
				ans[ia]=ans[ia]+int(y[m+1])
				m+=1
			else:
				ans.append(int(y[m+1]))
				ia+=1
				m+=1		
		else:
			ans[ia]=ans[ia]+int(y[m+1])
			m+=1
	

	elif z[m]=="-":
		if m < len(z)-1:
			if not z[m+1] in s2:
				ans[ia]=ans[ia]-int(y[m+1])
				m+=1
				ia+=1	
		else:
			ans[ia]=ans[ia]+int(y[m+1])
			m+=1
	print(m)
	print(ans)
	print(ia)
print(y)
print(z)
print(sum(ans))


