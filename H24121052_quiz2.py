a=float(input("enter the shopping amount: "))
b=input("enter the membership level (Regular or Gold): ")
if b == "Regular" or "Gold":
	if b == "Regular":
		if a<= 1000:
			c=a
			print(b, "$"+str(c))
		if a > 1000:
			c= a*0.9
			print(b, "$"+str(c))
		if a > 2000:
			c= a*0.85
			print(b, "$"+str(c))
		if a > 3000:
			c= a*0.8
			print(b, "$"+str(c))
	if b == "Gold":
		if a<= 1000:
			c=a
			print(b, "$"+str(c))
		if a > 1000:
			c= a*0.85
			print(b, "$"+str(c))
		if a > 2000:
			c= a*0.8
			print(b, "$"+str(c))
		if a > 3000:
			c= a*0.75
			print(b, "$"+str(c))	
	else:
		print("Invalid membership level. Please enter 'regular' or 'Gold'.")




