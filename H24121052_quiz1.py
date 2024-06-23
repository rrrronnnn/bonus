R=float(input("Please input a Richter scale value:"))
#Richter scale value
energy=10**(1.5*R+4.8)
#energy_of_TNT
energy2=energy/4.184e9
#energy of nutritious lunch
energy3=energy/2930200
print("Richter scale value:",R)
print("Equivalencein Joules:",energy)
print("Equivalencein in tons of TNT:",energy2)
print("Equivalencein in the number of nutritious lunches:",energy3)
