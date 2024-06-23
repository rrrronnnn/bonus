a=int(input('Input the force:')) #設定F的數值
b=int(input('Input the mass of m1:')) #設定m1的數值
c=int(input('Input the distance:')) #設定r的數值
d=1/(6.67*(10**-11))
e=299792458
print('The mass of m2:'{(c*c)*d*(1/b)*a}) #計算m2的值
print('The energy of m2:'{(c*c)*d*(1/b)*a*(e*e)})