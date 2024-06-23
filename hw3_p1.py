n=int(input("Input the total number of student (n>0)"))
y=list(range(1,n+1))
#串列*n 使其看似迴圈
x=y*n
#"J":要刪掉的數字
j=3
#兩個人的例外
if n==2:
	print("The last ID is :2")
#len(x)==n表示串列僅剩一個號碼
while len(x)!=n:
#"k"為被刪掉的數字前的位置
	k=	x.index(j)-1
#刪掉所有J
	while j in x:
		x.remove(j)
#下一個刪掉的數字
	j=x[k+3]
print("The last ID is :",x[0])
