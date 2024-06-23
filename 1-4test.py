thief = 1
while thief <= 4:
	true_thief=thief
	a=true_thief!=1
	b=true_thief==3
	c=true_thief==4
	d=true_thief!=4	
	if thief==1:
		if(a,b,c,d)==(0,1,1,1):
			print('The thief is', thief)
	if thief==2:
		if(a,b,c,d)==(1,0,1,1):
			print('The thief is', thief)
	if thief==3:
		if(a,b,c,d)==(1,1,0,1):
			print('The thief is', thief)
	if thief==1:
		if(a,b,c,d)==(1,1,1,0):
			print('The true thief is', thief)	
	thief = thief + 1 