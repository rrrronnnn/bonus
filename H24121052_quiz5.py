row_size=int(input("Enter the row"))
col_size=int(input("Enter the columns"))
dec=list(range(0,row_size*col_size))

dec_2=[]
for i in dec:
	print("A",end=(" "))
	i+=1
	if i%col_size==0:
		print()
for i in dec:
	dec_2.append("A")

i=0
def run (a,b):
	dec_2[nn-1]=nv
	for i in dec:
		print(dec_2[i],end=(" "))
		i+=1
		if i%size==0:
			print()

edit=input("Enter the reserved seat")
nv=R
each=edit.split("|")
for i in range(0,len(each)):
	new=each[i].split(",")
	nn=(int(new[0]))*(row_size)+(int(new[1])+1)
	print(nn)	
	run(nn,nv)
print(dec_2)
