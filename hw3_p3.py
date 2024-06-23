a=["+","-","-","-"]
b="".join(a*7)+"+"
c="|   "
d=c*7+"|"
#symbol
s=[1,2,3,4,5,6,7]

check1,check2,check3,check4=0,0,0,0

#1
#直線straight(共有七排)
check_horizontal=[]
while check1<7:
		check_horizontal.append('')
		check1+=1
straight=[]
#2
#horizontal 橫排
check_straight=[]
		
while check2<6:
		check_straight.append(' ')
		check2+=1
		
h=[]
#3
#斜線slash right up
check_sru=[]
		
while check3<6:
		check_sru.append(' ')
		check3+=1
sru=[]
#4
#斜線slash left up
check_slu=[]
		
while check4<6:
		check_slu.append(' ')
		check4+=1
slu=[]


#檢查是否獲勝

count1=0





while count1<7:
	inlist=[]
	count2=0
	while count2<6:
		inlist.append(' ')
		count2+=1
	straight.append(inlist)
	count1+=1


i=0
while i<6:
	print(b)
	print(d)
	h.append(list(d))
	if i==5:
		print(b)
	i+=1
number=1
while number<=7:
	print(" ",number,end=" ")
	number+=1
print()
		


i1,i2,i3,i4,i5,i6,i7=0,0,0,0,0,0,0
print(len(h))
game_over=1
while game_over==1:
	chess_count=0
	while game_over==1:
		if chess_count%2==0:
			chess="x"
			i=int(input('player x:'))
		else:
			chess="o"
			i=int(input('player o:'))
		#填棋子
		
		if not i in s:
			print("error ,please enter again")
			break

		if i ==1:	
			if i1==6:
				print("滿了重選")
				break
			straight[0][i1]=chess
			check_horizontal[0]+=chess
			#check_straight[i1]+=chess
			i1+=1
		elif i ==2:
			if i2==6:
				print("滿了重選")
				break			 
			straight[1][i2]=chess
			check_horizontal[1]+=chess
			#check_straight[i2]+=chess
			i2+=1
		elif i ==3:
			if i3==6:
				print("滿了重選")
				break			
			straight[2][i3]=chess
			check_horizontal[2]+=chess
			#check_straight[i3]+=chess
			i3+=1 
		elif i ==4:	
			if i4==6:
				print("滿了重選")
				break		
			straight[3][i4]=chess
			check_horizontal[3]+=chess
			#check_straight[i4]+=chess
			i4+=1 
		elif i ==5:	
			if i5==6:
				print("滿了重選")
				break		 
			straight[4][i5]=chess
			check_horizontal[4]+=chess
			#check_straight[i5]+=chess
			i5+=1
		
		elif i ==6:
			if i6==6:
				print("滿了重選")
				break
			straight[5][i6]=chess
			check_horizontal[5]+=chess
			#check_straight[i6]+=chess
			i6+=1
		elif i ==7:
			if i7==6:
				print("滿了重選")
				break
			straight[6][i7]=chess
			check_horizontal[6]+=chess
			#check_straight[i7]+=chess
			i7+=1
		tie=0
		
		
		h1=0
		s2=5
		
		check_straight_copy=list(check_straight)
		check_sru_copy=list(check_sru)
		check_slu_copy=list(check_slu)
		while h1<6:
			s1=0
			h2=2
			while s1<7:

				h[h1][h2]=straight[s1][s2]
				check_straight_copy[h1]+=straight[s1][s2]
			
				h2+=4
				s1+=1
			s2+=-1
			h1+=1
		sr1=0
		ssr1=0
		ssr2=2
		check_r=5
		while sr1 <6:
			ssr11=ssr1
			ssr22=ssr2
			while ssr22 <=check_r:
				check_sru_copy[sr1]+=straight[ssr11][ssr22]

				
				ssr11+=1
				ssr22+=1
			sr1+=1
			if ssr2!=0:
				ssr2+=-1
			else:
				if ssr11==7:
					check_r+=-1
				ssr1+=1
				

		sl1=0
		ssl1=0
		ssl2=3
		check_l=0
		while sl1 <6:
			ssl11=ssl1
			ssl22=ssl2
			while ssl22 >=check_l:
				check_slu_copy[sl1]+=straight[ssl11][ssl22]
				ssl11+=1
				ssl22+=-1
			sl1+=1
			if ssl2!=5:
				ssl2+=1
			else:
				if ssl11==7:
					check_l+=1
				ssl1+=1



		
		i=0
		while i<6:
			print(b)
			print(''.join(h[i]))
			h.append(list(d))
			if i==5:
				print(b)
			i+=1
		number=1
		while number<=7:
			print(" ",number,end=" ")
			number+=1
		print()
		chess_count+=1
		#平手
		if i1==6 and i2==6 and i3==6 and i4==6 and i5==6 and i6==6 and i7==6:
			print("Tie!")
			tie+=1
			game_over+=1
			break
		#檢查
		ic1=0
		while ic1<7:
			if "oooo" in check_horizontal[ic1]:
				game_over+=1
				winner="o"
				break
			elif "xxxx" in check_horizontal[ic1]:
				game_over+=1
				winner="x"
				break
			else:
				ic1+=1
		ic2=0
		while ic2<6:
			if "oooo" in check_straight_copy[ic2]:
				game_over+=1
				winner="o"
				break
			elif "xxxx" in check_straight_copy[ic2]:
				game_over+=1
				winner="x"
				break
			else:
				ic2+=1
		ic3=0
		while ic3<6:
			if "oooo" in check_sru_copy[ic3]:
				game_over+=1
				winner="o"
				break
			elif "xxxx" in check_sru_copy[ic3]:
				game_over+=1
				winner="x"
				break
			else:
				ic3+=1
		ic4=0
		while ic4<6:
			if "oooo" in check_slu_copy[ic4]:
				game_over+=1
				winner="o"
				break
			elif "xxxx" in check_slu_copy[ic4]:
				game_over+=1
				winner="x"
				break
			else:
				ic4+=1
		'''
		print(check_horizontal)
		print(check_straight_copy)
		
		print(straight)
		print(check_sru_copy)
		print(check_slu_copy)
		'''

		
if tie==0:		
	print("winner is :",winner)
		#print("".join(h))

#print("".join(y))
