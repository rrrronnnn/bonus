'''
n=int(input("n"))
i=0
variables={}
while i< n:
	i+=1
	variables[f"var{i}"]=i
for key, value in variables.items():
	print(key,"=", value)
print(variables)
print(variables{0})

s=[[]for _ in range (6)]
s[1].append(1)
s[2].append(1)
s[2].append(1)
s[2].append(1)
s[3].append(1)
print(s)
'''
a=[1,"q",1,1,1]
b=[2,2,2,2,2]
a[0]=b[1]
print(a)
a[1]+="3"
print(a)