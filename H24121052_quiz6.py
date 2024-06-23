alp=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
num=list(range(0,26))
dic=dict(zip(alp,num))
import random
c=list(alp)
random.shuffle(c)



ans=c[0]
print(ans)
print(dic[ans])
game=1
def enter (inp):
	if inp>dic[ans]:
		print("The alphabet you are looking for is alphabetically lower")
	if inp<dic[ans]:
		print("The alphabet you are looking for is alphabetically higher")
	if inp==dic[ans]:
		print("Congrats! You guessed the alphabet",ans,"in",count,"tries.")
		game==0
count=1
r1,r2,r3,r4,r5,r6,r7=0,0,0,0,0,0,0
while game:
	
	guess=input("Guess the lowercase alphhabet:" )
	

	if guess in alp:
		guess_number=dic[guess]
		enter(guess_number)
		count+=1
	



		if guess_number >=0 and guess_number<=3:
			r1+=1
		if guess_number >=4 and guess_number<=7:
			r2+=1
		if guess_number >=8 and guess_number<=11:
			r3+=1
		if guess_number >=12 and guess_number<=15:
			r4+=1
		if guess_number >=16 and guess_number<=19:
			r5+=1
		if guess_number >=20 and guess_number<=23:
			r6+=1
		if guess_number >=24 and guess_number<=25:
			r7+=1

		if guess_number==dic[ans]:
			break
print("Guess Histogram:")
print("a-d: ",r1*"*")
print("e-h: ",r2*"*")
print("i-l: ",r3*"*")
print("m-p: ",r4*"*")
print("q-t: ",r5*"*")
print("u-x: ",r6*"*")
print("y-z: ",r7*"*")




