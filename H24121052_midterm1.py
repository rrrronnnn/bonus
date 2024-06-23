j_origin=9
while j_origin>0:
	i=9
	j=j_origin 
	while i>0:
		#ab=i*j
		#a=" %-3d " % (ab)
		print(i,"x",j,"=",(i*j),end=("\t"))
		j+=-1
		if j%3==0:
			print()
			j=j_origin
			i+=-1
	print()
	j_origin+=-3

    