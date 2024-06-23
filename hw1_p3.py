#統計系_H24121052_金榮恩
v=eval(input("Input velocity(m/s)"))
c=299792458
print("Percentage of the light speed=",(v/c))
#算出r值
gamma=1/((1-(v*v)/(c*c))**0.5)
#Δtp of Alpha Centauri
tp1=4.3/gamma
#Δtp of Barnard’s Star
tp2=6.0/gamma
#Δtp of Betelgeuse (in the Milky Way)
tp3=309/gamma
#Δtp_ Andromeda Galaxy (closest galaxy)
tp4=2000000/gamma
print("Travel time to Alpha Centauri =",tp1)
print("Travel time to Barnard’s Star =",tp2)
print("Travel time to Alpha Betelgeuse =",tp3)
print("Travel time to  Andromeda Galaxy (closest galaxy) =",tp4)

