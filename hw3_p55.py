s=input("list").split()
print(s)
#M是str!!!
M=max(s)
L=len(s)
i=0
y=[]

while i<int(M):
	y.append("")
	i+=1
l_check=0
while l_check <int(L):

	#input 柱子到串列裡面
	ip=0
	while ip<int(M):
		if ip<int(s[l_check]):
			y[ip]+="o"
			ip+=1
		else:
			y[ip]+="x"
			ip+=1
	l_check+=1
print(y)
'''
I=-1
while -I<=int(L):
	if -I==int(L):
		print(y[0])

	else:
		print(y[I])
	I+=-1
'''
#檢查

i=0
water=0
while i<len(y):
	x=[]
	checkx=0
	z=list(y[i])
	while checkx<int(len(y[i])):
	
		#print(z)
		if "o" in z:
			num=z.index("o")

			x.append(num)
			z.remove("o")
			z.insert(num,"x")
			print(x)
			
		checkx+=1
		daihow=0

	

	while daihow<len(x):
		if daihow!=len(x)-1:
			a=y[i][x[daihow]:x[daihow+1]].count("x")
			water+=a
			
		daihow+=1
			
	i+=1
print(water)




