year=int(input("Please input year: "))
month=int(input("Please input month: "))
m=month
d=1
if m== 1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
	days=31
elif m==2:
	if year%4==0:
		days=29
	else:
		days=28
	if year%100==0 and year%400!=0:
		days=28
else:
	days=30
if m==1:=2
	m=13
	year+=-1
if m==2:
	m=14
	year+=-1
c=year//100
y=year%100
week=(y+int(y/4)+int(c/4)-2*c+int(26*(m+1)/10)+d-1)%7
print(week)
print("Sun Mon Tue Wed Thu Fri Sat")
print("    "*week+"01 ", end=" ")
f=2
while f<=days:
	week+=1
	if week==7:
		print("",end="\n")
		week=0
	print(str(f).zfill(2)+" ",end=" ")

	f+=1
