#基本圖形架構
bomb=0
import random
board="  "+"+---"*9+"+"
alp={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9}
alp_re={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i'}
a=list(range(1,82))
a_1=[]
for i in a:
	a_1.append("-")
a_2=list(a_1)

#說明
def help():
	print("Enter the column followed by the row (ex: a5). To add or remove a flag, add 'f' to the cell (ex: a5f). ")
	

#列印圖形
def play():
	print("    a   b   c   d   e   f   g   h   i")
	print(board)
	c=0
	print("1 ",end="")
	for i in a:
		print("|",a_2[i-1],end=" ")
		c+=1
		if c%9==0:
			print('|')
			print(board)
			if c//9+1!=10:
				print(c//9+1,end=" ")
#插旗
def flag():
	where=int(alp[ie_1[0]])+(int(ie_1[1])-1)*9
	if a_2[where-1]=="-":
		a_2[where-1]="F"
	elif a_2[where-1]=="F":
		a_2[where-1]="-"
	else:
		print("Cannot put a flag there")

#結束叫出炸彈
def call():

	ind=a_1.index("x")
	a_2[ind]="x"
	a_1[ind]="-"

#埋放炸彈檢查
def put():
	not_safe=[]
	#檢查右邊
	if pre_wait[-1][0]!="i":
		r=[alp_re[int(alp[pre_wait[-1][0]])+1],int(pre_wait[-1][1])]

		if a_1[int(alp[r[0]])+(int(r[1])-1)*9-1]=="x":
			not_safe.append(r)

	#檢查左邊
	if pre_wait[-1][0]!="a":
		l=[alp_re[int(alp[pre_wait[-1][0]])-1],int(pre_wait[-1][1])]

		if a_1[int(alp[l[0]])+(int(l[1])-1)*9-1]=="x":
			not_safe.append(l)

	#檢查上邊
	if pre_wait[-1][1]!='1' and pre_wait[-1][1]!=1:
		u=[pre_wait[-1][0],int(pre_wait[-1][1])-1]

		if a_1[int(alp[u[0]])+(int(u[1])-1)*9-1]=="x":
			not_safe.append(u)

		#檢查右上
		if u[0]!="i":
			ur=[alp_re[int(alp[u[0]])+1],u[1]]

			if a_1[int(alp[ur[0]])+(int(ur[1])-1)*9-1]=="x":
				not_safe.append(ur)

		#檢查左上
		if u[0]!="a":
			ul=[alp_re[int(alp[u[0]])-1],u[1]]

			if a_1[int(alp[ul[0]])+(int(ul[1])-1)*9-1]=="x":
				not_safe.append(ul)

	#檢查下邊
	#print(type(wait[-1][1]))
	if pre_wait[-1][1]!='9' and pre_wait[-1][1]!=9:
		d=[pre_wait[-1][0],int(pre_wait[-1][1])+1]
		#print(d)

		if a_1[int(alp[d[0]])+(int(d[1])-1)*9-1]=="x":
			not_safe.append(d)

		#檢查右下
		if d[0]!="i":
			dr=[alp_re[int(alp[d[0]])+1],d[1]]

			if a_1[int(alp[dr[0]])+(int(dr[1])-1)*9-1]=="x":
				not_safe.append(dr)

		#檢查左下
		if d[0]!="a":
			dl=[alp_re[int(alp[d[0]])-1],d[1]]

			if a_1[int(alp[dl[0]])+(int(dl[1])-1)*9-1]=="x":
				not_safe.append(dl)

	pre_wait.pop()
	judge=len(not_safe)

	return judge





#檢查炸彈
def check(ab):
	bomb=0
	non=0
	where_2=int(alp[wait[-1][0]])+(int(wait[-1][1])-1)*9

	safe=[]
	#檢查猜的那格是否為bomb
	if com[where_2]=="x":
		wait.pop()
		print('bomb!!!')
		bomb+=1
		ab=0
		return ab
	
	if a_1[where_2-1]!="-" :
		wait.pop()
		return ab
	
	#檢查右邊
	if wait[-1][0]!="i":
		r=[alp_re[int(alp[wait[-1][0]])+1],int(wait[-1][1])]
	#print(int(alp[r[0]])+(int(r[1])-1)*9)
		if com[int(alp[r[0]])+(int(r[1])-1)*9]!="x":
			safe.append(r)
	else:
		non+=1
	#檢查左邊
	if wait[-1][0]!="a":
		l=[alp_re[int(alp[wait[-1][0]])-1],int(wait[-1][1])]

		if com[int(alp[l[0]])+(int(l[1])-1)*9]!="x":
			safe.append(l)
	else:
		non+=1
	#檢查上邊
	if wait[-1][1]!='1' and wait[-1][1]!=1:
		u=[wait[-1][0],int(wait[-1][1])-1]

		if com[int(alp[u[0]])+(int(u[1])-1)*9]!="x":
			safe.append(u)

		#檢查右上
		if u[0]!="i":
			ur=[alp_re[int(alp[u[0]])+1],u[1]]

			if com[int(alp[ur[0]])+(int(ur[1])-1)*9]!="x":
				safe.append(ur)
		else:
			non+=1
		#檢查左上
		if u[0]!="a":
			ul=[alp_re[int(alp[u[0]])-1],u[1]]

			if com[int(alp[ul[0]])+(int(ul[1])-1)*9]!="x":
				safe.append(ul)
		else:
			non+=1
	else:
		non+=3
	#檢查下邊
	#print(type(wait[-1][1]))
	if wait[-1][1]!='9' and wait[-1][1]!=9:
		d=[wait[-1][0],int(wait[-1][1])+1]
		#print(d)

		if com[int(alp[d[0]])+(int(d[1])-1)*9]!="x":
			safe.append(d)

		#檢查右下
		if d[0]!="i":
			dr=[alp_re[int(alp[d[0]])+1],d[1]]

			if com[int(alp[dr[0]])+(int(dr[1])-1)*9]!="x":
				safe.append(dr)
		else:
			non+=1
		#檢查左下
		if d[0]!="a":
			dl=[alp_re[int(alp[d[0]])-1],d[1]]

			if com[int(alp[dl[0]])+(int(dl[1])-1)*9]!="x":
				safe.append(dl)
		else:
			non+=1
	else:
		non+=3

	wait.pop()

	a_2[where_2-1]=8-len(safe)-non
	

	if a_2[where_2-1]==0:
		for i in range(len(safe)):
			if safe[i] not in wait:

				if 	a_2[int(alp[safe[i][0]])+(int(safe[i][1])-1)*9-1]=="-" :

					wait.append(safe[i])


	return ab


play_game=1
while play_game:
	a_1=[]
	for i in a:
		a_1.append("-")
	a_2=list(a_1)

	play()
	help()	
	print("Type 'help to show this message again.")
	#第一枚&隨機置放炸彈
	i=input("Enter the cell: ")
	ie=list(i)
	where=int(alp[ie[0]])+(int(ie[1])-1)*9
	print(where)
	for i in range(10):
		del a_1[0]
		a_1.append("x")
	pre_wait=[]
	while True:
		pre_wait.append(ie)
		random.shuffle(a_1)
		ok=put()
		print(ok)
		if a_1[where-1]!="x":
			if ok==0:
				break

	com=dict(zip(a,a_1))

	#wait:待檢查
	wait=[]
	wait.append(ie)


	ab=1
	while True:
		if wait==[]:
			break
		check(ab)
	play()
	while ab:

		i_1=input("Enter the cell: ")
		#輸入錯誤
		if len(i_1)<2 :
			print('Invalid Cell1')
			continue
		if len(i_1)>3 and i_1!="help":
			print('Invalid Cell2')
			continue
		if len(i_1)==3:
			if i_1[0] not in alp:
				print('Invalid Cell3')
				continue
			if int(i_1[1]) not in alp_re:
				print('Invalid Cell4')
				continue
			if i_1[-1]!='f':
				print('Invalid Cell5')

				continue
		if len(i_1)==2:
			if i_1[0] not in alp:
				print('Invalid Cell6')

				continue

			if int(i_1[1]) not in alp_re:
				print('Invalid Cell7')

				continue

		#操作提示
		if i_1==('help'):
			help()
			continue
		ie_1=list(i_1)

		where=int(alp[ie_1[0]])+(int(ie_1[1])-1)*9
		if a_2[where-1]=="F" and len(ie_1)==2:
			print("There's a flag there")
			continue
		if ie_1[-1]=="f":
			print("hi")
			flag()
			play()
			continue

		wait.append(ie_1)

		while True:
			if wait==[]:
				break
			ab=check(ab)
		if ab==0:
			break
		play()
		if a_2.count("-")+a_2.count("F")==10:
			print("You win!")
			break

	#收尾


	for i in alp:
			for j in alp_re:
				end_check=[]
				where=int(alp[i])+(int(j)-1)*9
				if a_1[where-1]!="x":
					end_check.append(i)
					end_check.append(j)
					wait.append(end_check)

					check(ab)
	for i in range(10):
		call()
	play()
	if bomb!=0:
		print('You Losed!:D')
	print(bomb)
	ask=input('Play again? (y/n) :')
	if ask=='y':
		continue
	elif ask =="n":
		play_game=0


