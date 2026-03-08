import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

u=70.0
g=9.81
target_z=70.0

fig=plt.figure(figsize=(12,8))
ax=fig.add_subplot(111,projection='3d')
print("Drawing 3D flight path")

step_count=0
for i in range(100):
    path_x=[0.0]
    path_y=[0.0]
    path_z=[0.0]

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
        path_x.append(s_x)
        path_y.append(s_y)
        path_z.append(s_z)
        step_count+=1
        if step_count % 50 == 0:
            ax.scatter(s_z, s_x, s_y, color='black', s=5, alpha=0.3)
    ax.plot(path_z,path_x,path_y,color='red',alpha=0.15,lw=1)
ax.set_xlabel('Distance(Z/m)')
ax.set_ylabel('Slide Drift(X/m)')
ax.set_zlabel('Height(Y/m)')
ax.set_title('3D Flight Path Analysis')

plt.savefig('archery_3d_paths.png', dpi=300)
print("Simulation Finished. 3D Plot saved.")
plt.show()