string=input("Enter a string:")
length=len(string) 
reversed_string=string[::-1]  #反轉字串


i=0
newstring="" #設定預設值

while i<length:  #外部迴圈控制從第幾個數字開始

	x=1

	while i+x<=length: 
		if string[i:i+x] in reversed_string and len(string[i:i+x])>=len(newstring):  #如果字串中從第i字到i+x字有出現在反轉字串中,且此字串長度大於前一個newstring長度時,newstring值就會改變
			newstring=string[i:i+x]

		x=x+1  #迴圈中,會不斷確認到從i開始,到i+x的字有沒有出現在反轉字串中,如果i到i+x的字串沒出現在反轉字串中,內部迴圈就終止

	i=i+1  #終止內部迴圈後,i+1,進入另一個迴圈


print("Longest palindrome substring:",newstring)
print("Length is:",len(newstring))


