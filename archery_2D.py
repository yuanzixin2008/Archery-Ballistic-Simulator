import numpy as np
import matplotlib.pyplot as plt
u=70.0
g=9.81
target_z=70.0

scores = []
results_x=[]
results_y=[]
for i in range(100):
    s_z=0.0
    s_y=0.0
    s_x=0.0
    vx=0.0
    k=0.02
    t=0.0
    gap=0.01
    
    random_angle=np.random.normal(4.9,0.1)
    theta=np.radians(random_angle)
    uy=u*np.sin(theta)
    uz=u*np.cos(theta)
    wind_accel=np.random.normal(0,2.0)

    while(s_z<target_z):
        s_z+=uz*gap
        s_y+=uy*gap
        s_x+=vx*gap
        uz-=k*uz*gap
        uy-=k*uy*gap+g*gap
        vx+=wind_accel*gap-k*vx*gap
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
circles = [0.5, 1.0, 1.5, 2.0]
colors = ['gold', 'red', 'blue', 'black']
for r, c in zip(circles, colors):
    circle = plt.Circle((0, 1.2), r, color=c, fill=False, lw=2, alpha=0.3)
    plt.gca().add_patch(circle)
scores = []
for x, y in zip(results_x,results_y):
    dist = np.sqrt(x**2 + (y - 1.2)**2)
    if dist < 0.5: scores.append(10)
    elif dist <1.0: scores.append(9)
    elif dist <1.5: scores.append(7)
    elif dist < 2.0: scores.append(5)
    else: scores.append(0)
print("Simulation Finished")
print(f"Average Score:{np.mean(scores):.2f}")
plt.show()