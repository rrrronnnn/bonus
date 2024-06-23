print("Welcome to the simple caculator program!")
while True:
	fn=float(input("Enter the first number: "))
	sn=float(input("Enter the second number: "))
	ao=input("Select an arithmetic operation (+,-,*,/): ")

	if ao=="+":
		print(fn+sn)
	elif ao=="-":
		print(fn-sn)
	elif ao=="*":
		print(fn*sn)
	elif ao=="/":
		if sn!= 0:
			print(fn/sn)
		else:
			print("Error: Division by zero!")
			continue
	ac=input("Do you want to perform another caculation? (yes or no): ")
	if ac=="yes":
		continue
	elif ac=="no":
		break
print("Goodbye!")

