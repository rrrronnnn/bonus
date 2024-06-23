#統計系_H24121052_金榮恩
#輸入各項數值
F=eval(input("Input the force"))
m1=eval(input("Input the mass of the object 1 "))
r=eval(input("Input the distance"))
#利用公式算出m2
m2=F*r*r/((6.67e-11)*m1)
#再算出E
E=m2*(299792458**2)
#列印結果
print("The mass of m2 =",m2)
print("The energy of m2 =",E)