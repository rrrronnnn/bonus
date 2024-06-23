numbers=input("Enter a sequence of integers seperated by whitespace:").split()
lics=[]
for i in numbers:
	y=[]
	y.append(int(i))
	for j in range(numbers.index(i),len(numbers)):
		if int(numbers[j])>int(y[-1]):
			y.append(int(numbers[j]))		
	if len(y)>	len(lics):
		lics=y
print("Length:",len(lics))
print("LICS:",lics)



