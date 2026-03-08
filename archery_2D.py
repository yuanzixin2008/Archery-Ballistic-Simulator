import numpy as np
import matplotlib.pyplot as plt
u=70.0
g=9.81
target_z=70.0
results_x=[]
results_y=[]
scores=[]
for i in range(100):
    s_z=0.0
    s_y=0.0
    s_x=0.0
    vx=0.0
    k=0.02
    t=0.0
    gap=0.01
    
    random_angle=np.random.normal(5.1,0.15)
    theta=np.radians(random_angle)
    uy=u*np.sin(theta)
    uz=u*np.cos(theta)
    wind_speed=np.random.normal(0,3.0)

    while(s_z<target_z):
        s_z+=uz*gap
        s_y+=uy*gap
        s_x+=vx*gap
        uz-=k*uz*gap
        uy-=(k*uy+g)*gap
        vx+=k*(wind_speed-vx)*gap
        t+=gap
    results_x.append(s_x)
    results_y.append(s_y)

plt.figure(figsize=(6,6))
plt.scatter(results_x,results_y, alpha=0.6, c='red', label='Arrows')
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.title("Archery Impact Distribution (100 Arrows)")
plt.xlabel("Horizontal Deviation (m)")
plt.ylabel("Height (m)")
plt.grid(True)
plt.axis('equal')
circles = [0.06, 0.12, 0.24, 0.36]
colors = ['gold', 'red', 'blue', 'black']

height=1.3
for r, c in zip(circles, colors):
    circle = plt.Circle((0,height), r, color=c, fill=False, lw=2, alpha=0.3)
    plt.gca().add_patch(circle)

for x, y in zip(results_x,results_y):
    dist = np.sqrt(x**2 + (y - height)**2)
    if dist < 0.06: scores.append(10)
    elif dist <0.12: scores.append(9)
    elif dist <0.24: scores.append(7)
    elif dist <0.36: scores.append(5)
    else: scores.append(0)
print("Simulation Finished")
print(f"Average Score:{np.mean(scores):.2f}")
plt.show()