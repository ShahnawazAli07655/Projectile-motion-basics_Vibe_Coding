import numpy as np
import matplotlib.pyplot as plt
v0 = float(input("Enter the velocity (in m/s) :"))
x= float(input("\nEnter the angle of projection (in degrees) :"))
theta = np.radians(x)
g = 9.8
vx0 = v0 * np.cos(theta)
vy0 = v0 * np.sin(theta)
T= (2 * vy0)/g
R=vx0 * T
H=(vy0**2)/(2*g)
print("\nTime of flight=",T," sec")
print("Maximum height reached=",H," m")
print("Range=",R," m")
x,y=[],[]
i=0
r = lambda t : vx0 * t
h= lambda t : vy0 * t -0.5* g * t**2
viewtime= float(input("\nFor how long you want to see the plot (in sec)?"))
while i<=viewtime:
    x.append(r(i))
    y.append(h(i))
    i=i+0.02
plt.plot(x,y,"+",label="Projectile",color="green")
plt.title("Projectile motion")
plt.xlabel("Horizontal distance (in m)-->")
plt.ylabel("Vertical distance (in m)-->")
plt.grid()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()
