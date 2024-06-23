#統計系_H24121052_金榮恩
h=eval(input("Input the height of the 1st ball:"))
m1=eval(input("Input the mass of the 1st ball:"))
m2=eval(input("Input the mass of the 2nd ball:"))
g=9.8
#算出位能
U=m1*g*h
#頂點時U=平地時的Ek=E_mechanical
#利用動能公式求得u1
u1=((2*U)/m1)**0.5
u2=0
v2=2*m1/(m1+m2)*u1+(m1-m2)/(m1+m2)*u2
print("The velocity of the 1st ball after slide=",u1)
print("The velocity of the 2nd ball after collision=",v2)